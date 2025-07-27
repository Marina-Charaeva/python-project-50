def format_stylish(diff, indent=0):
    if not diff:
        return '{}' if indent == 0 else ''
    lines = []
    current_indent = ' ' * indent
    for key, node in sorted(diff.items()):
        if node['type'] == 'nested':
            lines.append(f"{current_indent}    {key}: {{")
            lines.append(format_stylish(node['children'], indent + 4))
            lines.append(f"{current_indent}    }}")
        elif node['type'] == 'added':
            lines.append(f"{current_indent}  + {key}: {format_value(node['value'], indent + 4)}")
        elif node['type'] == 'removed':
            lines.append(f"{current_indent}  - {key}: {format_value(node['value'], indent + 4)}")
        elif node['type'] == 'unchanged':
            lines.append(f"{current_indent}    {key}: {format_value(node['value'], indent + 4)}")
        elif node['type'] == 'changed':
            lines.append(f"{current_indent}  - {key}: {format_value(node['old_value'], indent + 4)}")
            lines.append(f"{current_indent}  + {key}: {format_value(node['new_value'], indent + 4)}")
    if indent == 0:
        return '{\n' + '\n'.join(lines) + '\n}'
    return '\n'.join(lines)


def format_value(value, indent):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{' ' * (indent + 4)}{k}: {format_value(v, indent + 4)}")
        lines.append(f"{' ' * indent}}}")
        return '\n'.join(lines)
    return str(value)
