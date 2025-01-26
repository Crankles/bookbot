# print("hello world")

def main():

    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    
        #print(file_contents)

        def word_count():
            words = file_contents.split()
            return(len(words))
        
        def character_counter():
            character_counts = {}
            for character in file_contents.lower():
                if character not in character_counts:
                    character_counts[character] = 1
                else:
                    character_counts[character] += 1
            return character_counts
        
        def create_report():
            print(f"A report on {book_path}")
            print(f"There are {word_count()} words.")
            char_dict = character_counter()
            for char in char_dict:
                if char.isalpha():
                    print(f"The character '{char}' appears {char_dict[char]} times.")
            return "End of report :)"

        #print(word_count())
        #print(character_counter())
        print(create_report())



main()