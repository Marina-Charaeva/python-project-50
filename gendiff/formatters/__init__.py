from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def get_formatter(format_name):
    if format_name == 'stylish':
        return format_stylish
    elif format_name == 'plain':
        return format_plain
    else:
        raise ValueError(f"Unknown format: {format_name}")
