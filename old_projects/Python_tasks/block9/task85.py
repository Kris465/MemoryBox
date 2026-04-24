def find_combination(sentence):

    index_chu = sentence.find("чу")
    index_shu = sentence.find("щу")

    if index_chu != -1 and (index_shu == -1 or index_chu < index_shu):
        return index_chu + 1
    elif index_shu != -1:
        return index_shu + 1

    return None


sentence = input("Введите предложение: ")
result = find_combination(sentence)

if result:
    print(f"Первое буквосочетание найдено на позиции: {result}")
else:
    print("Буквосочетания 'чу' или 'щу' не найдены.")
