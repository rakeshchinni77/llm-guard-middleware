import re

KEYWORDS = [
    "dan", "developer mode", "unfiltered",
    "no restrictions", "no filter", "roleplay",
    "pretend you are", "break character",
    "do anything now", "act as unrestricted"
]

def detect(text):
    lowered = text.lower()
    for k in KEYWORDS:
        if k in lowered:
            return {"detected": True, "threat_type": "jailbreak", "confidence": 0.98}
    return {"detected": False, "threat_type": None, "confidence": 0.0}
