from itertools import takewhile

grades = [list(map(int, input("Введите массив: ").split()))]

count_fives = len(list(takewhile(lambda grade: grade == 5, grades)))

print("Количество учеников с оценкой '5':", count_fives)
