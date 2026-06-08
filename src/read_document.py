import json
import sys
from pathlib import Path


def count_lines(text):
    return len(text.splitlines())


def count_words(text):
    return len(text.split())


def count_characters(text):
    return len(text)


def build_summary(file_name, text):
    return {
        "file_name": file_name,
        "line_count": count_lines(text),
        "word_count": count_words(text),
        "character_count": count_characters(text),
    }


def write_summary_json(output_path, summary):
    output_path.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )


def print_summary_header():
    print("Document Intake Summary")
    print("-----------------------")


def print_summary(summary):
    print_summary_header()
    print(f"File name: {summary['file_name']}")
    print(f"Line count: {summary['line_count']}")
    print(f"Word count: {summary['word_count']}")
    print(f"Character count: {summary['character_count']}")


def get_document_path(project_root, args):
    if len(args) > 1:
        return project_root / args[1]

    return project_root / "data" / "sample_document.txt"


def main():
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent

    file_path = get_document_path(project_root, sys.argv)

    if not file_path.exists():
        print_summary_header()
        print(f"Error: Could not find file: {file_path}")
        raise SystemExit(1)

    text = file_path.read_text(encoding="utf-8")

    summary = build_summary(file_path.name, text)

    output_path = project_root / "outputs" / "intake_summary.json"

    write_summary_json(output_path, summary)

    print_summary(summary)


if __name__ == "__main__":
    main()
