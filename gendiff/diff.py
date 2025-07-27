from gendiff.diff_builder import build_diff
from gendiff.formatters import format_diff
from gendiff.parsers import parse_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1) or {}
    data2 = parse_file(file_path2) or {}
    if data1 == data2:
        if format_name == 'plain':
            return "Files are identical"
        elif format_name == 'stylish' and data1 != {}:
            return '{\n}'
        return '{}'
    diff = build_diff(data1, data2)
    return format_diff(diff, format_name)
