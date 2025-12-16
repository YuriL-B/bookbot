def count_words(text: str) -> int:
    return len(text.split())

def count_runes(text: str) -> list:
    text = text.lower()
    rune_dict = {}
    for char in text:
        rune_dict.update({char:rune_dict.get(char,0)+1})
    return dictionary_to_list(rune_dict)

def dictionary_to_list(dictionary: dict) -> list:
    dictionary_list = []
    for char in dictionary:
        dictionary_list.append({"char": char, "num": dictionary[char]})
    dictionary_list.sort(key=sort_on, reverse=True)
    return dictionary_list

def sort_on(items: dict) -> int:
    return items["num"]