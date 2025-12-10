from .detectors.pii import detect as pii_detect
from .detectors.content_safety import detect as safety_detect
from .detectors.output_violation import detect as output_violation_detect

def validate(output: str) -> dict:
    pii_result = pii_detect(output)
    if pii_result["detected"]:
        return {
            "valid": False,
            "reason": pii_result["threat_type"]
        }

    safety_result = safety_detect(output)
    if safety_result["detected"]:
        return {
            "valid": False,
            "reason": safety_result["threat_type"]
        }

    output_violation_result = output_violation_detect(output)
    if output_violation_result["detected"]:
        return {
            "valid": False,
            "reason": output_violation_result["threat_type"]
        }

    return {
        "valid": True,
        "reason": None
    }
