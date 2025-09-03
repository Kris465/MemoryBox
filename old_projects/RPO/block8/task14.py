num_students = 15
num_subjects = 3

grades = [[0] * num_subjects for _ in range(num_students)]


for student in range(num_students):
    print(f"Введите оценки для студента {student + 1}\
        по 3 предметам (через пробел):")
    grades[student] = list(map(int, input().split()))


students_without_twos = sum(
    1 for student in range(
        num_students) if all(grade != 2 for grade in grades[student]))
print(f"\nКоличество студентов, сдавших сессию без двоек:\
    {students_without_twos}")


subjects_with_only_4_and_5 = 0
for subject in range(num_subjects):
    if all(grade in [4, 5] for grade in (grades[student][subject] for
                                         student in range(num_students))):
        subjects_with_only_4_and_5 += 1

print(f"Количество предметов, по которым были получены только оценки '5' и '4\
    ': {subjects_with_only_4_and_5}")


twos_count = [0] * num_subjects
for subject in range(num_subjects):
    twos_count[subject] = sum(1 for student in range(
        num_students) if grades[student][subject] == 2)

print("\nКоличество двоек по каждому предмету:")
for subject in range(num_subjects):
    print(f"Предмет {subject + 1}: {twos_count[subject]}")
