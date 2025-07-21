import sys
from stats import num_words, sort_dictionary, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
        
def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    contents = get_book_text(f"./{path}")
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words(contents)} total words")
    print(f"--------- Character Count -------")
    character_dictionary = count_characters(contents)
    final_dictionary = sort_dictionary(character_dictionary)
    for item in final_dictionary:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print(f"============= END ===============")

main()

