import pytest
import os
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join('tests/fixtures', filename)


def read_file(filepath):
    with open(filepath) as f:
        return f.read().strip()


@pytest.mark.parametrize("file1, file2, expected", [
    ('file1.json', 'file2.json', 'expected_plain.txt'),
    ('file1.yml', 'file2.yml', 'expected_plain.txt'),
])
def test_plain_format(file1, file2, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)
    
    expected_result = read_file(expected_path)
    actual_result = generate_diff(file1_path, file2_path, 'plain')
    
    assert actual_result == expected_result


def test_plain_identical_files():
    file_path = get_fixture_path('file1.json')
    result = generate_diff(file_path, file_path, 'plain')
    assert result == "Files are identical"


def test_plain_empty_files():
    file_path = get_fixture_path('empty.json')
    result = generate_diff(file_path, file_path, 'plain')
    assert result == "Files are identical"