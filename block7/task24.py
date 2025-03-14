def sum_odd_classes(students_per_class):
    total = 0
    for i in range(len(students_per_class)):
        if i % 2 == 0:
            total += students_per_class[i]
    return total


students_per_class = [30, 25, 28, 31, 29, 26, 27, 32, 33, 35, 34]
print(sum_odd_classes(students_per_class))
