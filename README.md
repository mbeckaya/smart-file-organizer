# Smart File Organizer

Smart File Organizer is a command-line application for reviewing and organizing files in a directory. It categorizes files by extension, reports file counts and storage usage, identifies files with identical content, and moves files into category folders only after user confirmation.

## Features

- Categorizes files into **Archives**, **Audios**, **Documents**, **Images**, **Videos**, and **Others**
- Shows a preview of the files found before making changes
- Reports the total file count, storage usage, and count per category
- Detects files with identical content and lists them for review; duplicates are not deleted
- Moves the listed files into category subfolders after the user confirms
- Includes pytest unit tests for categorization, moving, analytics, and duplicate detection

The application scans files directly inside the selected directory; it does not scan subdirectories recursively. To proceed with moving files, enter `y` at the confirmation prompt. Any other input cancels the operation.

## Requirements

- Python 3.10 or newer
- pip

Install the dependencies from the project directory:

```bash
pip install -r requirements.txt
```

## Run the application

From the project directory, start the interactive organizer with:

```bash
python main.py
```

Enter the path to the directory you want to organize. The application displays its file preview, analysis, and duplicate results before asking whether to move the files.

## Run the tests

The project includes pytest unit tests. Run the full test suite from the project directory with:

```bash
python -m pytest
```

## Project structure

```text
analytics/
    file_analyzer.py
    file_duplicate_finder.py
organizer/
    file_categorizer.py
    file_mover.py
tests/
main.py
```

## Technologies

Python, pathlib, hashlib, and pytest
