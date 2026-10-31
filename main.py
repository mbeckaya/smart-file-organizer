from pathlib import Path

from organizer.file_categorizer import FileCategorizer

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
            for docs in cat_files:
                print(f"  - {docs}")
            print("-" * 60)

    return True

if __name__ == '__main__':
    main()