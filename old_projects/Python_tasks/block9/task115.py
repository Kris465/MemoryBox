def remove_odd_o(sentence):
    result = []
    for index, char in enumerate(sentence):
        if char != 'о' or index % 2 == 0:
            result.append(char)
    return ''.join(result)


sentence = input("Введите предложение: ")
modified_sentence = remove_odd_o(sentence)
print("Измененное предложение:", modified_sentence)
