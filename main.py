from stats import get_num_words
from stats import get_num_characters

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(text)
    char_counts = get_num_characters(text)
    print(f"Found {word_count} total words")

    for c in char_counts:
        print(f"'{c}': {char_counts[c]}")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()