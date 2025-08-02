import os
import pytest
from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().rstrip()


@pytest.mark.parametrize("file1, file2, expected", [
    ('file1.json', 'file2.json', 'expected_stylish.txt'),
    ('file1.yml', 'file2.yml', 'expected_stylish.txt'),
    (
        'file1.json',
        'file2.yml',
        'expected_stylish.txt'),  # тест на смешанные типы
])
def test_stylish_format(file1, file2, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)
    
    expected_result = read_file(expected_path)
    actual_result = generate_diff(file1_path, file2_path)
    
    assert actual_result == expected_result


@pytest.mark.parametrize("file1, file2, format_name, expected", [
    ('file1.json', 'file2.json', 'stylish', 'expected_stylish.txt'),
    ('file1.json', 'file2.json', 'plain', 'expected_plain.txt'),
    ('file1.json', 'file2.json', 'json', 'expected_json.txt'),
])
def test_all_formatters(file1, file2, format_name, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)
    
    expected_result = read_file(expected_path)
    actual_result = generate_diff(file1_path, file2_path, format_name)
    
    if actual_result != expected_result:
        print(f"Format: {format_name}")
        print("Expected:\n", repr(expected_result))
        print("Actual:\n", repr(actual_result))
    assert actual_result == expected_result