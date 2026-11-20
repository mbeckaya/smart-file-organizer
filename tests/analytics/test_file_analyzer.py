from analytics.file_analyzer import FileAnalyzer


def create_tmp_files(tmp_path) -> dict[str, list[str]]:
    (tmp_path / "document.pdf").write_bytes(b"r" * 1024)
    (tmp_path / "image.jpg").write_bytes(b"i" * 512)

    return {
        "Documents": ["document.pdf", "missing.pdf"],
        "Images": ["image.jpg"],
    }


def test_file_analysis_counts_files_and_storage(tmp_path):
    files = create_tmp_files(tmp_path)

    analyzer = FileAnalyzer(files, tmp_path)
    result = analyzer.count_files()

    assert result == {
        "Total": 3,
        "Archives": 0,
        "Audios": 0,
        "Documents": 2,
        "Images": 1,
        "Others": 0,
        "Videos": 0,
        "Total storage": "1.5 KB",
    }
