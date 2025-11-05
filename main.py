from stats import get_num_words
from stats import get_num_characters
from stats import sorted_character_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text_path = sys.argv[1]
    text = get_book_text(text_path)
    word_count = get_num_words(text)
    char_counts = get_num_characters(text)
    sorted_counts = sorted_character_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")

    for count_dict in sorted_counts:
        current_char = count_dict["char"]
        current_count = count_dict["num"]

        if not current_char.isalpha():
            continue

        print(f"{current_char}: {current_count}")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()