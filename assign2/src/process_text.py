def process_text(text, is_spelling_correct = lambda word: True):
    def process_word(word):
        try:
            return word if is_spelling_correct(word) else f'[{word}]'
        except Exception as exception:
            return f"_{word}_"
    
    def process_line(line):
        return ' '.join(map(process_word, line.split()))
    
    return '\n'.join(map(process_line, text.splitlines()))
