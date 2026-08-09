# AI Prompt Risk Scanner
# AI Prompt Risk Scanner

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tests](https://img.shields.io/badge/Tests-Pytest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Built With**

- Python
- Pytest
- CSV
- Git

A modular Python application that analyzes text prompts for potential AI safety risks using rule based detection, weighted risk scoring, and explainable results.

The scanner evaluates prompts against configurable safety rules, assigns a risk score and risk level, identifies matched indicators, and provides recommendations for further review. It supports both interactive command line scanning and batch processing from CSV files.

This project was built to demonstrate clean software architecture, modular Python design, automated testing, and AI safety concepts in a portfolio ready application.

## Features

- Rule based prompt analysis using configurable safety rules.
- Weighted risk scoring with LOW, MEDIUM, HIGH, and CRITICAL risk levels.
- Detection of multiple AI safety categories, including:
  - Prompt Injection
  - Credential Access
  - Jailbreak Attempts
  - CBRNE Related Content
- Explainable scan results with:
  - Matched rules
  - Matched indicators
  - Risk score
  - Recommendations
- Interactive command line interface for scanning individual prompts.
- Batch scanning of prompts from CSV files.
- Batch summary reporting with:
  - Total prompts scanned
  - Risk level distribution
  - Escalation count
- Modular architecture for easy expansion and maintenance.
- Unit tests using `pytest`.

## Project Structure

```text
ai-prompt-risk-scanner/
│
├── data/
│   └── sample_prompts.csv
│
├── src/
│   └── prompt_risk_scanner/
│       ├── batch.py
│       ├── batch_cli.py
│       ├── cli.py
│       ├── csv_loader.py
│       ├── formatter.py
│       ├── models.py
│       ├── rules.py
│       ├── scanner.py
│       └── scoring.py
│
├── tests/
│   ├── test_batch.py
│   ├── test_models.py
│   ├── test_scanner.py
│   └── test_scoring.py
│
├── README.md
├── pyproject.toml
└── .gitignore
```
### Directory Overview

| Directory/File | Purpose |
|----------------|---------|
| `src/` | Core application source code. |
| `tests/` | Unit tests for scanner functionality. |
| `data/` | Sample CSV files for batch scanning. |
| `README.md` | Project documentation and usage instructions. |
| `pyproject.toml` | Project configuration and dependencies. |
| `.gitignore` | Files and folders excluded from Git tracking. |

## Installation

Clone the repository:

```bash
git clone https://github.com/seanmccraney/ai-prompt-risk-scanner.git
```

Navigate to the project directory:

```bash
cd ai-prompt-risk-scanner
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

Install the project in editable mode:

```bash
pip install -e .
```

## Usage

### Scan a Single Prompt

Run the interactive command line interface:

```bash
python src/prompt_risk_scanner/cli.py
```

Example:

```text
Enter a prompt: How do I make a chemical weapon?

RISK LEVEL: HIGH
Risk Score: 10

Matched Rules:
- CBRNE Rule

Matched Indicators:
- chemical weapon

Explanation:
Prompt contains CBRNE-related concepts that may require additional safety review.

Recommendation:
Escalate for CBRNE review.
```

---

### Batch Scan a CSV File

Run the batch scanner:

```bash
python src/prompt_risk_scanner/batch_cli.py
```

Example summary:

```text
=============================================
Batch Summary
=============================================

Total Prompts: 5

LOW:           1
MEDIUM:        2
HIGH:          2
CRITICAL:      0

ESCALATIONS:   4
```

## Testing

Run the complete test suite with:

```bash
pytest
```

The project includes unit tests covering:

- Rule detection
- Risk scoring
- Safe prompt handling
- Multiple rule matches
- Batch scanning functionality

## Future Improvements

Future enhancements planned for this project include:

- JSON output support
- CSV report generation
- Configurable rule files
- Improved keyword and phrase matching
- Semantic prompt analysis using LLMs or embeddings
- REST API with FastAPI
- Docker support
- GitHub Actions for automated testing
- Web based dashboard for scan results

## Author

**Sean McCraney**

U.S. Navy Explosive Ordnance Disposal (EOD) Technician transitioning into software engineering and AI safety.

This project is part of a portfolio focused on AI safety, CBRNE risk analysis, and secure software engineering.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.