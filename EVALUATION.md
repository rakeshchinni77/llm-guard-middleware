# Evaluation Report — LLM Prompt Injection Defense Middleware

This document presents the final evaluation results of the **LLM Prompt Injection Defense Middleware**, measured using the complete malicious and benign test suites.

---

## Test Dataset Description

### 🔹 Attack Dataset

- Total Malicious Prompts: **30**
- Attack Categories:
  - Direct Prompt Injection
  - Indirect / RAG-based Injection
  - Jailbreak & Roleplay (DAN) Attacks
  - System Prompt Leakage
  - Obfuscated Injection Attacks
  - Semantic / Unseen Attacks

### 🔹 Benign Dataset

- Total Benign Prompts: **15**
- Categories:
  - General Question Answering
  - Programming & Coding Queries
  - Casual and Conversational Prompts

---

## Final Evaluation Metrics (Submission Results)

| Metric                  | Value          |
| ----------------------- | -------------- |
| Total Attack Prompts    | 30             |
| Total Benign Prompts    | 15             |
| True Positives (TP)     | **30**         |
| False Negatives (FN)    | **0**          |
| True Negatives (TN)     | **15**         |
| False Positives (FP)    | **0**          |
| **Detection Rate**      | **100% (1.0)** |
| False Negative Rate     | **0.0%**       |
| **False Positive Rate** | **0.0%**       |

Evaluation Command Used:

```bash
python scripts/evaluate.py
```
