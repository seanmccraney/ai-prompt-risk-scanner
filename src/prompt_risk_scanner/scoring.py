
from prompt_risk_scanner.models import RiskLevel


def calculate_risk_level(score: int) -> RiskLevel:

    """Determine the risk level based on the risk score."""
    if score <= 4:
        return RiskLevel.LOW
    elif score <= 9:
        return RiskLevel.MEDIUM
    elif score <= 14:
        return RiskLevel.HIGH
    else:
        return RiskLevel.CRITICAL