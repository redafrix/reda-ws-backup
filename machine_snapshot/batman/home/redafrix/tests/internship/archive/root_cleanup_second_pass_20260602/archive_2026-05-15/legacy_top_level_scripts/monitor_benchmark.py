import subprocess
import json
import time

def get_success_rate():
    try:
        cmd = "ssh sam 'cat ~/test/reda_ws/intern_ship_ws/eval_results_100/*.json'"
        output = subprocess.check_output(cmd, shell=True).decode()
        results = []
        # JSONs are saved one after another, possibly not in a valid list format if cat together
        # Actually they are separate files. cat will join them.
        # I'll split by }{ and fix it.
        raw_json = output.replace('}\n{', '},{')
        if raw_json:
            data = json.loads('[' + raw_json + ']')
            successes = [r['success'] for r in data]
            total = len(successes)
            rate = sum(successes) / total * 100
            return total, rate
    except Exception as e:
        return 0, 0

print("Monitoring SimVLA Libero Benchmark on Sam...")
while True:
    total, rate = get_success_rate()
    if total > 0:
        print(f"Progress: {total}/100 | Success Rate: {rate:.2f}%")
    else:
        print("Waiting for first results...")
    time.sleep(300)
