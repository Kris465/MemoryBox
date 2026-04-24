import math


def is_perfect_square(num):
    if num < 0:
        return False
    root = math.isqrt(num)  # целая часть квадратного корня
    return root * root == num


n = int(input("Введите натуральное число n: "))


a = []
print(f"Введите {n} целых чисел:")
for i in range(n):
    a.append(int(input(f"a{i+1}: ")))


count_squares = sum(1 for num in a if is_perfect_square(num))

print(f"Количество чисел, являющихся полными квадратами: {count_squares}")
