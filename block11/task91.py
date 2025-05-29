array = list(map(int, input("Введите числа через пробел: ").split()))

min_val = min(array)
max_val = max(array)
average = (min_val + max_val) / 2

result = [i for i, val in enumerate(array) if val > average]

print("Среднее арифметическое: ", average)
print("Кол-во элементовЮ, больших среднего: ", len(result))
print("Их индексы: ", result)
