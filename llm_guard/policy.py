
from .config import (
    STRICT_THRESHOLD,
    BALANCED_THRESHOLD,
    PERMISSIVE_THRESHOLD
)

def apply_policy(risk: float, policy: str) -> bool:
    if policy == "strict":
        return risk >= STRICT_THRESHOLD

    elif policy == "balanced":
        return risk >= BALANCED_THRESHOLD

    elif policy == "permissive":
        return risk >= PERMISSIVE_THRESHOLD

    else:
        # Default to balanced if invalid policy is provided
        return risk >= BALANCED_THRESHOLD