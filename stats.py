def get_num_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def get_num_char(text):
    lowercase_text = text.lower()
    characters = {}
    for char in lowercase_text:
        if char in characters:
            characters[char] = characters[char] + 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def sort_char(characters):
    char_list = []

    for char in characters:
        char_list.append({"char": char, "num": characters[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list