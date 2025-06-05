grades = [4, 5, 3, 4, 5, 2, 4, 3, 5, 4,
          3, 2, 4, 5, 3, 4, 2, 3, 5, 4,
          3, 2]

total_grades = sum(grades)

average_grade = total_grades / len(grades)

students_below_avg = [index + 1 for index, grade in
                      enumerate(grades) if grade < average_grade]

print(f"Количество учеников с оценкой меньше \
    среднего: {len(students_below_avg)}")
print("Номера элементов массива (учеников):", students_below_avg)
