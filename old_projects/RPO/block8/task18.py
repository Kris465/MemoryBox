
num_grades = 11
num_classes = 4


students = []


for grade in range(num_grades):
    print(f"Введите количество учеников для {grade + 1} класса \
        (A, B, C, D) через пробел:")
    class_counts = list(map(int, input().split()))
    students.append(class_counts)


min_students_in_class = min(min(class_counts) for class_counts in students)
print(f"\nКоличество учеников в самом \
    малочисленном классе: {min_students_in_class}")


min_students_in_grade = min(sum(class_counts) for class_counts in students)
print(f"Минимальное значение общего количества учеников в классах одной \
    параллели: {min_students_in_grade}")


total_students_per_class = [0] * num_classes

for class_index in range(num_classes):
    total_students_per_class[class_index] = \
        sum(students[grade][class_index] for grade in range(num_grades))

min_students_in_classes = min(total_students_per_class)
print(f"Минимальное значение общего количества учеников \
    в классах A, B, C и D: {min_students_in_classes}")
