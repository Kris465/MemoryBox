def max_consecutive_spaces(sentence):
    segments = sentence.split(' ')

    max_spaces = 0
    for segment in segments:
        if segment:
            max_spaces = max(max_spaces, len(segment) - 1)

    return max_spaces


sentence = input("Введите предложение: ")
result = max_consecutive_spaces(sentence)
print("Наибольшее количество идущих подряд пробелов:", result)
