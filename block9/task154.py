def count_unique_letters(word):

    unique_letters = set(word.lower())

    unique_letters = {letter for letter in unique_letters if letter.isalpha()}

    return len(unique_letters)


word = "Программирование"
result = count_unique_letters(word)
print("Количество различных букв в слове:", result)
