from .read_file import get_file_extension, read_file


def parse_file(file_path):
    extension = get_file_extension(file_path)
    if extension == '.json':
        return read_file(file_path)
    else:
        raise ValueError(f"Unsupported file format: {extension}")
