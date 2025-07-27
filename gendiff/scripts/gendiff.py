from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    args = parse_args()
    try:
        diff = generate_diff(args.first_file, args.second_file, args.format)
        print(diff)  # Форматирование уже выполняется в generate_diff
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == '__main__':
    main()
