import os
from gendiff import generate_diff

def get_fixture_path(file_name):
    return os.path.join('tests', 'test_data', file_name)

def test_flat_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    with open(get_fixture_path('expected_result.txt')) as f:
        expected = f.read().strip()
    
    assert generate_diff(file1, file2) == expected