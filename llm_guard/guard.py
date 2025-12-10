from .sanitizer import sanitize
from .policy import apply_policy
from .risk import aggregate
from .logger import log

from .detectors.prompt_injection import detect as direct_detect
from .detectors.indirect_injection import detect as indirect_detect
from .detectors.jailbreak import detect as jailbreak_detect
from .detectors.leakage import detect as leakage_detect
from .detectors.content_safety import detect as safety_detect
from .detectors.llm_classifier import classify as llm_classify


class LLMGuard:
    def __init__(self, policy: str = "balanced"):
        self.policy = policy

    def process(self, prompt: str) -> dict:
        # Step 1: Sanitize input
        sanitized_prompt = sanitize(prompt)

        # Step 2: Run all detectors
        results = [
            direct_detect(sanitized_prompt),
            indirect_detect(sanitized_prompt),
            jailbreak_detect(sanitized_prompt),
            leakage_detect(sanitized_prompt),
            safety_detect(sanitized_prompt),
            llm_classify(sanitized_prompt)
        ]

        # Step 3: Aggregate risk
        confidences = [r["confidence"] for r in results if r["detected"]]
        final_risk = aggregate(confidences)

        # Step 4: Apply policy decision
        blocked = apply_policy(final_risk, self.policy)

        if blocked:
            log({
                "prompt": prompt,
                "threat_type": [r["threat_type"] for r in results if r["detected"]],
                "confidence": final_risk,
                "policy": self.policy,
                "action": "blocked"
            })

            return {
                "allowed": False,
                "sanitized_prompt": None,
                "reason": "Threat detected"
            }

        # Step 5: Allow prompt
        return {
            "allowed": True,
            "sanitized_prompt": sanitized_prompt,
            "reason": None
        }
