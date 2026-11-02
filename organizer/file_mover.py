from pathlib import Path


class FileMover:
    def __init__(self, files: dict[str, list], directory: Path):
        self.__files = files
        self.__directory = directory

    def move(self) -> bool:
        files_moved = False

        for category, files in self.__files.items():
            if files:
                files_moved = True

                new_folder = self.__directory / category
                new_folder.mkdir(exist_ok=True)

                for file in files:
                    src = self.__directory / file
                    dest = new_folder / file
                    src.rename(dest)

        return files_moved


if __name__ == "__main__":
    directory = Path("test_directory")

    files = {
        "Documents": [path.name for path in directory.glob("*.pdf")],
        "Images": [path.name for path in directory.glob("*.jpg")],
    }

    mover = FileMover(files, directory)
    mover.move()