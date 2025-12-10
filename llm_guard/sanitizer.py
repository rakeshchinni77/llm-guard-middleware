import re
import unicodedata

SUBSTITUTIONS = {
    "0": "o",
    "1": "i",
    "3": "e",
    "4": "a",
    "5": "s",
    "@": "a",
    "$": "s",
    "!": "i"
}

def sanitize(prompt: str) -> str:
    text = unicodedata.normalize("NFKC", prompt)
    text = text.lower()

    # Replace obfuscation characters
    for k, v in SUBSTITUTIONS.items():
        text = text.replace(k, v)

    # Fix split words like "ign or e"
    text = re.sub(r"(\w)\s+(\w)", r"\1\2", text)

    # Remove repeated characters
    text = re.sub(r'(.)\1{2,}', r'\1', text)

    # Normalize spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()
