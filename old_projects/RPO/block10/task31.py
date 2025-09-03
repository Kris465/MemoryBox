def last_occurrence_position(sentence, letter):

    last_pos = 0
    for index, ch in enumerate(sentence, start=1):
        if ch.lower() == letter.lower():
            last_pos = index
    return last_pos


def main():

    sentence1 = input("Введите первое предложение: ")
    sentence2 = input("Введите второе предложение: ")

    letter = 'ш'

    pos1 = last_occurrence_position(sentence1, letter)
    pos2 = last_occurrence_position(sentence2, letter)

    if pos1 == 0 and pos2 == 0:
        print("В обоих предложениях буква 'ш' не найдена.")
    elif pos1 == 0:
        print("В первом предложении буква 'ш' не найдена.")
        print(f"Во втором предложении последний раз 'ш' встречается\
            на позиции {pos2}.")
    elif pos2 == 0:
        print("Во втором предложении буква 'ш' не найдена.")
        print(f"В первом предложении последний раз 'ш' встречается\
            на позиции {pos1}.")
    else:
        if pos1 > pos2:
            print(f"Буква 'ш' в первом предложении имеет больший порядковый\
                номер: {pos1}")
        elif pos2 > pos1:
            print(f"Буква 'ш' во втором предложении имеет больший порядковый\
                номер: {pos2}")
        else:
            print(f"Буква 'ш' встречается в обоих предложениях на одинаковой\
                позиции: {pos1}")


if __name__ == "__main__":
    main()
