from dataclasses import dataclass
from enum import Enum


class RiskLevel(str, Enum):
    """Represents the severity assigned to a scanned prompt."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Category(str, Enum):
    """Represents the type of risk identified in a prompt."""

    PROMPT_INJECTION = "prompt_injection"
    JAILBREAK = "jailbreak"
    CREDENTIAL_ACCESS = "credential_access"
    SENSITIVE_INFORMATION = "sensitive_information"
    CBRNE = "cbrne"
    DRUGS_AND_CONTROLLED_SUBSTANCES = "drugs_and_controlled_substances"


@dataclass
class Rule:
    """Represents a single safety rule used to classify prompts."""

    name: str
    category: Category
    risk_level: RiskLevel
    indicators: list[str]
    weight: int
    explanation: str
    recommendation: str


@dataclass
class ScanResult:
    """Represents the result of scanning a prompt."""

    original_prompt: str
    matched_rules: list[Rule]
    matched_indicators: list[str]
    risk_score: int
    risk_level: RiskLevel
    explanation: str
    recommendation: str
    escalate: bool