word = input("Введите слово из 12 букв: ")


if len(word) != 12:
    print("Ошибка: слово должно содержать ровно 12 букв.")
else:

    part1 = word[:2]
    middle = word[2:9]
    part2 = word[9:]

    middle_reversed = middle[::-1]

    result = part1 + middle_reversed + part2

    print("Результат:", result)
