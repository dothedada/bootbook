def word_count(string):
    return len(string.split())


def char_frecuency(string=""):
    chars = {}
    for char in string:
        if not char.isalpha():
            continue

        char_lower = char.lower()

        if char_lower not in chars:
            chars[char_lower] = 0

        chars[char_lower] += 1

    return chars
