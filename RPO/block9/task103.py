def swap_adjacent_letters(word):
    word_list = list(word)
    for i in range(0, len(word_list) - 1, 2):
        word_list[i], word_list[i + 1] = word_list[i + 1], word_list[i]
    return ''.join(word_list)


slovo = input("Введите слово из четного числа букв: ")

if len(slovo) % 2 == 0:
    modified_word = swap_adjacent_letters(slovo)
    print("Измененное слово:", modified_word)
else:
    print("Ошибка: слово должно содержать четное число букв.")
