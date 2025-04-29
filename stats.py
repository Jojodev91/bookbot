def word_counter(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def count_characters(book_text):
    character_dictonary = {}
    text = book_text.lower()
    for char in text:
        if char in character_dictonary:
            character_dictonary[char] +=1
        else:
            character_dictonary[char] = 1
    return character_dictonary

def sort_character_count(dictionary):
    this_list = []
    for key in dictionary:
        if key.isalpha() == True:
            temp_dic = {"Char": key, "Num": dictionary[key]}
            this_list.append(temp_dic)    
    this_list.sort(reverse=True, key=sort_on) 
    return this_list

def sort_on(dict):
    return  dict["Num"]

def bookbot_report(list, count, file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for x in range(0,len(list)):
        print(f"{list[x]["Char"]}: {list[x]["Num"]}")
    print("============= END ===============")
    pass