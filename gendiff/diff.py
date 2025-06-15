def generate_diff(file_path1, file_path2, format_name='stylish'):
    from gendiff.formatters import get_formatter
    from gendiff.parser import parse_file

    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)
    formatter = get_formatter(format_name)
    return formatter(diff)
    pass


def build_diff(data1, data2):
    diff = {}
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in all_keys:
        if key not in data1:
            diff[key] = {'type': 'added', 'value': data2[key]}
        elif key not in data2:
            diff[key] = {'type': 'removed', 'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'type': 'nested',
                'children': build_diff(data1[key], data2[key])
            }
        elif data1[key] == data2[key]:
            diff[key] = {'type': 'unchanged', 'value': data1[key]}
        else:
            diff[key] = {
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
    return diff
