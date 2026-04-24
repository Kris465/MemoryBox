# Запрашиваем у пользователя два числа
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Вычисляем сумму, разность, произведение и частное
summa = num1 + num2
raznost = num1 - num2
proizvedenie = num1 * num2

# Проверка деления на ноль перед делением
if num2 != 0:
    chastnoe = num1 / num2
else:
    chastnoe = "Деление на ноль невозможно"

# Вывод результатов
print(f"Сумма: {summa}")
print(f"Разность: {raznost}")
print(f"Произведение: {proizvedenie}")
print(f"Частное: {chastnoe}")
