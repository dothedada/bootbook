def main():
    data = get_data('./books/frankenstein.txt')
    ammount_words = word_count(data)
    char_count = char_frecuency(data)
    print(ammount_words)
    print(char_count)


def get_data(file):
    with open(file) as f:
        return f.read()


def word_count(string):
    return len(string.split())


def char_frecuency(string=''):
    chars = {}
    for char in string:
        if not char.isalpha():
            continue
        char_lower = char.lower()
        if char_lower not in chars:
            chars[char_lower] = 0

        chars[char_lower] += 1

    return chars


main()
