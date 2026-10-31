# Smart File Organizer

🚧 **Status: In Progress**

A lightweight Python tool that organizes files in a selected directory into category folders based on their file extensions. Files are listed for review before you confirm the move.

## Features

- Automatic file categorization
- File preview and confirmation before moving
- Categories for documents, images, archives, audio, videos, and other files
- Organized category subfolders inside the selected directory
- **Basic file analytics:** Displays the total number of files, storage usage, and file counts per category
- **Duplicate file detection:** Identifies files with identical content and displays them for review without automatically deleting anything

## Requirements

- Python 3.x

No additional libraries are required. The project uses Python's built-in modules.

## Usage

Start the program from the project directory:

```bash
python main.py
```

Enter the directory you want to organize. The program scans the directory and displays the files it found by category.

It also provides a basic file analysis showing the total number of files, storage usage, and the number of files in each category. Duplicate files with identical content can also be detected and displayed.

Nothing is moved until you confirm with `y`; pressing Enter or entering anything else cancels the operation.

## Example

```text
============================================================
                 SMART FILE ORGANIZER
     Preview mode — files move only after confirmation
============================================================

Please enter a directory path: C:\Users\Alex\Downloads

[SUCCESS] Directory validated: C:\Users\Alex\Downloads

[CATEGORY] documents
  - report.pdf

[CATEGORY] images
  - vacation.jpg

------------------------------------------------------------
FILE ANALYSIS
------------------------------------------------------------
Total files: 120
Documents: 35
Images: 50
Videos: 15
Other: 20

Total storage: 1.5 GB

------------------------------------------------------------
DUPLICATE DETECTION
------------------------------------------------------------
[INFO] Duplicate files found: 2

[INFO] Move the listed files now? [y/N]:
```

## Tech

**Python · File System Automation · pathlib · hashlib · Basic Data Analytics**