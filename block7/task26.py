<<<<<<< HEAD
Temperatyra = [12, 7, 3, 2, 0, -2, -6, 4, 15, -13, 5, 2, 0, -3, -34, 45]

count_temp = sum(1 for temp in Temperatyra if temp < 0)
print("Количество дней с темп ниже 0:", count_temp)
=======
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
>>>>>>> db601d430cb832b2128b1b19d7480eb6966c95df
