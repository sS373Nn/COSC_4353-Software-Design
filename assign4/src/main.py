from src.Block.fetch_block import fetch_block
from src.process_text import process_text

def read_file(file_name):
    with open(file_name, 'r') as file:
        text = [line.strip() for line in file.readlines()]
    return text

def choose_text():
    return input("Please input text to process: ")

def print_chosen_block_names(block_names):
    if block_names:
        print("You've chosen to add the following blocks: ")
        for block in block_names:
            print(block)
    else:
        print("No Blocks Chosen")

def main():
    name_of_chosen_blocks = read_file("./data/blocks.txt")

    print_chosen_block_names(name_of_chosen_blocks)

    input_text = choose_text()

    processed_text = process_text(input_text, *(map(fetch_block, name_of_chosen_blocks)))

    print(processed_text)

    return 0

main()
