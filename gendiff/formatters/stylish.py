def format_value(value):  # Вынесено в отдельную функцию
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def walk(node, depth):  # Основная логика вынесена
    lines = []
    indent = '    ' * depth
    for key in sorted(node.keys()):
        meta = node[key]
        if meta['type'] == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(walk(meta['children'], depth + 1))
            lines.append(f"{indent}    }}")
        elif meta['type'] == 'changed':
            lines.append(f"{indent}  - {key}: {format_value(meta['old_value'])}")
            lines.append(f"{indent}  + {key}: {format_value(meta['new_value'])}")
        else:
            prefix = {'added': '+', 'removed': '-', 'unchanged': ' '}[meta['type']]
            lines.append(f"{indent}  {prefix} {key}: {format_value(meta['value'])}")
    return '\n'.join(lines)


def format_stylish(diff):  # Теперь сложность <7
    return '{\n' + walk(diff, 0) + '\n}'
