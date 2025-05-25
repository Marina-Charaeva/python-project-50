from gendiff.cli import parser
import sys
from gendiff.read_file import read_file
from gendiff.parser import parse_files

def main():
    args = parser()  # Получаем аргументы командной строки
    file1_data = read_file(args.first_file)
    file2_data = read_file(args.second_file)

    differences = parse_files(file1_data, file2_data)

    for key, value in differences.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()