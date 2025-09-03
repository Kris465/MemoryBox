def algebra_average(grades):
    return sum(grades) / len(grades)


class_grades = [8, 9, 10, 7, 8, 9, 8, 9, 10, 9]
print("Средняя оценка по алгебре для класса:", algebra_average(class_grades))
