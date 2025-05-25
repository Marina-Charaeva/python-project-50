def parse_files(file1_data, file2_data):
    keys = set(file1_data) | set(file2_data)
    differences = {}

    for key in keys:
        if key in file1_data and key in file2_data:
            if file1_data[key] != file2_data[key]:
                differences[key] = {'status': 'changed', 'old_value': file1_data[key], 'new_value': file2_data[key]}
        elif key in file1_data:
            differences[key] = {'status': 'removed', 'old_value': file1_data[key]}
        else:
            differences[key] = {'status': 'added', 'new_value': file2_data[key]}

    return difference