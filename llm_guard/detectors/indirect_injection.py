import re

PATTERNS = [
    r"the document says",
    r"summary says",
    r"as written above",
    r"according to the article",
    r"hidden note",
    r"instructions inside",
    r"embedded message",
    r"text says to ignore"
]

def detect(text):
    lowered = text.lower()
    for p in PATTERNS:
        if p in lowered:
            return {"detected": True, "threat_type": "indirect_injection", "confidence": 0.93}
    return {"detected": False, "threat_type": None, "confidence": 0.0}
