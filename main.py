from stats import count_words
from stats import count_chars
from stats import sort_char_dict

def get_book_text(file):
    with open(file) as f:
        book = f.read()
    return book

def char_report(sorted_chars):
    report = ""
    chars_for_report = []
    for entry in sorted_chars:
        if entry["char"].isalpha():
            chars_for_report.append(f"{entry['char']}: {entry['num']}")
    report = "\n".join(chars_for_report)
    return report

def main():
    file = "books/frankenstein.txt"
    book = get_book_text(file)
    word_count = count_words(book)
    char_count = count_chars(book)
    sorted_chars = sort_char_dict(char_count)
    print(f"""============ BOOKBOT ============
Analyzing book found at {file}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{char_report(sorted_chars)}
============= END ===============""")
    
main()