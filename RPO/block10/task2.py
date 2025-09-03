import math


def calculate_y_a():
    y_a = (((1 + math.sin(1)) / 3) +
           ((5 + math.sin(5)) / 3) +
           ((3 + math.sin(3)) / 3))
    return y_a


def calculate_y_b():
    y_b = (((2 + math.sin(2)) / (math.sin(5) + 5)) +
           ((6 + math.sin(6)) / (math.sin(3) + 3)) +
           ((1 + math.sin(1)) / (math.sin(4) + 4)))
    return y_b


def calculate_y_c():
    y_c = (((1 + math.sin(4)) / (4 + math.sin(1))) +
           ((7 + math.sin(5)) / (5 + math.sin(7))) +
           ((3 + math.sin(2)) / (2 + math.sin(3))))
    return y_c


def calculate_y_d():
    y_d = (((2 + math.sin(3)) / (3 + math.sin(2))) +
           ((1 + math.sin(5)) / (math.sin(1) + 5)) +
           ((math.sin(7) + 4) / (math.sin(3) + 7)))
    return y_d


print(f"Значение y для задачи a: {calculate_y_a()}")
print(f"Значение y для задачи b: {calculate_y_b()}")
print(f"Значение y для задачи c: {calculate_y_c()}")
print(f"Значение y для задачи d: {calculate_y_d()}")
