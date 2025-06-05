
array = [list(map(int, input("Введите массив: ").split()))]


min_value = None
max_value = None

for num in array:
    if min_value is None or num < min_value:
        min_value = num
    if max_value is None or num > max_value:
        max_value = num


condition_a = (max_value - min_value) <= 25
condition_b = min_value < max_value / 2

print(f"Условие (а): Максимальный элемент превышает минимальный не более \
      чем на 25 — {condition_a}")
print(f"Условие (б): Минимальный элемент меньше максимального более \
      чем в 2 раза — {condition_b}")
