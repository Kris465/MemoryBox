exam1_grades = [4, 2, 3, 5, 2]
exam2_grades = [3, 5, 2, 5, 2]

count_students_with_fail = sum(1 for e1, e2 in zip(exam1_grades, exam2_grades)
if e1 == 2 or e2 == 2)
print(f"количество студентовб получивших двойку: {count_students_with_fail}")
