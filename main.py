from stats import get_num_words, character_counter, create_report


# print("hello world")


def main():

    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    
        #print(file_contents)
        #print(get_num_words(file_contents))
        #print(character_counter(file_contents))
        print(create_report(book_path, file_contents))





main()
