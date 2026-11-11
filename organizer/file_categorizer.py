from collections.abc import Iterable
from pathlib import Path


class FileCategorizer:
    def __init__(self, is_uppercase=True):
        self.__is_uppercase = is_uppercase

    def add(self, files: Iterable[Path]) -> dict[str, list[str]]:
        files_with_cats = {
            "Archives": [],
            "Audios": [],
            "Documents": [],
            "Images": [],
            "Others": [],
            "Videos": [],
        }

        files_with_cats = {
            key.capitalize() if self.__is_uppercase else key.lower(): value
            for key, value in files_with_cats.items()
        }

        for file in files:
            if not file.is_file():
                continue

            category = self.get_category(file)
            files_with_cats[category].append(file.name)

        return files_with_cats

    def get_category(self, file: Path) -> str:
        file_ext = file.suffix.lower().replace(".", "")

        if file_ext in (
            "7z", "bz2", "gz", "iso", "rar", "tar", "tgz", "xz", "zip"
        ):
            file_cat = "archives".capitalize() if self.__is_uppercase else "archives"
        elif file_ext in (
            "aac", "flac", "m4a", "mp3", "ogg", "opus", "wav", "wma"
        ):
            file_cat = "audios".capitalize() if self.__is_uppercase else "audios"
        elif file_ext in (
            "csv", "doc", "docx", "eml", "epub", "key", "md",
            "mobi", "msg", "numbers", "odp", "ods", "odt",
            "pages", "pdf", "ppt", "pptx", "rtf", "tsv",
            "txt", "xls", "xlsx"
        ):
            file_cat = "documents".capitalize() if self.__is_uppercase else "documents"
        elif file_ext in (
            "avif", "bmp", "gif", "heic", "ico", "jpeg", "jpg",
            "png", "psd", "svg", "tiff", "webp"
        ):
            file_cat = "images".capitalize() if self.__is_uppercase else "images"
        elif file_ext in (
            "avi", "flv", "m4v", "mkv", "mov", "mp4", "webm", "wmv"
        ):
            file_cat = "videos".capitalize() if self.__is_uppercase else "videos"
        else:
            file_cat = "others".capitalize() if self.__is_uppercase else "others"

        return file_cat