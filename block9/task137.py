def rearrange_word(word):
    if len(word) != 12:
        raise ValueError("Слово должно содержать ровно 12 букв.")

    new_order = [0, 11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    rearranged = ''.join(word[i] for i in new_order)

    return rearranged


word = input("Введите слово: ")
result = rearrange_word(word)
print(result)
