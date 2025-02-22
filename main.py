import sys
from stats import word_count, char_frecuency


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    data = get_data(sys.argv[1])
    ammount_words = word_count(data)
    char_count = char_frecuency(data)
    report_printer(ammount_words, sort_chars(char_count), sys.argv[1])


def get_data(file):
    with open(file) as f:
        return f.read()


def sort_chars(chars={}):
    sorted_chars = {}
    sorted_tuples = sorted(chars.items(), key=lambda item: (-item[1], item[0]))

    for key, value in sorted_tuples:
        sorted_chars[key] = value

    return sorted_chars


def report_printer(words_count, chars_count, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")

    for char in chars_count:
        print(f"{char}: {chars_count[char]}")

    print("============= END ===============")


main()
