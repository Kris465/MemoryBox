from functools import reduce

numbers = list(map(int, input("Введите 8 чисел через пробел: ")))

product = reduce(lambda x, y: x * y, numbers)

if product < 10000:
    print("Произведение меньше 10000")
else:
    print("Произведение больше 10000")
