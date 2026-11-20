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
    categorizer = FileCategorizer(is_uppercase=False)
    result = categorizer.add(create_tmp_files(tmp_path))
    
    assert len(result["archives"]) == 0
    assert len(result["audios"]) == 0
    assert "notes.txt" in result["documents"]
    assert "document.pdf" in result["documents"]
    assert "image.jpg" in result["images"]
    assert len(result["others"]) == 0

def test_file_categorization_language_EN(tmp_path):
    categorizer = FileCategorizer(is_uppercase=False)
    result = categorizer.add(create_tmp_files(tmp_path))
    
    assert len(result["archives"]) == 0
    assert len(result["audios"]) == 0
    assert "notes.txt" in result["documents"]
    assert "document.pdf" in result["documents"]
    assert "image.jpg" in result["images"]
    assert len(result["others"]) == 0

def test_file_categorization_language_DE(tmp_path):
    categorizer = FileCategorizer(is_uppercase=False, language="DE")
    result = categorizer.add(create_tmp_files(tmp_path))
    
    assert len(result["archive"]) == 0
    assert len(result["audios"]) == 0
    assert "notes.txt" in result["dokumente"]
    assert "document.pdf" in result["dokumente"]
    assert "image.jpg" in result["bilder"]
    assert len(result["andere"]) == 0

def test_video_and_unknown_extensions_use_correct_categories(tmp_path):
    video_file = tmp_path / "clip.mp4"
    video_file.touch()
    unknown_file = tmp_path / "installer.exe"
    unknown_file.touch()

    english_result = FileCategorizer(is_uppercase=False).add(
        [video_file, unknown_file]
    )
    german_result = FileCategorizer(
        is_uppercase=False,
        language="DE",
    ).add([video_file, unknown_file])

    assert "clip.mp4" in english_result["videos"]
    assert "installer.exe" in english_result["others"]
    assert "clip.mp4" in german_result["videos"]
    assert "installer.exe" in german_result["andere"]