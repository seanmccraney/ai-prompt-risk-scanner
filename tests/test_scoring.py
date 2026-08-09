from prompt_risk_scanner.models import RiskLevel
from prompt_risk_scanner.scoring import calculate_risk_level


def test_calculate_risk_level():
    assert calculate_risk_level(0) == RiskLevel.LOW
    assert calculate_risk_level(4) == RiskLevel.LOW
    assert calculate_risk_level(5) == RiskLevel.MEDIUM
    assert calculate_risk_level(9) == RiskLevel.MEDIUM
    assert calculate_risk_level(10) == RiskLevel.HIGH
    assert calculate_risk_level(14) == RiskLevel.HIGH
    assert calculate_risk_level(15) == RiskLevel.CRITICAL
    assert calculate_risk_level(100) == RiskLevel.CRITICAL