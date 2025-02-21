physics_grades_class1 = [4, 5, 3, 4, 5, 4, 3, 5, 4, 5]


physics_grades_class2 = [5, 4, 5, 3, 4, 5, 4, 3, 5, 4]


def calculate_average_grade(grades):
    return sum(grades) / len(grades)


avg_class1 = calculate_average_grade(physics_grades_class1)
print(f"Средняя оценка по физике в первом классе: {avg_class1:.2f}")


avg_class2 = calculate_average_grade(physics_grades_class2)
print(f"Средняя оценка по физике в втором классе: {avg_class1:.2f}")
