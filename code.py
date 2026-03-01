convert_naves_csv.py
python convert_naves_csv.py

import csv
import json

input_file = "NavesTopicalDictionary.csv"
output_file = "naves.json"

data = []

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        section = row["section"].strip()
        subject = row["subject"].strip()
        entry_text = row["entry"].strip()

        if not subject:
            continue

        # Split by new lines and clean bullets
        topics = []
        lines = entry_text.split("\n")

        for line in lines:
            clean_line = line.strip().lstrip("-").strip()
            if clean_line:
                topics.append(clean_line)

        data.append({
            "section": section,
            "subject": subject,
            "topics": topics
        })

with open(output_file, "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=2, ensure_ascii=False)

print("Conversion complete.")
print("Total subjects:", len(data))
