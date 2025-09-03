def input_grades():
    data = input("Введите оценки 25 учеников по химии, разделённые пробелом: ")
    grades = [int(x) for x in data.strip().split()]
    if len(grades) != 25:
        print("Ошибка: необходимо ввести ровно 25 оценок.")
        return None
    return grades


def main():
    grades = input_grades()
    if grades is None:
        return

    failing_students = sum(1 for grade in grades if grade < 3)

    print(f"Количество неуспевающих по химии учеников: {failing_students}")


if __name__ == "__main__":
    main()
