from functools import reduce

def process_text(text, *blocks):

    def process_block(text, block):
        return ''.join(map(block, text))

    return reduce(process_block, blocks, text)
    