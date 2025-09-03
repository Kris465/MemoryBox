grades = [[] for _ in range(3)]

for student in range(1, 19):
    print(f"Введите оценки для ученика {student} (3 оценки через пробел):")
    scores = list(map(int, input().split()))
    for i in range(3):
        grades[i].append(scores[i])


print("\nОценки по предметам:")
for subject in range(3):
    print(f"Предмет {subject + 1}: ", end="")
    for student in range(18):
        print(grades[subject][student], end=" ")
    print()
