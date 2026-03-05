generate_daily_verses.py


import json
import random

# Load your KJV Bible JSON
with open("KJV.json", "r", encoding="utf-8") as f:
    bible = json.load(f)

all_verses = []

for book in bible["books"]:
    for chapter in book["chapters"]:
        for verse in chapter["verses"]:
            reference = f'{book["name"]} {chapter["chapter"]}:{verse["verse"]}'
            text = verse["text"]

            all_verses.append({
                "reference": reference,
                "verse": text
            })

# Shuffle so verses are spread across the Bible
random.shuffle(all_verses)

daily = []

for i in range(366):
    v = all_verses[i]

    daily.append({
        "day": i + 1,
        "reference": v["reference"],
        "verse": v["verse"]
    })

# Save output
with open("daily_verses.json", "w", encoding="utf-8") as f:
    json.dump(daily, f, indent=2, ensure_ascii=False)

print("daily_verses.json generated with 366 verses")


python generate_daily_verses.py
