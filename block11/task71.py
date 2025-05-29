def input_grades():
    data = input("Введите оценки по 10 предметам, разделённые пробелом: ")
    grades = [int(x) for x in data.strip().split()]
    if len(grades) != 10:
        print("Ошибка: необходимо ввести ровно 10 оценок.")
        return None
    return grades


def main():
    grades = input_grades()
    if grades is None:
        return

    count_four = sum(1 for g in grades if g == 4)
    count_five = sum(1 for g in grades if g == 5)

    print(f"Общее количество четверок: {count_four}")
    print(f"Общее количество пятёрок: {count_five}")


if __name__ == "__main__":
    main()
