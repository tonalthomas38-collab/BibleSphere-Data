import xml.etree.ElementTree as ET
import json
import re

# -------- SETTINGS --------
INPUT_XML = "strongshebrew.xml"   # change if your filename differs
OUTPUT_JSON = "hebrew.json"
# --------------------------

def clean_text(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()

def extract_full_text(elem):
    text = elem.text or ""
    for child in elem:
        text += extract_full_text(child)
        if child.tail:
            text += child.tail
    return clean_text(text)

def strip_namespace(tag):
    return tag.split("}")[-1]

def main():
    print("Loading Hebrew XML...")
    tree = ET.parse(INPUT_XML)
    root = tree.getroot()

    entries = []

    for entry in root.iter():
        if strip_namespace(entry.tag) != "entry":
            continue

        strong_id = entry.get("id")
        if not strong_id:
            continue

        number = strong_id  # already like H1

        hebrew_word = ""
        transliteration = ""
        pronunciation = ""
        part_of_speech = ""
        definition = ""
        source = ""
        usage = ""

        for child in entry:
            tag = strip_namespace(child.tag)

            if tag == "w":
                hebrew_word = clean_text(child.text)
                transliteration = child.get("xlit", "")
                pronunciation = child.get("pron", "")
                part_of_speech = child.get("pos", "")

            elif tag == "meaning":
                definition = extract_full_text(child)

            elif tag == "source":
                source = extract_full_text(child)

            elif tag == "usage":
                usage = extract_full_text(child)

        entries.append({
            "number": number,
            "word": hebrew_word,
            "transliteration": transliteration,
            "pronunciation": pronunciation,
            "part_of_speech": part_of_speech,
            "definition": definition,
            "source": source,
            "usage": usage
        })

    print("Writing Hebrew JSON...")
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

    print("Done.")
    print(f"Total Hebrew entries converted: {len(entries)}")

if __name__ == "__main__":
    main()

python convert_hebrew_xml.py

convert_hebrew_xml.py
