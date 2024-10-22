def main(text):
    with open(text, 'r') as file:
        contents = file.read()
        return contents

def word_count(text):
    words = text.split()
    print(f"{len(words)} words found in the document.")

def character_count(text):
    characters_dict = {}
    for letters in text:
        lower_case_letters = letters.lower()       
        if lower_case_letters in characters_dict:
            characters_dict[lower_case_letters]+=1
        else:
            characters_dict[lower_case_letters] = 1
    return characters_dict

def alpha_list(char_dictionary):
    char_list = []
    for i in char_dict.keys():
        if i.isalpha():
            char_list.append(i)

    return char_list

if __name__ == "__main__":
    text = 'books/frankenstein.txt'
    document = main(text)
    word_count(document)
    char_dict = character_count(document)
    char_list = alpha_list(char_dict)
    
    
    print("--- Begin report of books/frankenstein.txt ---")
    word_count(document)
    for char, count in sorted(char_dict.items(),reverse=True,key=lambda x:x[1]):
        if char in char_list:
            print(f"The {char} character was found {count} times")
   
    print("--- End report ---")
