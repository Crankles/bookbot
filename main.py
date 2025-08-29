from stats import get_num_words, character_counter, create_report
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        book_path = sys.argv[1]

        with open(book_path) as f:
            file_contents = f.read()
    
        print(create_report(book_path, file_contents))

main()
