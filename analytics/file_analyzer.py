from pathlib import Path


class FileAnalyzer:
    def __init__(self, files: dict[str, list], directory: Path):
        self.__files = files
        self.__directory = directory

    def count_files(self) -> dict[str, int | str]:
        file_stats = {
            "Total": 0,
            "Archives": 0,
            "Audios": 0,
            "Documents": 0,
            "Images": 0,
            "Others": 0,
            "Videos": 0,
        }
        total_storage = 0

        for category, files in self.__files.items():
            count = len(files)
            file_stats["Total"] += count
            file_stats[category] = file_stats.get(category, 0) + count
            for file in files:
                path = self.__directory / file
                if path.is_file():
                    total_storage += path.stat().st_size

        file_stats["Total storage"] = self.__format_size(total_storage)
        return file_stats

    @staticmethod
    def __format_size(size_bytes: int) -> str:
        size = float(size_bytes)
        for unit in ("B", "KB", "MB", "GB", "TB"):
            if size < 1024 or unit == "TB":
                return f"{size:.1f} {unit}"
            size /= 1024