from pathlib import Path
import hashlib


class FileDuplicateFinder:
    def __init__(self, files: dict[str, list], directory: Path):
        self.__files = files
        self.__directory = directory
        
    def check(self) -> tuple:
        hashed_files = {}
        
        for values in self.__files.values():
            for file in values:
                file_path = self.__directory / Path(file)

                if not file_path.is_file():
                    continue

                file_hash = hashlib.md5(file_path.read_bytes()).hexdigest()
                hashed_files.setdefault(file_hash, []).append(file)

        duplicates = {
            file_hash: files
            for file_hash, files in hashed_files.items()
            if len(files) >= 2
        }

        return (
            sum(len(files) for files in duplicates.values()),
            duplicates.values()
        )


if __name__ == "__main__":
    directory = Path("test_directory")

    files = {
        "Documents": [path.name for path in directory.glob("*")],
    }

    finder = FileDuplicateFinder(files, directory)
    result = finder.check()
    print(result)