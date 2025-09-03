
word = input("Введите слово: ")


if len(word) >= 4:

    result = word[1] + word[3]

    print("Буквосочетание:", result)
else:
    print("Слово должно содержать как минимум 4 символа.")
