import os
import json
from llm_guard.guard import LLMGuard

ATTACK_DIR = "tests/attacks"
BENIGN_DIR = "tests/benign"
OUTPUT_FILE = "evaluation_results.json"


def load_prompts_from_dir(folder_path):
    prompts = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        prompts.append(line)
    return prompts


def evaluate():
    guard = LLMGuard(policy="balanced")

    attack_prompts = load_prompts_from_dir(ATTACK_DIR)
    benign_prompts = load_prompts_from_dir(BENIGN_DIR)

    true_positive = 0
    false_negative = 0
    true_negative = 0
    false_positive = 0

    # Evaluate attacks
    for prompt in attack_prompts:
        result = guard.process(prompt)
        if not result["allowed"]:
            true_positive += 1
        else:
            false_negative += 1

    # Evaluate benign prompts
    for prompt in benign_prompts:
        result = guard.process(prompt)
        if result["allowed"]:
            true_negative += 1
        else:
            false_positive += 1

    total_attacks = len(attack_prompts)
    total_benign = len(benign_prompts)

    detection_rate = true_positive / total_attacks if total_attacks else 0
    false_negative_rate = false_negative / total_attacks if total_attacks else 0
    false_positive_rate = false_positive / total_benign if total_benign else 0

    results = {
        "total_attack_prompts": total_attacks,
        "total_benign_prompts": total_benign,
        "true_positive": true_positive,
        "false_negative": false_negative,
        "true_negative": true_negative,
        "false_positive": false_positive,
        "detection_rate": round(detection_rate, 4),
        "false_negative_rate": round(false_negative_rate, 4),
        "false_positive_rate": round(false_positive_rate, 4)
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print("Evaluation Complete")
    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    evaluate()
