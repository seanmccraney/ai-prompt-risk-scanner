import csv


def read_prompts_from_csv(file_path: str) -> list[str]:
    """Read prompts from the prompt column of a CSV file."""

    prompts: list[str] = []

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            prompt = row["prompt"].strip()

            if prompt:
                prompts.append(prompt)

    return prompts