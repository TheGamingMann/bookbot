from stats import count_words

def get_book_text(file):
    with open(file) as f:
        book = f.read()
    return book

def main():
    file = "./books/frankenstein.txt"
    book = get_book_text(file)
    print(f"{count_words(book)} words found in the document")

main()