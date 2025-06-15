def format_stylish(diff):
    def walk(node, depth):
        lines = []
        indent = '    ' * depth
        for key in sorted(node.keys()):
            meta = node[key]
            nested = meta['type'] == 'nested'
            changed = meta['type'] == 'changed'
            if nested:
                lines.append(f"{indent}    {key}: {{")
                lines.append(walk(meta['children'], depth + 1))
                lines.append(f"{indent}    }}")
            elif changed:
                old = format_value(meta['old_value'])
                new = format_value(meta['new_value'])
                lines.append(f"{indent}  - {key}: {old}")
                lines.append(f"{indent}  + {key}: {new}")
            else:
                prefix = get_prefix(meta['type'])
                val = format_value(meta['value'])
                lines.append(f"{indent}  {prefix} {key}: {val}")
        return '\n'.join(lines)

    def format_value(value):
        if isinstance(value, dict):
            return '[complex value]'
        elif value is None:
            return 'null'
        elif isinstance(value, bool):
            return str(value).lower()
        return str(value)

    def get_prefix(type_):
        return {'added': '+', 'removed': '-', 'unchanged': ' '}.get(type_, ' ')
    return '{\n' + walk(diff, 0) + '\n}'
