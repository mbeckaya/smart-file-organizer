from organizer.file_organizer import FileOrganizer


def test_invalid_directory_returns_false(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "missing-directory")

    assert FileOrganizer().run() is False
    assert "[ERROR]" in capsys.readouterr().out


def test_cancel_leaves_files_in_place(tmp_path, monkeypatch, capsys):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("Important text content", encoding="utf-8")
    responses = iter([str(tmp_path), "", "", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    assert FileOrganizer().run() is False

    output = capsys.readouterr().out
    assert "[INFO] Operation cancelled. No files were moved." in output
    assert file_path.is_file()
    assert not (tmp_path / "Documents").exists()
