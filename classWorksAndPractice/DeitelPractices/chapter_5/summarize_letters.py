def count_characters(characters):
    a_tuple = ()
    a_list = []
    for char in characters:
        if char in a_list:
            continue
        else:
            a_list.append(char)
            a_tuple = tuple(a_list)
    return a_tuple

print(count_characters("Sherifat Omo logba logba"))