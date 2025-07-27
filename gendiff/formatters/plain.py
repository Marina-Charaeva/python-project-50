def format_plain(diff, parent_key=''):
    lines = []
    for key, node in sorted(diff.items()):
        current_key = f"{parent_key}.{key}" if parent_key else key
        value = format_value(node.get('value'))
        old_value = format_value(node.get('old_value'))
        new_value = format_value(node.get('new_value'))
        if node['type'] == 'nested':
            lines.append(format_plain(node['children'], current_key))
        elif node['type'] == 'added':
            lines.append(f"Property '{current_key}' was added with value: {value}")
        elif node['type'] == 'removed':
            lines.append(f"Property '{current_key}' was removed")
        elif node['type'] == 'changed':
            lines.append(
                f"Property '{current_key}' was updated. From {old_value} to {new_value}"
            )
    return '\n'.join(line for line in lines if line)


def format_value(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)
