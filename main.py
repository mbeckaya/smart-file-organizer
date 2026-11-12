from pathlib import Path

from analytics.file_analyzer import FileAnalyzer
from analytics.file_duplicate_finder import FileDuplicateFinder
from organizer.file_categorizer import FileCategorizer
from organizer.file_mover import FileMover


def main() -> bool:
    print("=" * 60)
    print("SMART FILE ORGANIZER".center(60))
    print("Preview mode — files move only after confirmation".center(60))
    print("=" * 60)

    user_path = input("Please enter a directory path: ").strip()

    current_path = Path(user_path)

    is_path_valid = current_path.exists() and current_path.is_dir()

    if not is_path_valid:
        print(f"[ERROR] The selected path '{current_path}' does not exist or is not a directory.")
        return False

    print(f"[SUCCESS] Directory validated: {current_path}")

    user_dir_format_action = input(
        "[INFO] Should folder names be uppercase? [Y/n]: "
    ).strip().lower()

    is_uppercase = user_dir_format_action != "n"

    user_dir_language_action = input(
        "[INFO] Folder names in English or German? [EN/de]: "
    ).strip().upper()

    language = "DE" if user_dir_language_action == "DE" else "EN"
    
    categorizer = FileCategorizer(
        is_uppercase=is_uppercase,
        language=language,
    )
    files_with_cats = categorizer.add(current_path.iterdir())

    for cat, cat_files in files_with_cats.items():
        if cat_files:
            print(f"[CATEGORY] {cat}")
            for file in cat_files:
                print(f"  - {file}")
            print("-" * 60)

    file_stats = FileAnalyzer(files_with_cats, current_path).count_files()

    print("FILE ANALYSIS")
    print("-" * 60)

    for label, value in file_stats.items():
        if label == "Total":
            label = "Total files"
        elif label == "Total storage":
            print(f"{label}: {value}")
            continue
        print(f"{label}: {value}")

    print("-" * 60)
    print("DUPLICATE DETECTION")
    print("-" * 60)

    duplicate_finder = FileDuplicateFinder(files_with_cats, current_path)
    duplicates_total, duplicates = duplicate_finder.check()

    print(f"[INFO] Duplicate files found: {duplicates_total}")

    for files in duplicates:
        for file in files:
            print(f"  - {file}")

    user_continue_action = input(
        "[INFO] Move the listed files now? [y/N]: "
    ).strip().lower()

    if user_continue_action != "y":
        print("[INFO] Operation cancelled. No files were moved.")
        return False

    print("[INFO] Starting file organization...")

    mover = FileMover(files_with_cats, current_path)
    files_moved = mover.move()

    if not files_moved:
        print("[WARNING] No files were moved.")
        return False
    
    print("[SUCCESS] File organization completed.")
    return True

    
if __name__ == '__main__':
    main()