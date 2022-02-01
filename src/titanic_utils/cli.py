import argparse
import sys

from titanic_utils.str_utils import extract_titles


def main():
    parser = argparse.ArgumentParser(description="Extract the title from a name")
    parser.add_argument("--name", required=True, help="Name to extract title from")
    args = parser.parse_args()
    print(extract_titles(args.name))


if __name__ == "__main__":
    # This part will be executed
    # when calling the script from the terminal
    main()
