array = list(map(float, input("Введите числа через пробел: ").split()))

positive_count = sum(1 for x in array if x > 0)
negative_count = sum(1 for x in array if x < 0)

print("Положительных:", positive_count)
print("Отрицательных:", negative_count)
