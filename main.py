def main():
    data = get_data('./books/frankenstein.txt')
    ammount_words = word_count(data)
    print(ammount_words)


def get_data(file):
    with open(file) as f:
        return f.read()


def word_count(string=''):
    return len(string.split())


main()
