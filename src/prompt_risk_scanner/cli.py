"""cli.py is going to, ask user for a prompt, send prompt to scanner, and print the results in a user friendly format."""

from prompt_risk_scanner.formatter import print_scan_result
from prompt_risk_scanner.scanner import scan


def main() -> None:
    """Main function to run the CLI."""

    prompt = input("Enter a prompt: ") 
    result = scan(prompt)
    print_scan_result(result)

if __name__ == "__main__":
    main()