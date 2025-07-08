import sys
import os
import pytest
from gendiff.diff import generate_diff
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read_file(file_path):
    with open(file_path) as f:
        return f.read().strip()


@pytest.mark.parametrize("file1, file2, expected", [
    ("file1.json", "file2.json", "expected.txt"),
])
def test_flat_json_diff(file1, file2, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)
    result = generate_diff(file1_path, file2_path)
    expected_result = read_file(expected_path)
    assert result == expected_result


def test_identical_files():
    file_path = get_fixture_path("file1.json")
    result = generate_diff(file_path, file_path)
    assert "  host: hexlet.io" in result
    assert "-" not in result and "+" not in result


def test_empty_files():
    empty_file = get_fixture_path("empty.json")
    result = generate_diff(empty_file, empty_file)
    assert result in ("{}", "{\n\n}")
