import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
READ_DOCUMENT_SCRIPT = "src/read_document.py"
MISSING_DOCUMENT_PATH = PROJECT_ROOT / "data" / "missing_document.txt"


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


result = subprocess.run(
    [
        sys.executable,
        READ_DOCUMENT_SCRIPT,
        "data/missing_document.txt",
    ],
    cwd=PROJECT_ROOT,
    capture_output=True,
    text=True,
)


expected_output_lines = [
    "Document Intake Summary",
    "-----------------------",
    f"Error: Could not find file: {MISSING_DOCUMENT_PATH}",
]


actual_output_lines = result.stdout.strip().splitlines()


if result.returncode != 1:
    fail(f"Expected exit code 1, got {result.returncode}")


if actual_output_lines != expected_output_lines:
    fail(
        "Missing-file output did not match expected output.\n"
        f"Expected: {expected_output_lines}\n"
        f"Actual: {actual_output_lines}"
    )


print("PASS: missing-file error message and exit code are correct.")
