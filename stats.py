def count_words(text):
    count = 0
    words = text.split()
    for w in words:
        count += 1
    return count

def count_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            count = chars[char]
            count += 1
            chars[char] = count
        else:
            count = 1
            chars[char] = count
    return chars
