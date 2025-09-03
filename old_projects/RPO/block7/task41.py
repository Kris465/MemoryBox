
grades = [5, 4, 3, 2, 5, 4, 3, 5, 2]

grade_count = {5: 0, 4: 0, 3: 0, 2: 0}

for grade in grades:
    if grade in grade_count:
        grade_count[grade] += 1

print(f"Пятёрок: {grade_count[5]}")
print(f"Четвёрок: {grade_count[4]}")
print(f"Троек: {grade_count[3]}")
print(f"Двоек: {grade_count[2]}")
