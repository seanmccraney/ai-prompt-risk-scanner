from prompt_risk_scanner.models import Category, RiskLevel, Rule

# Detect prompts that attempt to override or expose system instructions
prompt_injection_rule = Rule(
    name="Prompt Injection Rule",
    category=Category.PROMPT_INJECTION,
    risk_level=RiskLevel.HIGH,
    indicators=[
        "ignore previous instructions",
        "ignore all previous instructions",
        "disregard previous instructions",
        "forget previous instructions",
        "system prompt",
    ],
    weight=5,
    explanation="Prompt attempts to override or expose system instructions.",
    recommendation="Review for prompt injection before processing.",
)
# Detect prompts that attempt to access sensitive credentials
credential_access_rule = Rule(
    name="Credential Access Rule",
    category=Category.CREDENTIAL_ACCESS,
    risk_level=RiskLevel.HIGH,
    indicators=[
        "api key",
        "access token",
        "secret key",
        "password",
    ],
    weight=8,
    explanation="Prompt may be attempting to access or expose credentials.",
    recommendation="Escalate for credential-access review.",
)
# Detect prompts that attempt to bypass AI safety measures or restrictions
jailbreak_rule = Rule(
    name="Jailbreak Rule",
    category=Category.JAILBREAK,
    risk_level=RiskLevel.CRITICAL,
    indicators=[
    "jailbreak",
    "bypass",
    "circumvent restrictions",
    "ignore your safety rules",
    "pretend you have no restrictions",
    "act as dan",
    "bypass safety",
    ],
    weight=10,
    explanation="Prompt may be attempting to bypass safety measures.",
    recommendation="Escalate for jailbreak review.",
)
# detect prompts that attempt to create or use chemical, biological, radiological, nuclear, or explosive materials
cbrne_rule = Rule(
    name="CBRNE Rule",
    category=Category.CBRNE,
    risk_level=RiskLevel.CRITICAL,
    indicators=[
        "explosive",
        "chemical agent",
        "chemical weapon",
        "biological agent",
        "radiological material",
        "nuclear material",
        "toxin",
    ],
    weight=10,
    explanation="Prompt contains CBRNE-related concepts that may require "
    "additional safety review.",
    recommendation="Escalate for CBRNE review.",
)

# List of all defined rules
RULES = [
    prompt_injection_rule,
    credential_access_rule,
    jailbreak_rule,
    cbrne_rule,
]
