num_students = int(input("Введите количество учеников: "))

grades = []


for i in range(num_students):
    grade = int(input(f"Введите оценку для ученика {i + 1}: "))
    grades.append(grade)

count_of_fives = 0

for grade in grades:
    if grade == 5:
        count_of_fives += 1


print(f"Количество пятерок: {count_of_fives}")
