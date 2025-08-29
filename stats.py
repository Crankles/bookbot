def get_num_words(text):
            words = text.split()
            return(f"Found {len(words)} total words")

def character_counter(text):
            character_counts = {}
            for character in text.lower():
                if character not in character_counts:
                    character_counts[character] = 1
                else:
                    character_counts[character] += 1
            return character_counts

def get_sorted_dict_list(dict):
       
    def sort_on(a_dict):
        return a_dict["num"]
       
    dict_list = [{"char": key, "num": dict[key]} for key in dict if key.isalpha()]
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

def create_report(path, file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file)} total words")
    print("--------- Character Count -------")
    for item in get_sorted_dict_list(character_counter(file)):
          print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")