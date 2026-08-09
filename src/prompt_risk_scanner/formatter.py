from prompt_risk_scanner.models import ScanResult


def print_scan_result(result: ScanResult) -> None:
    """Print a formatted Scan Result"""

    print(f"Risk Level: {result.risk_level.value}".upper())
    print(f"Risk Score: {result.risk_score}")
    
    print("Matched Rules:")
    if result.matched_rules:
        for rule in result.matched_rules:
            print(f"- {rule.name}")
    else:
        print("- None")
    
    print("Matched Indicators:")
    if result.matched_indicators:
        for indicator in result.matched_indicators:
            print(f"- {indicator}")
    else:
        print("- None")
    
    print(f"Explanation: {result.explanation}")
    print(f"Recommendation: {result.recommendation}")