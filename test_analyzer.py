import pytest
from analyzer import analyze_text


def test_analyze_text(tmp_path):
    d = tmp_path/"sub"
    d.mkdir()
    file_path = d/"test.sample.txt"
    file_path.write_text("Тест. Тест! Слово.", encoding="utf-8")

    count, freq = analyze_text(str(file_path))

    assert count == 3
    assert freq.get("тест") == 2
    assert freq.get("слово") == 1


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        analyze_text("non_existent_file.txt")


def test_empty_file(tmp_path):
    file_path = tmp_path/"empty.txt"
    file_path.write_text(" \n ", encoding="utf")

    with pytest.raises(ValueError):
        analyze_text(str(file_path))