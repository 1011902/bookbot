from stats import wordCount, characterCount, list
import sys

def get_book_text(path_to_file) :
    with open(path_to_file) as f:
        return f.read()

def main() :
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    contents = get_book_text(book_path)
    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {book_path}...\n"
    "----------- Word Count ----------")
    wordCount(contents)
    print("--------- Character Count -------")
    chars_dict = characterCount(contents)
    sortedList = list(chars_dict)
    for item in sortedList:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()