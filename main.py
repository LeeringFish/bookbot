def main():
    count = word_count((get_book_text("books/frankenstein.txt")))
    print(f"Found {count} total words")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def word_count(text):
    return len(text.split())

main()