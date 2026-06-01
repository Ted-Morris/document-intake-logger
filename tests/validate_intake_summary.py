import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = PROJECT_ROOT / "outputs" / "intake_summary.json"



EXPECTED_SUMMARY = {
    "file_name": "sample_document.txt",
    "line_count": 4,
    "word_count": 35,
    "character_count": 197,
}


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


if not SUMMARY_PATH.exists():
    fail(f"Missing summary file: {SUMMARY_PATH}")


with SUMMARY_PATH.open("r", encoding="utf-8") as file:
    actual_summary = json.load(file)


for field_name in EXPECTED_SUMMARY:
    if field_name not in actual_summary:
        fail(f"Missing expected field: {field_name}")


for field_name, expected_value in EXPECTED_SUMMARY.items():
    actual_value = actual_summary[field_name]

    if actual_value != expected_value:
        fail(
            f"Wrong value for {field_name}: "
            f"expected {expected_value}, got {actual_value}"
        )


print("PASS: intake_summary.json has the expected fields and values.")
