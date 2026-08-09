from prompt_risk_scanner.models import ScanResult
from prompt_risk_scanner.scanner import scan


def scan_batch(prompts: list[str]) -> list[ScanResult]:
    """Scan multiple prompts and return their results."""


    results: list[ScanResult] = []

    for prompt in prompts:
        result = scan(prompt)
        results.append(result)


    return results