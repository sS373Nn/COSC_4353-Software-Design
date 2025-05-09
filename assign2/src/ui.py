import sys

from src.spell_check import is_spelling_correct
from src.process_text import process_text

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return None

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = input("Please enter the file name to be processed: (or press Enter to use 'sample.txt')")

        if not file_name:
            file_name ='sample.txt'

    file_contents = read_file(file_name)

    if file_contents:
        print(process_text(file_contents, is_spelling_correct))
    else:
        print("No file content to process.")

if __name__ == '__main__':
    main()
