from itertools import takewhile

grades = [5, 5, 5, 4, 4, 3, 5, 2, 5, 4, 3, 2, 5, 5, 4, 3, 2, 4, 3, 5, 4, 3, 2, 2]

count_fives = len(list(takewhile(lambda grade: grade == 5, grades)))

print("Количество учеников с оценкой '5':", count_fives)
