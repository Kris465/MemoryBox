num_courses = 4
num_groups = 6

students = []

for course in range(num_courses):
    print(f"Введите количество студентов для курса\
        {course + 1} в группах (6 групп) через пробел:")
    group_counts = list(map(int, input().split()))
    students.append(group_counts)

total_students_per_course = [sum(group_counts) for group_counts in students]
min_students_course = total_students_per_course.index(
    min(total_students_per_course)) + 1

min_students_group = float('inf')
min_group_info = (0, 0)

for course in range(num_courses):
    for group in range(num_groups):
        if students[course][group] < min_students_group:
            min_students_group = students[course][group]
            min_group_info = (group + 1, course + 1)

min_groups_per_course = []
for course in range(num_courses):
    min_group_index = students[course].index(min(students[course])) + 1
    min_groups_per_course.append(min_group_index)

print(f"\nКурс с наименьшим количеством студентов: {min_students_course}")
print(f"Самая малочисленная группа: Группа\
    {min_group_info[0]}, Курс {min_group_info[1]}")
print("Номера самых малочисленных групп для каждого курса:")
for course in range(num_courses):
    print(f"Курс {course + 1}: Группа {min_groups_per_course[course]}")
