def count_words(text):
    count = 0
    words = text.split()
    for w in words:
        count += 1
    return count