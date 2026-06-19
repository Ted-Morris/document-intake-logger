import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
READ_DOCUMENT_SCRIPT = "src/read_document.py"
EMPTY_DOCUMENT_PATH = PROJECT_ROOT / "data" / "empty_document.txt"


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


result = subprocess.run(
    [
        sys.executable,
        READ_DOCUMENT_SCRIPT,
        "data/empty_document.txt",
    ],
    cwd=PROJECT_ROOT,
    capture_output=True,
    text=True,
)


expected_output_lines = [
"Document Intake Summary",
"-----------------------",
"File name: empty_document.txt",
"Line count: 0",
"Word count: 0",
"Character count: 0",
]


actual_output_lines = result.stdout.strip().splitlines()


if result.returncode != 0:
    fail(f"Expected exit code 0, got {result.returncode}")


if actual_output_lines != expected_output_lines:
    fail(
        "Empty-file output did not match expected output.\n"
        f"Expected: {expected_output_lines}\n"
        f"Actual: {actual_output_lines}"
    )



print("PASS: empty-file behavior (empty input accepted, exit 0) is correct.")
