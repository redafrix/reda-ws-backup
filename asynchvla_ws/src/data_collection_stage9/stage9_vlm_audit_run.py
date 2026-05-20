from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Any

import torch


PROMPT = """You are auditing a robot manipulation rollout label.

You see a review sheet with candidate BEFORE/AFTER images and, when available, the best same-state sibling BEFORE/AFTER images. The sheet also includes simulator metrics and our current label.

Task instruction:
{task_instruction}

Our current label:
{our_label}

Bad subtype:
{bad_subtype}

Our label reasons:
{label_reasons}

Raw simulator bad evidence:
{raw_bad_evidence}

Raw simulator good/progress evidence:
{raw_good_evidence}

Important rules:
- Do not call the candidate bad only because the task is not completed yet.
- Do not call the candidate bad only because terminal success is false.
- Call it bad only if the visible behavior or shown metrics indicate real degradation: object dropped, moved away from goal, wrong object, collision, clear no-progress when progress is expected, or candidate visibly worse than the same-state sibling.
- If the image pair is insufficient, answer unclear.
- If our label is VALIDATED_BAD but you see progress or no visible/metric bad event, mark suspicious_label true.
- JSON only. No prose outside JSON.

Return exactly this JSON schema:
{{
  "behavior": "good" | "bad" | "unclear",
  "failure_type": "none" | "no_progress" | "object_drop" | "wrong_object" | "misplacement" | "collision" | "moved_away" | "unclear",
  "candidate_vs_sibling": "better" | "worse" | "similar" | "no_sibling" | "unclear",
  "suspicious_label": true | false,
  "suggested_label_action": "keep" | "downgrade_to_ambiguous" | "upgrade_to_review" | "manual_review",
  "confidence": 0.0,
  "explanation": "one short sentence"
}}
"""


BLIND_PROMPT = """You are auditing a robot manipulation rollout from before/after images.

You see a review sheet with candidate BEFORE/AFTER images and, when available, the best same-state sibling BEFORE/AFTER images.

Task instruction:
{task_instruction}

Important rules:
- Do not call the candidate bad only because the task is not completed yet.
- Call it bad only if the visible behavior indicates real degradation: object dropped, moved away from goal, wrong object, collision, clear no-progress when progress is expected, or candidate visibly worse than the same-state sibling.
- If the before/after images are insufficient, answer unclear.
- JSON only. No prose outside JSON.

Return exactly this JSON schema:
{{
  "behavior": "good" | "bad" | "unclear",
  "failure_type": "none" | "no_progress" | "object_drop" | "wrong_object" | "misplacement" | "collision" | "moved_away" | "unclear",
  "candidate_vs_sibling": "better" | "worse" | "similar" | "no_sibling" | "unclear",
  "suspicious_label": false,
  "suggested_label_action": "keep" | "downgrade_to_ambiguous" | "upgrade_to_review" | "manual_review",
  "confidence": 0.0,
  "explanation": "one short sentence"
}}
"""


def load_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def build_prompt(row: dict[str, Any], blind: bool = False) -> str:
    if blind:
        return BLIND_PROMPT.format(task_instruction=row.get("task_instruction"))
    return PROMPT.format(
        task_instruction=row.get("task_instruction"),
        our_label=row.get("our_label"),
        bad_subtype=row.get("bad_subtype"),
        label_reasons=row.get("label_reasons"),
        raw_bad_evidence=row.get("raw_bad_evidence"),
        raw_good_evidence=row.get("raw_good_evidence"),
    )


def extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    text = re.sub(r"^```(?:json)?", "", text).strip()
    text = re.sub(r"```$", "", text).strip()
    try:
        return json.loads(text)
    except Exception:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        try:
            return json.loads(text[start : end + 1])
        except Exception:
            return {"parse_error": True, "raw_text": text}
    return {"parse_error": True, "raw_text": text}


def load_model(model_name: str, load_in_4bit: bool):
    from transformers import AutoProcessor

    quantization_config = None
    dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
    if load_in_4bit:
        try:
            from transformers import BitsAndBytesConfig

            quantization_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_use_double_quant=True,
            )
            dtype = None
        except Exception as exc:
            print(f"4bit_unavailable={exc}", flush=True)

    if "Qwen3-VL" in model_name:
        from transformers import Qwen3VLForConditionalGeneration

        model_cls = Qwen3VLForConditionalGeneration
    elif "Qwen2.5-VL" in model_name or "Qwen2_5" in model_name:
        from transformers import Qwen2_5_VLForConditionalGeneration

        model_cls = Qwen2_5_VLForConditionalGeneration
    else:
        from transformers import AutoModelForImageTextToText

        model_cls = AutoModelForImageTextToText

    kwargs = {"device_map": "auto"}
    if dtype is not None:
        kwargs["torch_dtype"] = dtype
    if quantization_config is not None:
        kwargs["quantization_config"] = quantization_config
    model = model_cls.from_pretrained(model_name, **kwargs)
    processor = AutoProcessor.from_pretrained(model_name, min_pixels=224 * 224, max_pixels=1024 * 1024)
    model.eval()
    return model, processor


def run_one(model, processor, row: dict[str, Any], max_new_tokens: int, blind_prompt: bool) -> dict[str, Any]:
    from qwen_vl_utils import process_vision_info

    image_path = row["contact_sheet_path"]
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image_path},
                {"type": "text", "text": build_prompt(row, blind=blind_prompt)},
            ],
        }
    ]
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = inputs.to(model.device)
    with torch.inference_mode():
        generated = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
    generated_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated)
    ]
    output_text = processor.batch_decode(generated_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    parsed = extract_json(output_text)
    return {"raw_response": output_text, "parsed": parsed}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out-jsonl", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--categories", nargs="*", default=None)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--num-shards", type=int, default=1)
    parser.add_argument("--max-new-tokens", type=int, default=256)
    parser.add_argument("--load-in-4bit", action="store_true")
    parser.add_argument("--blind-prompt", action="store_true")
    args = parser.parse_args()

    rows = list(load_jsonl(Path(args.manifest)))
    if args.categories:
        wanted = set(args.categories)
        rows = [r for r in rows if r.get("category") in wanted]
    rows = [r for i, r in enumerate(rows) if i % args.num_shards == args.shard_index]
    if args.limit:
        rows = rows[: args.limit]

    Path(args.out_jsonl).parent.mkdir(parents=True, exist_ok=True)
    done = set()
    out_path = Path(args.out_jsonl)
    if out_path.exists():
        for row in load_jsonl(out_path):
            if row.get("audit_id"):
                done.add(row["audit_id"])

    model, processor = load_model(args.model, args.load_in_4bit)
    started = time.time()
    with out_path.open("a") as f:
        for idx, row in enumerate(rows):
            if row.get("audit_id") in done:
                continue
            t0 = time.time()
            try:
                result = run_one(model, processor, row, args.max_new_tokens, args.blind_prompt)
                status = "ok"
                error = None
            except Exception as exc:
                result = {"raw_response": "", "parsed": {"parse_error": True}}
                status = "error"
                error = repr(exc)
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            record = {
                **row,
                "vlm_model": args.model,
                "status": status,
                "error": error,
                "seconds": time.time() - t0,
                "result": result,
            }
            f.write(json.dumps(record, default=str) + "\n")
            f.flush()
            print(json.dumps({
                "idx": idx,
                "audit_id": row.get("audit_id"),
                "status": status,
                "seconds": round(time.time() - t0, 2),
                "elapsed": round(time.time() - started, 2),
            }), flush=True)


if __name__ == "__main__":
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    main()
