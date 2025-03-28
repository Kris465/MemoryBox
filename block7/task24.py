<<<<<<< HEAD
spisok = []
user_input = ''
while user_input != 'exit':
    num = int(input("Введите количество учащихся: "))
    spisok.append(num)

total_students = sum(spisok[i] for i in range
                     (0, len(spisok), 2))
print("Общее число детей в нечетных классах: ", total_students)
exit
=======
def sum_odd_classes(students_per_class):
    total = 0
    for i in range(len(students_per_class)):
        if i % 2 == 0:
            total += students_per_class[i]
    return total


students_per_class = [30, 25, 28, 31, 29, 26, 27, 32, 33, 35, 34]
print(sum_odd_classes(students_per_class))
>>>>>>> db601d430cb832b2128b1b19d7480eb6966c95df
