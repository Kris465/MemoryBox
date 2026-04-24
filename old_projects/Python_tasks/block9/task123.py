def insert_before_last_i(sentence, letter):
    index = sentence.rfind('и')
    if index != -1:
        return sentence[:index] + letter + sentence[index:]
    return sentence


sentence = input("Введите предложение, оканчивающееся символом '_': ")
letter = input("Введите букву для вставки: ")

modified_sentence = insert_before_last_i(sentence, letter)
print("Измененное предложение:", modified_sentence)
