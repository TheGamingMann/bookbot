from stats import count_words
from stats import count_chars

def get_book_text(file):
    with open(file) as f:
        book = f.read()
    return book

def main():
    file = "./books/frankenstein.txt"
    book = get_book_text(file)
    word_count = count_words(book)
    char_count = count_chars(book)
    print(f"{word_count} words found in the document")
    print(char_count)

main()