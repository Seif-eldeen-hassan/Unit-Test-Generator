import argparse
import os
import sys
from utils import get_functions_from_code, clean_function
from client import generate_unit_tests

def main():
    parser = argparse.ArgumentParser(description="Generate Unit test for a specific function")
    parser.add_argument("file_path", help="The python file path")
    args = parser.parse_args()
    file_path = args.file_path

    if not os.path.exists(file_path) or not file_path.endswith('.py'):
        print("Error: This tool only generates unit tests for functions.")
        sys.exit(1)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
    except Exception:
        print("Error: This tool only generates unit tests for functions.")
        sys.exit(1)

    functions = get_functions_from_code(source_code)

    if len(functions) == 1:
        cleaned_code = clean_function(functions[0])
        try:
            result = generate_unit_tests(cleaned_code)
            print(result) 
        except Exception:
            print("Error: This tool only generates unit tests for functions.")
            sys.exit(1)
    else:
        print("Error: This tool only generates unit tests for functions.")
        sys.exit(1)

if __name__ == "__main__":
    main()