from pathlib import Path

from organizer.file_mover import FileMover


def create_tmp_files(tmp_path) -> list[str]:
    text_file = tmp_path / "notes.txt"
    text_file.write_text("Important text content", encoding="utf-8")
    
    return [path.name for path in tmp_path.iterdir()]

def test_file_moving(tmp_path):
    assert tmp_path.is_dir()
    assert not (tmp_path / "Documents").is_dir()
    
    files = {
        "Documents": create_tmp_files(tmp_path),
    }
    
    mover = FileMover(files, tmp_path)
    mover.move()

    docs_dir = tmp_path / "Documents"
    text_file = docs_dir / "notes.txt"

    assert docs_dir.is_dir()
    assert text_file.is_file()