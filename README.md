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

After validating the directory, choose whether category folder names start with a capital letter. The default (`Y`) uses names such as `Documents`; enter `n` to use lowercase names such as `documents`. Then choose the folder-name language: `EN` (the default) or `DE`.

### CLI input and output

`main.py` prompts for these inputs in order:

1. **Directory path** — enter the directory to scan. It must exist and be a directory; otherwise, the CLI prints an `[ERROR]` message and stops.
2. **Folder-name capitalization** — enter `n` for lowercase names. Any other input, including an empty response, uses names with an initial capital.
3. **Folder-name language** — enter `DE` for German category folder names (`Archive`, `Audios`, `Dokumente`, `Bilder`, `Andere`, `Videos`). Any other input, including an empty response, uses English names. This choice changes category and folder names; the other CLI messages remain in English.
4. **Move confirmation** — enter `y` to move files, or any other input to cancel. The default is cancellation.

Before the move confirmation, the CLI prints the files grouped by category, a file analysis (total files, counts per category, and total storage), and the duplicate-file results. Duplicate files are listed for review; they are not deleted. On confirmation, it prints a start message followed by a success message if files were moved. If there are no files to move, it prints a warning instead. On cancellation, it reports that no files were moved.

### Example terminal session

The following example uses sample files and sizes. Your results will depend on the files in the selected directory. The text after each prompt is the user's input:

```text
============================================================
                    SMART FILE ORGANIZER
      Preview mode — files move only after confirmation
============================================================
Please enter a directory path: C:\Users\Alex\Downloads\to-organize
[SUCCESS] Directory validated: C:\Users\Alex\Downloads\to-organize
[INFO] Should folder names be uppercase? [Y/n]: y
[INFO] Folder names in English or German? [EN/de]: en
[CATEGORY] Archives
  - backup.zip
------------------------------------------------------------
[CATEGORY] Audios
  - song.mp3
------------------------------------------------------------
[CATEGORY] Documents
  - budget.xlsx
  - notes.txt
  - notes-copy.txt
------------------------------------------------------------
[CATEGORY] Images
  - photo.jpg
------------------------------------------------------------
[CATEGORY] Others
  - installer.exe
------------------------------------------------------------
[CATEGORY] Videos
  - clip.mp4
------------------------------------------------------------
FILE ANALYSIS
------------------------------------------------------------
Total files: 8
Archives: 1
Audios: 1
Documents: 3
Images: 1
Others: 1
Videos: 1
Total storage: 28.4 MB
------------------------------------------------------------
DUPLICATE DETECTION
------------------------------------------------------------
[INFO] Duplicate files found: 2
  - notes.txt
  - notes-copy.txt
[INFO] Move the listed files now? [y/N]: y
[INFO] Starting file organization...
[SUCCESS] File organization completed.
```

Enter `y` to move the files into category subfolders. Any other input cancels the operation and leaves the files in place:

```text
[INFO] Move the listed files now? [y/N]: n
[INFO] Operation cancelled. No files were moved.
```

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
