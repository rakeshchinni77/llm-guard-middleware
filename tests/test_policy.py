from llm_guard.policy import apply_policy


def test_strict_policy_blocks_low_risk():
    assert apply_policy(0.2, "strict") is True


def test_balanced_policy_blocks_medium_risk():
    assert apply_policy(0.7, "balanced") is True


def test_permissive_policy_blocks_only_high_risk():
    assert apply_policy(0.95, "permissive") is True


def test_invalid_policy_defaults_to_balanced():
    assert apply_policy(0.7, "invalid") is True
