students = int(input("Введите количество студентов Совы: "))
students_names = []

for i in range(students):
    student_name = input(f"Введите имя студента {i + 1}: ")

    students_names.append(student_name)

print("Поздравляю с успешным выпуском:", *students_names)
