from collections.abc import Iterable
from pathlib import Path


class FileCategorizer:
    def __init__(
            self, 
            is_uppercase=True,
            language="EN",
        ):
        self.__is_uppercase = is_uppercase
        self.__dir_names = (
            "archives",
            "audios",
            "documents",
            "images",
            "others",
            "videos",
        )

        if language.upper() == "DE":
            self.__dir_names = (
                "archive",
                "audios",
                "dokumente",
                "bilder",
                "andere",
                "videos",
            )
        
        self.__file_dirs = {
            name: [] 
            for name in self.__dir_names
        }

    def add(self, files: Iterable[Path]) -> dict[str, list[str]]:
        if self.__is_uppercase:
            self.__file_dirs = {
                key.capitalize(): value
                for key, value in self.__file_dirs.items()
            }

        for file in files:
            if not file.is_file():
                continue

            category = self.get_category(file)
            self.__file_dirs[category].append(file.name)

        return self.__file_dirs

    def get_category(self, file: Path) -> str:
        file_ext = file.suffix.lower().replace(".", "")

        if file_ext in (
            "7z", "bz2", "gz", "iso", "rar", "tar", "tgz", "xz", "zip"
        ):
            file_cat = self.__dir_names[0].capitalize() if self.__is_uppercase else self.__dir_names[0]
        elif file_ext in (
            "aac", "flac", "m4a", "mp3", "ogg", "opus", "wav", "wma"
        ):
            file_cat = self.__dir_names[1].capitalize() if self.__is_uppercase else self.__dir_names[1]
        elif file_ext in (
            "csv", "doc", "docx", "eml", "epub", "key", "md",
            "mobi", "msg", "numbers", "odp", "ods", "odt",
            "pages", "pdf", "ppt", "pptx", "rtf", "tsv",
            "txt", "xls", "xlsx"
        ):
            file_cat = self.__dir_names[2].capitalize() if self.__is_uppercase else self.__dir_names[2]
        elif file_ext in (
            "avif", "bmp", "gif", "heic", "ico", "jpeg", "jpg",
            "png", "psd", "svg", "tiff", "webp"
        ):
            file_cat = self.__dir_names[3].capitalize() if self.__is_uppercase else self.__dir_names[3]
        elif file_ext in (
            "avi", "flv", "m4v", "mkv", "mov", "mp4", "webm", "wmv"
        ):
            file_cat = self.__dir_names[5].capitalize() if self.__is_uppercase else self.__dir_names[5]
        else:
            file_cat = self.__dir_names[4].capitalize() if self.__is_uppercase else self.__dir_names[4]

        return file_cat