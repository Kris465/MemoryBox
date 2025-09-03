m = int(input("Введите индекс первой буквы для замены (начиная с 0): "))
n = int(input("Введите индекс второй буквы для замены (начиная с 0): "))
slovo = input("Введите слово: ")


def swap_letters(slovo, m, n):
    word_list = list(slovo)
    if m < len(slovo) and n < len(slovo):
        word_list[m], word_list[n] = word_list[n], word_list[m]
    return ''.join(word_list)


modified_word = swap_letters(slovo, m, n)
print(modified_word)
