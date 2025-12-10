VIOLATION_PHRASES = [
    "my system prompt",
    "my internal instructions",
    "as an ai developed by",
    "i am not allowed to",
    "i should not reveal",
    "according to my policy",
    "i will ignore safety",
    "bypassing safety",
    "developer instructed me"
]

def detect(text: str) -> dict:
    lowered = text.lower()

    for phrase in VIOLATION_PHRASES:
        if phrase in lowered:
            return {
                "detected": True,
                "threat_type": "output_policy_violation",
                "confidence": 0.9
            }

    return {
        "detected": False,
        "threat_type": None,
        "confidence": 0.0
    }
