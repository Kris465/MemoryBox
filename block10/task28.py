def count_n_letters(sentence):
    """Подсчитывает количество букв 'н' в предложении."""
    count = 0
    for char in sentence.lower():
        if char == 'н':
            count += 1
    return count


def main():
    sentence1 = input("Введите первое предложение: ")
    sentence2 = input("Введите второе предложение: ")

    total_n = count_n_letters(sentence1) + count_n_letters(sentence2)

    print(f"Общее количество букв 'н' в двух предложениях: {total_n}")


if __name__ == "__main__":
    main()
