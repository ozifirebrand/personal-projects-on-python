def summarise_letters(word):
    tuple_of_characters = ()
    for character in word:
        if character not in tuple_of_characters:
            character = (character,)
            tuple_of_characters = tuple_of_characters + character
        else:
            character = ('',)
    print(tuple_of_characters)
    return tuple_of_characters