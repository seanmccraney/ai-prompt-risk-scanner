from prompt_risk_scanner.models import Category, RiskLevel


def test_risk_level_values():
    assert RiskLevel.LOW.value == "low"
    assert RiskLevel.MEDIUM.value == "medium"
    assert RiskLevel.HIGH.value == "high"
    assert RiskLevel.CRITICAL.value == "critical"

def test_category_values():
    assert Category.PROMPT_INJECTION.value == "prompt_injection"
    assert Category.JAILBREAK.value == "jailbreak"
    assert Category.CREDENTIAL_ACCESS.value == "credential_access"
    assert Category.SENSITIVE_INFORMATION.value == "sensitive_information"
    assert Category.CBRNE.value == "cbrne"
    assert Category.DRUGS_AND_CONTROLLED_SUBSTANCES.value == "drugs_and_controlled_substances"