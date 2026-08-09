from prompt_risk_scanner.models import RiskLevel, ScanResult
from prompt_risk_scanner.rules import RULES
from prompt_risk_scanner.scoring import calculate_risk_level


def scan(prompt: str) -> ScanResult:
    """Scan a prompt against all configured rules."""

    # Normalize the prompt so rule matching is case-insensitive.
    normalized_prompt = prompt.lower()

    matched_rules = []  
    matched_indicators = []

    # Evaluate every configured rule against the prompt.
    for rule in RULES:
        rule_matched = False

        for indicator in rule.indicators:
            if indicator.lower() in normalized_prompt:
                matched_indicators.append(indicator)
                rule_matched = True

        # Add the rule once if any of its indicators matched.
        if rule_matched:
            matched_rules.append(rule)

    # Calculate the overall risk score and corresponding risk level.
    risk_score = sum(rule.weight for rule in matched_rules)
    risk_level = calculate_risk_level(risk_score)

    # Build a ScanResult containing all matched rules and recommendations.
    if matched_rules:
        explanation = " ".join(rule.explanation for rule in matched_rules)
        recommendation = " ".join(
            rule.recommendation for rule in matched_rules
        )

        return ScanResult(
            original_prompt=prompt,
            matched_rules=matched_rules,
            matched_indicators=matched_indicators,
            risk_score=risk_score,
            risk_level=risk_level,
            explanation=explanation,
            recommendation=recommendation,
            escalate=True,
        )

    # Return a default low-risk result when no rules match.
    return ScanResult(
        original_prompt=prompt,
        matched_rules=[],
        matched_indicators=[],
        risk_score=0,
        risk_level=RiskLevel.LOW,
        explanation="No matching safety rules were triggered.",
        recommendation="No action required.",
        escalate=False,
    )