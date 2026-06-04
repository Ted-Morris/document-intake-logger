import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
READ_DOCUMENT_SCRIPT = "src/read_document.py"


def run_step(step_name, command):
    print()
    print(f"Step: {step_name}")
    print(f"Running: {' '.join(command)}")
    subprocess.run(command, cwd=PROJECT_ROOT, check=True)


# Each validation step has a display name and the command the runner executes.
validation_steps = [
    (
        "Generate alternate document summary",
        [sys.executable, READ_DOCUMENT_SCRIPT, "data/another_document.txt"],
    ),
    (
        "Validate alternate document summary",
        [sys.executable, "tests/validate_another_document_summary.py"],
    ),
    (
        "Restore default sample document summary",
        [sys.executable, READ_DOCUMENT_SCRIPT],
    ),
    (
        "Validate default sample document summary",
        [sys.executable, "tests/validate_intake_summary.py"],
    ),
    (
        "Validate document path selection",
        [sys.executable, "tests/validate_document_path_selection.py"],
    ),
]


for step_name, command in validation_steps:
    run_step(step_name, command)

print()
print(f"PASS: {len(validation_steps)} validation steps completed successfully.")
