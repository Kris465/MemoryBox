def swap_halves(word):
    mid = len(word) // 2
    first_half = word[:mid]
    second_half = word[mid:]
    swapped = ''.join([second_half[i] + first_half[i] for i in range(mid)])
    return swapped


slovo = input("Введите слово из четного числа букв: ")

if len(slovo) % 2 == 0:
    modified_word = swap_halves(slovo)
    print("Измененное слово:", modified_word)
else:
    print("Ошибка: слово должно содержать четное число букв.")
