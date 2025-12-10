import re

PATTERNS = [
    r"reveal system prompt",
    r"show internal instructions"
]

def detect(text):
    for p in PATTERNS:
        if re.search(p, text):
            return {"detected": True, "threat_type": "leakage_attempt", "confidence": 0.92}
    return {"detected": False, "threat_type": None, "confidence": 0.0}
