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

def sort_on(items):
    return items["num"]

def sort_char_dict(dict):
    sorted_chars = []
    for k in dict:
        char_count = {}
        char_count["char"] = f"{k}"
        char_count["num"] = dict[k]
        sorted_chars.append(char_count)
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars 
    
