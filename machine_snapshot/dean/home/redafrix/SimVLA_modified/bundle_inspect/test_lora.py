import torch
from transformers import AutoModelForImageTextToText
from peft import LoraConfig, get_peft_model

# Load tiny model
print("Loading model...")
model = AutoModelForImageTextToText.from_pretrained("HuggingFaceTB/SmolVLM-500M-Instruct", torch_dtype=torch.float32, trust_remote_code=True)

# Keep track of original output
# dummy input
input_ids = torch.tensor([[1, 2, 3]])
orig_out = model.model(input_ids=input_ids).last_hidden_state

lora_config = LoraConfig(
    r=16,
    target_modules=["q_proj", "v_proj"],
)
print("Applying LoRA...")
model = get_peft_model(model, lora_config)

# Run through model.model
new_out = model.model.model(input_ids=input_ids).last_hidden_state

# Now let's change a lora weight
for n, p in model.named_parameters():
    if "lora_" in n:
        torch.nn.init.constant_(p, 1.0)

changed_out = model.model.model(input_ids=input_ids).last_hidden_state

print("Original == New:", torch.allclose(orig_out, new_out))
print("New == Changed:", torch.allclose(new_out, changed_out))
