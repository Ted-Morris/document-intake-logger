import json
from pathlib import Path


script_path = Path(__file__).resolve()
project_root = script_path.parent.parent
file_path = project_root / "data" / "sample_document.txt"

if not file_path.exists():
    print("Document Intake Summary")
    print("-----------------------")
    print(f"Error: Could not find file: {file_path}")
    raise SystemExit(1)

text = file_path.read_text(encoding="utf-8")

line_count = len(text.splitlines())
word_count = len(text.split())
character_count = len(text)

summary = {
    "file_name": file_path.name,
    "line_count": line_count,
    "word_count": word_count,
    "character_count": character_count
}

output_path = project_root / "outputs" / "intake_summary.json"

output_path.write_text(
    json.dumps(summary, indent=2),
    encoding="utf-8",
)

print("Document Intake Summary")
print("-----------------------")
print(f"File name: {file_path.name}")
print(f"Line count: {line_count}")
print(f"Word count: {word_count}")
print(f"Character count: {character_count}")
