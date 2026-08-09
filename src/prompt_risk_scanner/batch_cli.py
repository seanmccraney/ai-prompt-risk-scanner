from prompt_risk_scanner.batch import scan_batch
from prompt_risk_scanner.csv_loader import read_prompts_from_csv
from prompt_risk_scanner.formatter import print_scan_result
from prompt_risk_scanner.models import RiskLevel


def main() -> None:
  
    
    csv_file_path = "data/sample_prompts.csv"
    # Read prompts from the CSV file
    prompts = read_prompts_from_csv(csv_file_path)
    # Scan the prompts in batch
    results = scan_batch(prompts)
    # Print the results for each prompt
    for result in results:
        print("=" * 45)
        print("Prompt")
        print("=" * 45)
        print(result.original_prompt)

        print_scan_result(result)
        print()
    # Generate a summary of the batch scan results
    print("=" * 45)
    print("Batch Summary")
    print("=" * 45)
    print()
    print(f"Total Prompts: {len(results)}")
    print()

    low_count = 0
    medium_count = 0
    high_count = 0
    critical_count = 0
    escalation_count = 0

    for result in results:
        if result.risk_level is RiskLevel.LOW:
            low_count += 1
        elif result.risk_level is RiskLevel.MEDIUM:
            medium_count += 1
        elif result.risk_level is RiskLevel.HIGH:
            high_count += 1
        elif result.risk_level is RiskLevel.CRITICAL:
            critical_count += 1
        if result.escalate:
            escalation_count += 1


    print(f"LOW:           {low_count}")
    print(f"MEDIUM:        {medium_count}")
    print(f"HIGH:          {high_count}")
    print(f"CRITICAL:      {critical_count}")
    print()
    print(f"ESCALATIONS:   {escalation_count}")

if __name__ == "__main__":
    main()