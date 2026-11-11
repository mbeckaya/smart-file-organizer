from pathlib import Path

from organizer.file_categorizer import FileCategorizer


def create_tmp_files(tmp_path) -> list[Path]:
    text_file = tmp_path / "notes.txt"
    text_file.write_text("Important text content", encoding="utf-8")
    
    jpg_file = tmp_path / "image.jpg"
    jpg_file.write_bytes(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")
    
    pdf_file = tmp_path / "document.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 Minimal PDF content")

    return list(tmp_path.iterdir())

def test_file_categorization_uppercase(tmp_path):
    categorizer = FileCategorizer()
    result = categorizer.add(create_tmp_files(tmp_path))
    
    assert len(result["Archives"]) == 0
    assert len(result["Audios"]) == 0
    assert "notes.txt" in result["Documents"]
    assert "document.pdf" in result["Documents"]
    assert "image.jpg" in result["Images"]
    assert len(result["Others"]) == 0

def test_file_categorization_lowercase(tmp_path):
    categorizer = FileCategorizer(False)
    result = categorizer.add(create_tmp_files(tmp_path))
    
    assert len(result["archives"]) == 0
    assert len(result["audios"]) == 0
    assert "notes.txt" in result["documents"]
    assert "document.pdf" in result["documents"]
    assert "image.jpg" in result["images"]
    assert len(result["others"]) == 0