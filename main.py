from pathlib import Path

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

if __name__ == '__main__':
    main()