from gendiff.cli import parser
from gendiff.parser import parse_file


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = {}
    # Все уникальные ключи из обоих файлов
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in all_keys:
        if key not in data1:
            diff[f"+ {key}"] = data2[key]
        elif key not in data2:
            diff[f"- {key}"] = data1[key]
        elif data1[key] == data2[key]:
            diff[f"  {key}"] = data1[key]
        else:
            diff[f"- {key}"] = data1[key]
            diff[f"+ {key}"] = data2[key]
    return diff


def format_diff(diff_dict):
    lines = ["{"]
    for key, value in diff_dict.items():
        # Преобразуем булевы значения в lowercase (true/false)
        if isinstance(value, bool):
            value = str(value).lower()
        lines.append(f"  {key}: {value}")
    lines.append("}")
    return "\n".join(lines)


def main():
    args = parser()
    diff = generate_diff(args.first_file, args.second_file)
    print(format_diff(diff))


if __name__ == "__main__":
    main()
