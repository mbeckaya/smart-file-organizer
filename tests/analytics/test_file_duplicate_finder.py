from analytics.file_duplicate_finder import FileDuplicateFinder


def create_tmp_files(tmp_path) -> dict[str, list[str]]:
    (tmp_path / "first.txt").write_text("same content", encoding="utf-8")
    (tmp_path / "duplicate.txt").write_text("same content", encoding="utf-8")
    (tmp_path / "unique.txt").write_text("different content", encoding="utf-8")

    return {
        "Documents": ["first.txt", "duplicate.txt", "unique.txt", "missing.txt"],
    }


def test_file_duplicate_finder_returns_duplicate_files(tmp_path):
    files = create_tmp_files(tmp_path)

    finder = FileDuplicateFinder(files, tmp_path)
    duplicate_count, duplicates = finder.check()

    assert duplicate_count == 2
    assert list(duplicates) == [["first.txt", "duplicate.txt"]]


def test_file_duplicate_finder_returns_empty_result_without_duplicates(tmp_path):
    (tmp_path / "first.txt").write_text("first", encoding="utf-8")
    (tmp_path / "second.txt").write_text("second", encoding="utf-8")
    files = {"Documents": ["first.txt", "second.txt"]}

    finder = FileDuplicateFinder(files, tmp_path)
    duplicate_count, duplicates = finder.check()

    assert duplicate_count == 0
    assert list(duplicates) == []
