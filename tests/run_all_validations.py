import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_command(command):
    print()
    print(f"Running: {' '.join(command)}")
    subprocess.run(command, cwd=PROJECT_ROOT, check=True)


run_command([sys.executable, "src/read_document.py", "data/another_document.txt"])
run_command([sys.executable, "tests/validate_another_document_summary.py"])

run_command([sys.executable, "src/read_document.py"])
run_command([sys.executable, "tests/validate_intake_summary.py"])

run_command([sys.executable, "tests/validate_document_path_selection.py"])

print()
print("PASS: all validations completed successfully.")
