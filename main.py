from stats import word_counter, count_characters, sort_character_count, bookbot_report
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():

    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]

    word_count = word_counter(get_book_text(file_path))
    character_count = count_characters(get_book_text(file_path))
    sorted_list = sort_character_count(character_count)
    bookbot_report(sorted_list, word_count, file_path)
    return

main()
