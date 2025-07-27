from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.yaml import format_yaml


def format_diff(diff, format_name='stylish'):
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    elif format_name == 'yaml':
        return format_yaml(diff)
    raise ValueError(f"Unknown format: {format_name}")


__all__ = ['format_diff']
