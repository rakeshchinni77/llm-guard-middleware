import re

KEYWORDS = [
    "ignore", "override", "disregard", "bypass",
    "break rules", "no rules", "disable safety",
    "remove restrictions", "forget rules"
]

def detect(text):
    lowered = text.lower()

    # wildcard match: ignore.*instructions
    if re.search(r"ignore.*instruction", lowered):
        return {"detected": True, "threat_type": "direct_injection", "confidence": 0.99}

    # fuzzy keyword detection
    for w in KEYWORDS:
        if w.replace(" ", "") in lowered.replace(" ", ""):
            return {"detected": True, "threat_type": "direct_injection", "confidence": 0.97}

    return {"detected": False, "threat_type": None, "confidence": 0.0}
