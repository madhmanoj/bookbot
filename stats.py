def num_words(text):
    return len(text.split())

def count_characters(text):
    dictionary = {}
    for i in text:
        if i.lower() in dictionary:
            dictionary[i.lower()] += 1
        else:
            dictionary[i.lower()] = 1
    return dictionary

def sort_on(items):
    return items["num"]

def sort_dictionary(character_dictionary):
    transformed_dictionary = [{"char": i, "num": character_dictionary[i]} for i in character_dictionary]
    transformed_dictionary.sort(reverse=True, key=sort_on)
    return transformed_dictionary
