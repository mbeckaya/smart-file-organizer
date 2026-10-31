from pathlib import Path

from organizer.file_categorizer import FileCategorizer
from analytics.file_analyzer import FileAnalyzer


def main() -> bool:
    print("=" * 60)
    print("SMART FILE ORGANIZER".center(60))
    print("Preview mode — files move only after confirmation".center(60))
    print("=" * 60)

    user_path = input("Please enter a directory path: ")

    current_path = Path(user_path)

    is_path_valid = current_path.exists() and current_path.is_dir()

    if not is_path_valid:
        print(f"[ERROR] The selected path '{current_path}' does not exist or is not a directory.")
        return False

    print(f"[SUCCESS] Directory validated: {current_path}")

    categorizer = FileCategorizer()
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

    return True

if __name__ == '__main__':
    main()