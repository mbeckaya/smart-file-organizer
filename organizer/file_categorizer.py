from pathlib import Path

class FileCategorizer:
    def add(self, files: list[Path]) -> dict[str, list]:
        files_with_cats = {
            "Archives": [],
            "Audios": [],
            "Documents": [],
            "Images": [],
            "Others": [],
            "Videos": [],
        }

        for file in files:
            category = self.get_category(file)
            files_with_cats[category].append(file.name)

        return files_with_cats

    def get_category(self, file: Path) -> str:
        file_ext = file.suffix.lower().replace(".", "")

        if file_ext in (
            "7z", "bz2", "gz", "iso", "rar", "tar", "tgz", "xz", "zip"
        ):
            file_cat = "Archives"
        elif file_ext in (
            "aac", "flac", "m4a", "mp3", "ogg", "opus", "wav", "wma"
        ):
            file_cat = "Audios"
        elif file_ext in (
            "csv", "doc", "docx", "eml", "epub", "key", "md",
            "mobi", "msg", "numbers", "odp", "ods", "odt",
            "pages", "pdf", "ppt", "pptx", "rtf", "tsv",
            "txt", "xls", "xlsx"
        ):
            file_cat = "Documents"
        elif file_ext in (
            "avif", "bmp", "gif", "heic", "ico", "jpeg", "jpg",
            "png", "psd", "svg", "tiff", "webp"
        ):
            file_cat = "Images"
        elif file_ext in (
            "avi", "flv", "m4v", "mkv", "mov", "mp4", "webm", "wmv"
        ):
            file_cat = "Videos"
        else:
            file_cat = "Others"

        return file_cat

if __name__ == "__main__":
    categorizer = FileCategorizer()

    files = Path("test_directory").iterdir()
    result = categorizer.add(files)

    print(result)