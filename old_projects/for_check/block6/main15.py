def print_numbers_less_than_a(a):
    n = 1  # Начинаем с n = 1
    while True:
        # Вычисляем текущее число в последовательности
        current_number = 1 + 1 / n
        
        # Если текущее число меньше a, печатаем его
        if current_number < a:
            print(current_number)
        else:
            # Если текущее число больше или равно a, завершаем цикл
            break
        
        # Увеличиваем n для следующего числа в последовательности
        n += 1

# Ввод числа a
a = float(input("Введите число a: "))

# Вызов функции
print_numbers_less_than_a(a)
