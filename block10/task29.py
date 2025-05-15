def count_letter_in_sentence(sentence, letter):
    """Подсчитывает количество заданной буквы в предложении."""
    count = 0
    for char in sentence.lower():
        if char == letter.lower():
            count += 1
    return count


def main():
    sentence1 = input("Введите первое предложение: ")
    sentence2 = input("Введите второе предложение: ")
    sentence3 = input("Введите третье предложение: ")

    letter = input("Введите букву для подсчёта: ")

    if len(letter) != 1:
        print("Пожалуйста, введите одну букву.")
        return

    total_count = (
        count_letter_in_sentence(sentence1, letter) +
        count_letter_in_sentence(sentence2, letter) +
        count_letter_in_sentence(sentence3, letter)
    )

    print(f"Общее количество букв \
          '{letter}' во всех трёх предложениях: {total_count}")


if __name__ == "__main__":
    main()
