# Document Intake Logger v0.1

Document Intake Logger is a beginner AI engineering learning project. It reads a text document, creates a simple intake summary, and saves that summary as JSON.

This project is part of my beginner AI engineering track. The current version is `v0.1`.

## What the project does

Document Intake Logger reads a `.txt` file and reports:

* File name
* Line count
* Word count
* Character count

It also writes the intake summary to a JSON file so the output can be validated and reused by other scripts.

## Project structure

```text
document-intake-logger/
|-- data/
|   |-- sample_document.txt
|   `-- another_document.txt
|-- output/
|   `-- intake_summary.json
|-- src/
|   `-- read_document.py
|-- tests/
|   |-- run_all_validations.py
|   |-- validate_another_document_summary.py
|   |-- validate_document_path_selection.py
|   `-- validate_intake_summary.py
|-- .gitignore
`-- README.md
```

## How to use the virtual environment

The project uses a local Python virtual environment named `.venv`.

Activate it from the project folder:

```powershell
.\.venv\Scripts\Activate.ps1
```

When it is active, the PowerShell prompt begins with:

```text
(.venv)
```

The `.venv` folder is local only. It is ignored by Git and should not be committed to the repository.

## How to run the project

Run the default sample document:

```powershell
python .\src\read_document.py
```

Run the alternate sample document:

```powershell
python .\src\read_document.py .\data\another_document.txt
```

The script prints the document summary in the terminal and writes the JSON summary to:

```text
output/intake_summary.json
```

## How to run all validations

Run the full validation runner:

```powershell
python .\tests\run_all_validations.py
```

This runs the project checks in sequence and confirms that the generated summaries match the expected results.

If the `vrun` shortcut is available in PowerShell, the same validation runner can be started with:

```powershell
vrun
```

## Current status

Status: Learning project
Track: Beginner AI engineering
Version: v0.1
Repository branch: `main`

This project currently focuses on basic Python scripting, file input, JSON output, validation scripts, virtual environment usage, Git, and GitHub portfolio setup.
