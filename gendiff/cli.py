import argparse


def create_parser():
    """Create and return argument parser."""
    parser = argparse.ArgumentParser(
        description='Generate diff between two files'
    )
    parser.add_argument(
        'first_file',
        help='path to first file (JSON or YAML)'
    )
    parser.add_argument(
        'second_file',
        help='path to second file (JSON or YAML)'
    )
    parser.add_argument('-f', '--format',
                       help='output format (default: stylish)',
                       default='stylish',
                       choices=['stylish', 'plain', 'json'])
    return parser


def parse_args():
    """Parse and return command line arguments."""
    return create_parser().parse_args()
