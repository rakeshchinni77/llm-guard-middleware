import re

# Email, Phone, and API-like key patterns
EMAIL_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PHONE_PATTERN = r"\b\d{10}\b"
API_KEY_PATTERN = r"sk-[a-zA-Z0-9]{20,}"
JWT_PATTERN = r"eyJ[a-zA-Z0-9_-]+\.eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+"

def detect(text: str) -> dict:
    if re.search(EMAIL_PATTERN, text):
        return {
            "detected": True,
            "threat_type": "email_pii",
            "confidence": 0.9
        }

    if re.search(PHONE_PATTERN, text):
        return {
            "detected": True,
            "threat_type": "phone_pii",
            "confidence": 0.9
        }

    if re.search(API_KEY_PATTERN, text):
        return {
            "detected": True,
            "threat_type": "api_key_leak",
            "confidence": 0.95
        }

    if re.search(JWT_PATTERN, text):
        return {
            "detected": True,
            "threat_type": "jwt_token_leak",
            "confidence": 0.95
        }

    return {
        "detected": False,
        "threat_type": None,
        "confidence": 0.0
    }
