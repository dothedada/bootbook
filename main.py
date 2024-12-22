def main():
    data = get_data('./books/frankenstein.txt')
    ammount_words = word_count(data)
    char_count = char_frecuency(data)
    report_printer(ammount_words, sort_chars(char_count))


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


def sort_chars(chars={}):
    sorted_chars = {}
    sorted_tuples = sorted(chars.items(), key=lambda item: (-item[1], item[0]))

    for key, value in sorted_tuples:
        sorted_chars[key] = value

    return sorted_chars


def report_printer(words_count, chars_count):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{words_count} words found in the document')
    print('')

    for char in chars_count:
        print(f"The '{char}' character was found {chars_count[char]} times")

    print('--- End report ---')


main()
