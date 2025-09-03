grades = []

num_students = 18
num_subjects = 3

for student_num in range(num_students):
    print(f"Введите оценки ученика {student_num + 1} \
        по 3 предметам через пробел:")
    row = list(map(int, input().split()))
    if len(row) != num_subjects:
        print(f"Ошибка: введено неверное количество оценок ({len(row)}). \
            Должно быть {num_subjects}.")
        continue
    grades.append(row)

fives_count = sum(grade.count(5) for grade in grades)
print(f"Общее количество пятерок: {fives_count}")


for student_num, grade in enumerate(grades):
    threes_count = grade.count(3)
    print(f"Ученик {student_num + 1} имеет {threes_count} троек.")

for subject_num in range(num_subjects):
    twos_count = sum(grade[subject_num] == 2 for grade in grades)
    print(f"По предмету {subject_num + 1} имеется {twos_count} двоек.")
