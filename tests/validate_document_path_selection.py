import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_PATH))

from read_document import get_document_path


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


def check_document_path(args, expected_relative_path):
    actual_path = get_document_path(PROJECT_ROOT, args)
    expected_path = PROJECT_ROOT / expected_relative_path

    if actual_path != expected_path:
        fail(
            f"Wrong path for args {args}: "
            f"expected {expected_path}, got {actual_path}"
        )


check_document_path(
    ["src/read_document.py"],
    Path("data") / "sample_document.txt",
)

check_document_path(
    ["src/read_document.py", "data/another_document.txt"],
    Path("data") / "another_document.txt",
)


print("PASS: document path selection works as expected.")
