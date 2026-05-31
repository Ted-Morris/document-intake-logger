from pathlib import Path
file_path = Path("data") / "sample_document.txt"
text = file_path.read_text(encoding="utf-8")
line_count = len(text.splitlines())
word_count = len(text.split())
character_count = len(text)
print("Document Intake Summary")
print("-----------------------")
print(f"File name: {file_path.name}")
print(f"Line count: {line_count}")
print(f"Word count: {word_count}")
print(f"Character count: {character_count}")
