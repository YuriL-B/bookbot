import sys

from app.Application.Service.bookStats import count_words, count_runes, dictionary_to_list


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_book_path_by_argument() -> str:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def main():
    path_to_file: str = get_book_path_by_argument()
    book_text: str = get_book_text(path_to_file)
    print('Found {0} total words'.format(count_words(book_text)))
    dict = count_runes(book_text)
    list = dictionary_to_list(dict)
    for item in list:
        if item["char"].isalpha():
            print(item['char'], item['num'], sep=': ')
        else:
            continue

if __name__ == '__main__':
    main()
