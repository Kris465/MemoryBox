def remove_letter_s(sentence):
    return sentence.replace('с', '')


sentence = input("Введите предложение: ")
modified_sentence = remove_letter_s(sentence)
print("Измененное предложение:", modified_sentence)
