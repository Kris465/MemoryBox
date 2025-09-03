# Пример массива
array = [3, -2, 5, -7, 0, 4, -1]

# Вычисляем сумму положительных элементов
sum_positive = sum(x for x in array if x > 0)

# Вычисляем сумму отрицательных элементов
sum_negative = sum(x for x in array if x < 0)

# Берем модуль суммы отрицательных элементов
abs_sum_negative = abs(sum_negative)

# Проверка деления на ноль
if abs_sum_negative != 0:
    result = sum_positive / abs_sum_negative
    print("Частное:", result)
else:
    print("Деление на ноль невозможно: сумма отрицательных элементов равна нулю.")

