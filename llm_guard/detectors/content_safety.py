BAD_WORDS = ["kill", "bomb", "rape", "terrorist"]

def detect(text):
    for w in BAD_WORDS:
        if w in text:
            return {"detected": True, "threat_type": "unsafe_content", "confidence": 0.85}
    return {"detected": False, "threat_type": None, "confidence": 0.0}
