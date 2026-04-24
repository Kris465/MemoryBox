exam1 = float(input("Введите оценку за первый экзамен: "))
exam2 = float(input("Введите оценку за второй экзамен: "))
exam3 = float(input("Введите оценку за третий экзамен: "))
exam4 = float(input("Введите оценку за четвертый экзамен: "))


if 0 <= exam1 <= 100 and 0 <= exam2 <= 100 and 0 <= exam3 <= 100 and 0 <= \
    exam4 <= 100:

    total_score = exam1 + exam2 + exam3 + exam4

    print("Сумма набранных баллов:", total_score)
else:
    print("Ошибка: Оценки должны быть в диапазоне от 0 до 100.")