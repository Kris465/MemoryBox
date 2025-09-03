def letter_share(sentence, letter):
    """Вычисляет долю (в %) заданной буквы в предложении."""
    total_chars = len(sentence)
    if total_chars == 0:
        return 0
    count_letter = sum(1 for ch in sentence.lower() if ch == letter.lower())
    share_percentage = (count_letter / total_chars) * 100
    return share_percentage


def main():

    sentence1 = input("Введите первое предложение: ")
    sentence2 = input("Введите второе предложение: ")
    letter = input("Введите букву для анализа: ")

    if len(letter) != 1:
        print("Пожалуйста, введите одну букву.")
        return
    share1 = letter_share(sentence1, letter)
    share2 = letter_share(sentence2, letter)

    if share1 > share2:
        print(f"В первом предложении доля буквы '{letter}' \
              больше: {share1:.2f}%")
    elif share2 > share1:
        print(f"Во втором предложении доля буквы '{letter}' \
              больше: {share2:.2f}%")
    else:
        print(f"Доли буквы '{letter}' равны и составляют: {share1:.2f}%")


if __name__ == "__main__":
    main()
