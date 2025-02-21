grades = []


for i in range(20):
    grade = float(input(f"Введите оценку ученика {i + 1}: "))

    if 0 <= grade <= 100:
        grades.append(grade)
    else:
        print("Ошибка: оценка должна быть в диапазоне от 0 до 100.")
        grade = float(input(f"Введите оценку ученика {i + 1} снова: "))
        grades.append(grade)

if len(grades) > 0:
    average_grade = sum(grades) / len(grades)
    print(f"Средняя оценка по физике: {average_grade:.2f}")
else:
    print("Нет оценок для вычисления средней.")
