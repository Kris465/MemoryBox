from math import log, sin, cos, sqrt
from random import randint

print("Добро пожаловать в калькулятор")
print("Вы желаете ввести свои числа или рандомные значения?")
print("1 - Свои числа")
print("2 - рандомные значения")
choice1 = int(input("Ваш выбор: "))

if choice1 == 1:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

elif choice1 == 2:
    interval = int(input("Введите промежуток чисел: "))
    random_num1 = randint(0, interval)
    random_num2 = randint(0, interval)
    print(f"Первое число: {random_num1}")
    print(f"Второе число: {random_num2}")


print("Выберите то, что хотите сделать с числами")
print("1 - сложение")
print("2 - вычитание")
print("3 - умножение")
print("4 - деление")
choice2 = int(input("Ваш выбор: "))

# выбор пользователя
if choice2 == 1 and choice1 == 1:
    print(f"Ваш пример: {num1} + {num2}")
elif choice2 == 2 and choice1 == 1:
    print(f"Ваш пример: {num1} - {num2}")
elif choice2 == 3 and choice1 == 1:
    print(f"Ваш пример: {num1} * {num2}")
elif choice2 == 4 and choice1 == 1:
    print(f"Ваш пример: {num1} : {num2}")


if choice2 == 1 and choice1 == 2:
    print(f"Ваш пример: {random_num1} + {random_num2}")
elif choice2 == 2 and choice1 == 2:
    print(f"Ваш пример: {random_num1} - {random_num2}")
elif choice2 == 3 and choice1 == 2:
    print(f"Ваш пример: {random_num1} * {random_num2}")
elif choice2 == 4 and choice1 == 2:
    print(f"Ваш пример: {random_num1} : {random_num2}")


print("Выберите доп.функции: ")
print("1 - возведение в степень")
print("2 - извлечение корня")
print("3 - модуль")
print("4 - логарифм")
print("5 - синус")
print("6 - косинус")
print("7 - оставить как есть")
choice3 = int(input("Ваш выбор: "))

# СЛОЖЕНИЕ

# степень
if choice2 == 1 and choice3 == 1 and choice1 == 1:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(num1, degree)
        # конечный ответ
        otvet1_in_degree = num1_in_degree + num2
        print(f"ваш пример: {num1}^{degree} + {num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(num2, degree)
        print(f"Ваш пример: {num1} + {num2}^{degree}")
        # конечный ответ
        otvet2_in_degree = num1 + num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        # конечный ответ
        nums_in_degree = pow(num1, degree) + pow(num2, degree)
        print(f"Ваш пример: {num1}^{degree} + {num2}^{degree}")

# извлечение корня
if choice2 == 1 and choice3 == 2 and choice1 == 1:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(num1)
        print(f"Ваш пример: ↓▬{num1} + {num2}")
        # конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 + num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(num2)
        print(f"Ваш пример: {num1} + ↓▬{num2}")
        # конечный ответ
        otvet_in_root_extraction2 = num1 + root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(num1) + sqrt(num2)
        print(f"Ваш пример: ↓▬{num1} + ↓▬{num2}")
        # конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

# модуль
if choice2 == 1 and choice3 == 3 and choice1 == 1:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        # конечный ответ
        otvet_in_module1 = abs(num1) + num2
        print(f"Ваш пример: |{num1}| + {num2}")
    if num_choice3 == 2:
        # конечный ответ
        otvet_in_module2 = num1 + abs(num2)
        print(f"Ваш пример: {num1} + |{num2}|")
    if num_choice3 == 3:
        module_nums = abs(num1) + abs(num2)
        # конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{num1}| + |{num2}|")

# логарифм
if choice2 == 1 and choice3 == 4 and choice1 == 1:
    print("Из какого числа хотите совершить логарифм?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num1 = log(num1, base) + num2
        print(f"Ваш пример: log{base}^{num1} + {num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num2 = num1 + log(num2, base)
        print(f"Ваш пример: {num1} + log{base}^{num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log(num1, base) + log(num2, base)
        # конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{num1} + log{base}^{num2}")

# синус
if choice2 == 1 and choice3 == 5 and choice1 == 1:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(num1)
        # конечный ответ
        otvet_sin_num1 = sin_num1 + num2
        print(f"Ваш пример: sin{num1} + {num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(num2)
        # конечный ответ
        otvet_sin_num2 = num1 + sin_num2
        print(f"Ваш пример: {num1} + sin{num2}")
    elif num_choice5 == 3:
        # конечный ответ
        sin_nums = sin(num1) + sin(num2)
        print(f"Ваш пример: sin{num1} + sin{num2}")

# косинус
if choice2 == 1 and choice3 == 6 and choice1 == 1:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(num1)
        # конечный ответ
        otvet_cos_num1 = cos_num1 + num2
        print(f"Ваш пример: cos{num1} + {num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(num2)
        # конечный ответ
        otvet_cos_num2 = num1 + cos_num2
        print(f"Ваш пример: {num1} + cos{num2}")
    elif num_choice6 == 3:
        # конечный ответ
        cos_nums = cos(num1) + cos(num2)
        print(f"Ваш пример: cos{num1} + cos{num2}")

# оставить все как есть
if choice3 == 7 and choice2 == 1 and choice1 == 1:
    print(f"Ваш пример: {num1} + {num2}")

# ВЫЧИТАНИЕ

# степень
if choice2 == 2 and choice3 == 1 and choice1 == 1:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(num1, degree)
        # конечный ответ
        otvet1_in_degree = num1_in_degree - num2
        print(f"ваш пример: {num1}^{degree} - {num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(num2, degree)
        print(f"Ваш пример: {num1} - {num2}^{degree}")
        # конечный ответ
        otvet2_in_degree = num1 - num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        # конечный ответ
        nums_in_degree = pow(num1, degree) - pow(num2, degree)
        print(f"Ваш пример: {num1}^{degree} - {num2}^{degree}")

# извлечение корня
if choice2 == 2 and choice3 == 2 and choice1 == 1:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(num1)
        print(f"Ваш пример: ↓▬{num1} - {num2}")
        # конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 - num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(num2)
        print(f"Ваш пример: {num1} - ↓▬{num2}")
        # конечный ответ
        otvet_in_root_extraction2 = num1 - root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(num1) - sqrt(num2)
        print(f"Ваш пример: ↓▬{num1} - ↓▬{num2}")
        # конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

# модуль
if choice2 == 2 and choice3 == 3 and choice1 == 1:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        # конечный ответ
        otvet_in_module1 = abs(num1) - num2
        print(f"Ваш пример: |{num1}| - {num2}")
    if num_choice3 == 2:
        # конечный ответ
        otvet_in_module2 = num1 - abs(num2)
        print(f"Ваш пример: {num1} - |{num2}|")
    if num_choice3 == 3:
        module_nums = abs(num1) - abs(num2)
        # конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{num1}| - |{num2}|")

# логарифм
if choice2 == 2 and choice3 == 4 and choice1 == 1:
    print("Из какого числа хотите совершить логарифм?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        log_num1 = log(num1, base)
        # конечный ответ
        otvet_log_num1 = log(num1, base) - num2
        print(f"Ваш пример: log{base}^{num1} - {num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num2 = num1 - log(num2, base)
        print(f"Ваш пример: {num1} - log{base}^{num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log(num1, base) - log(num2, base)
        # конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{num1} - log{base}^{num2}")

# синус
if choice2 == 2 and choice3 == 5 and choice1 == 1:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(num1)
        # конечный ответ
        otvet_sin_num1 = sin_num1 - num2
        print(f"Ваш пример: sin{num1} - {num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(num2)
        # конечный ответ
        otvet_sin_num2 = num1 - sin_num2
        print(f"Ваш пример: {num1} - sin{num2}")
    elif num_choice5 == 3:
        # конечный ответ
        sin_nums = sin(num1) - sin(num2)
        print(f"Ваш пример: sin{num1} - sin{num2}")

# косинус
if choice2 == 2 and choice3 == 6 and choice1 == 1:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(num1)
        # конечный ответ
        otvet_cos_num1 = cos_num1 - num2
        print(f"Ваш пример: cos{num1} - {num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(num2)
        # конечный ответ
        otvet_cos_num2 = num1 - cos_num2
        print(f"Ваш пример: {num1} - cos{num2}")
    elif num_choice6 == 3:
        # конечный ответ
        cos_nums = cos(num1) - cos(num2)
        print(f"Ваш пример: cos{num1} - cos{num2}")

# оставить все как есть
if choice3 == 7 and choice2 == 2 and choice1 == 1:
    print(f"Ваш пример: {num1} - {num2}")

# УМНОЖЕНИЕ

# степень
if choice2 == 3 and choice3 == 1 and choice1 == 1:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(num1, degree)
        # конечный ответ
        otvet1_in_degree = num1_in_degree * num2
        print(f"ваш пример: {num1}^{degree} * {num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(num2, degree)
        print(f"Ваш пример: {num1} * {num2}^{degree}")
        # конечный ответ
        otvet2_in_degree = num1 * num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        # конечный ответ
        nums_in_degree = pow(num1, degree) * pow(num2, degree)
        print(f"Ваш пример: {num1}^{degree} * {num2}^{degree}")

# извлечение корня
if choice2 == 3 and choice3 == 2 and choice1 == 1:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(num1)
        print(f"Ваш пример: ↓▬{num1} * {num2}")
        # конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 - num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(num2)
        print(f"Ваш пример: {num1} * ↓▬{num2}")
        # конечный ответ
        otvet_in_root_extraction2 = num1 * root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(num1) * sqrt(num2)
        print(f"Ваш пример: ↓▬{num1} * ↓▬{num2}")
        # конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

# модуль
if choice2 == 3 and choice3 == 3 and choice1 == 1:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        # конечный ответ
        otvet_in_module1 = abs(num1) * num2
        print(f"Ваш пример: |{num1}| * {num2}")
    if num_choice3 == 2:
        # конечный ответ
        otvet_in_module2 = num1 * abs(num2)
        print(f"Ваш пример: {num1} * |{num2}|")
    if num_choice3 == 3:
        module_nums = abs(num1) * abs(num2)
        # конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{num1}| * |{num2}|")

# логарифм
if choice2 == 3 and choice3 == 4 and choice1 == 1:
    print("Из какого числа хотите совершить логарифм?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num1 = log(num1, base) * num2
        print(f"Ваш пример: log{base}^{num1} * {num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num2 = num1 * log(num2, base)
        print(f"Ваш пример: {num1} * log{base}^{num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log(num1, base) * log(num2, base)
        # конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{num1} * log{base}^{num2}")

# синус
if choice2 == 3 and choice3 == 5 and choice1 == 1:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(num1)
        # конечный ответ
        otvet_sin_num1 = sin_num1 * num2
        print(f"Ваш пример: sin{num1} * {num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(num2)
        # конечный ответ
        otvet_sin_num2 = num1 * sin_num2
        print(f"Ваш пример: {num1} * sin{num2}")
    elif num_choice5 == 3:
        # конечный ответ
        sin_nums = sin(num1) * sin(num2)
        print(f"Ваш пример: sin{num1} * sin{num2}")

# косинус
if choice2 == 3 and choice3 == 6 and choice1 == 1:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(num1)
        # конечный ответ
        otvet_cos_num1 = cos_num1 * num2
        print(f"Ваш пример: cos{num1} * {num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(num2)
        # конечный ответ
        otvet_cos_num2 = num1 * cos_num2
        print(f"Ваш пример: {num1} * cos{num2}")
    elif num_choice6 == 3:
        # конечный ответ
        cos_nums = cos(num1) * cos(num2)
        print(f"Ваш пример: cos{num1} * cos{num2}")

# оставить все как есть
if choice3 == 7 and choice2 == 3 and choice1 == 1:
    print(f"Ваш пример: {num1} * {num2}")

# ДЕЛЕНИЕ

# степень
if choice2 == 4 and choice3 == 1 and choice1 == 1:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(num1, degree)
        # конечный ответ
        otvet1_in_degree = num1_in_degree / num2
        print(f"ваш пример: {num1}^{degree} : {num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(num2, degree)
        print(f"Ваш пример: {num1} : {num2}^{degree}")
        # конечный ответ
        otvet2_in_degree = num1 / num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        # конечный ответ
        nums_in_degree = pow(num1, degree) / pow(num2, degree)
        print(f"Ваш пример: {num1}^{degree} : {num2}^{degree}")

# извлечение корня
if choice2 == 4 and choice3 == 2 and choice1 == 1:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(num1)
        print(f"Ваш пример: ↓▬{num1} : {num2}")
        # конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 / num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(num2)
        print(f"Ваш пример: {num1} : ↓▬{num2}")
        # конечный ответ
        otvet_in_root_extraction2 = num1 / root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(num1) / sqrt(num2)
        print(f"Ваш пример: ↓▬{num1} : ↓▬{num2}")
        # конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

# модуль
if choice2 == 3 and choice3 == 3 and choice1 == 1:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        # конечный ответ
        otvet_in_module1 = abs(num1) / num2
        print(f"Ваш пример: |{num1}| : {num2}")
    if num_choice3 == 2:
        # конечный ответ
        otvet_in_module2 = num1 / abs(num2)
        print(f"Ваш пример: {num1} : |{num2}|")
    if num_choice3 == 3:
        module_nums = abs(num1) / abs(num2)
        # конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{num1}| : |{num2}|")

# логарифм
if choice2 == 4 and choice3 == 4 and choice1 == 1:
    print("Из какого числа хотите совершить логарифм?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num1 = log(num1, base) / num2
        print(f"Ваш пример: log{base}^{num1} : {num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num2 = num1 / log(num2, base)
        print(f"Ваш пример: {num1} : log{base}^{num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log(num1, base) / log(num2, base)
        # конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{num1} : log{base}^{num2}")

# синус
if choice2 == 4 and choice3 == 5 and choice1 == 1:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(num1)
        # конечный ответ
        otvet_sin_num1 = sin_num1 / num2
        print(f"Ваш пример: sin{num1} : {num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(num2)
        # конечный ответ
        otvet_sin_num2 = num1 / sin_num2
        print(f"Ваш пример: {num1} : sin{num2}")
    elif num_choice5 == 3:
        # конечный ответ
        sin_nums = sin(num1) / sin(num2)
        print(f"Ваш пример: sin{num1} : sin{num2}")

# косинус
if choice2 == 4 and choice3 == 6 and choice1 == 1:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(num1)
        otvet_cos_num1 = cos_num1 / num2
        print(f"Ваш пример: cos{num1} : {num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(num2)
        otvet_cos_num2 = num1 / cos_num2
        print(f"Ваш пример: {num1} : cos{num2}")
    elif num_choice6 == 3:
        cos_nums = cos(num1) / cos(num2)
        print(f"Ваш пример: cos{num1} : cos{num2}")

# оставить все как есть
if choice3 == 7 and choice2 == 4 and choice1 == 1:
    print(f"Ваш пример: {num1} : {num2}")

# Рандомные числа

# СЛОЖЕНИЕ

# степень
if choice2 == 1 and choice3 == 1 and choice1 == 2:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(random_num1, degree)
        # конечный ответ
        otvet1_in_degree = num1_in_degree + num2
        print(f"ваш пример: {random_num1}^{degree} + {random_num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(random_num2, degree)
        print(f"Ваш пример: {random_num1} + {random_num2}^{degree}")
        # конечный ответ
        otvet2_in_degree = random_num1 + num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        # конечный ответ
        nums_in_degree = pow(random_num1, degree) + pow(random_num2, degree)
        print(f"Ваш пример: {random_num1}^{degree} + {random_num2}^{degree}")

# извлечение корня
if choice2 == 1 and choice3 == 2 and choice1 == 2:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(random_num1)
        print(f"Ваш пример: ↓▬{random_num1} + {random_num2}")
        # конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 + random_num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(random_num2)
        print(f"Ваш пример: {random_num1} + ↓▬{random_num2}")
        # конечный ответ
        otvet_in_root_extraction2 = random_num1 + root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(random_num1) + sqrt(random_num2)
        print(f"Ваш пример: ↓▬{random_num1} + ↓▬{random_num2}")
        # конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

# модуль
if choice2 == 1 and choice3 == 3 and choice1 == 2:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        # конечный ответ
        otvet_in_module1 = abs(random_num1) + random_num2
        print(f"Ваш пример: |{random_num1}| + {random_num2}")
    if num_choice3 == 2:
        # конечный ответ
        otvet_in_module2 = random_num1 + abs(random_num2)
        print(f"Ваш пример: {random_num1} + |{random_num2}|")
    if num_choice3 == 3:
        module_nums = abs(random_num1) + abs(random_num2)
        # конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{random_num1}| + |{random_num2}|")

# логарифм
if choice2 == 1 and choice3 == 4 and choice1 == 2:
    print("Из какого числа хотите совершить логарифм?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num1 = log(random_num1, base) + random_num2
        print(f"Ваш пример: log{base}^{random_num1} + {random_num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num2 = random_num1 + log(random_num2, base)
        print(f"Ваш пример: {random_num1} + log{base}^{random_num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log(random_num1, base) + log(random_num2, base)
        # конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{random_num1} + log{base}^{random_num2}")

# синус
if choice2 == 1 and choice3 == 5 and choice1 == 2:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(random_num1)
        # конечный ответ
        otvet_sin_num1 = sin_num1 + random_num2
        print(f"Ваш пример: sin{random_num1} + {random_num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(random_num2)
        # конечный ответ
        otvet_sin_num2 = random_num1 + sin_num2
        print(f"Ваш пример: {random_num1} + sin{random_num2}")
    elif num_choice5 == 3:
        # конечный ответ
        sin_nums = sin(random_num1) + sin(random_num2)
        print(f"Ваш пример: sin{random_num1} + sin{random_num2}")

# косинус
if choice2 == 1 and choice3 == 6 and choice1 == 2:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(random_num1)
        # конечный ответ
        otvet_cos_num1 = cos_num1 + random_num2
        print(f"Ваш пример: cos{random_num1} + {random_num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(random_num2)
        # конечный ответ
        otvet_cos_num2 = random_num1 + cos_num2
        print(f"Ваш пример: {random_num1} + cos{random_num2}")
    elif num_choice6 == 3:
        # конечный ответ
        cos_nums = cos(random_num1) + cos(random_num2)
        print(f"Ваш пример: cos{random_num1} + cos{random_num2}")

# оставить все как есть
if choice3 == 7 and choice2 == 1 and choice1 == 2:
    print(f"Ваш пример: {random_num1} + {random_num2}")

# ВЫЧИТАНИЕ

# степень
if choice2 == 2 and choice3 == 1 and choice1 == 2:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(random_num1, degree)
        # конечный ответ
        otvet1_in_degree = num1_in_degree - random_num2
        print(f"ваш пример: {random_num1}^{degree} - {random_num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(random_num2, degree)
        print(f"Ваш пример: {random_num1} - {random_num2}^{degree}")
        # конечный ответ
        otvet2_in_degree = random_num1 - num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        # конечный ответ
        nums_in_degree = pow(random_num1, degree) - pow(random_num2, degree)
        print(f"Ваш пример: {random_num1}^{degree} - {random_num2}^{degree}")

# извлечение корня
if choice2 == 2 and choice3 == 2 and choice1 == 2:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(random_num1)
        print(f"Ваш пример: ↓▬{random_num1} - {random_num2}")
        # конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 - random_num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(random_num2)
        print(f"Ваш пример: {random_num1} - ↓▬{random_num2}")
        # конечный ответ
        otvet_in_root_extraction2 = random_num1 - root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(random_num1) - sqrt(random_num2)
        print(f"Ваш пример: ↓▬{random_num1} - ↓▬{random_num2}")
        # конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

# модуль
if choice2 == 2 and choice3 == 3 and choice1 == 2:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        # конечный ответ
        otvet_in_module1 = abs(random_num1) - random_num2
        print(f"Ваш пример: |{random_num1}| - {random_num2}")
    if num_choice3 == 2:
        module_num2 = abs(random_num2)
        # конечный ответ
        otvet_in_module2 = random_num1 - abs(random_num2)
        print(f"Ваш пример: {random_num1} - |{random_num2}|")
    if num_choice3 == 3:
        module_nums = abs(random_num1) - abs(random_num2)
        # конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{random_num1}| - |{random_num2}|")

# логарифм
if choice2 == 2 and choice3 == 4 and choice1 == 2:
    print("Из какого числа хотите совершить логарифм?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num1 = log(random_num1, base) - random_num2
        print(f"Ваш пример: log{base}^{random_num1} - {random_num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num2 = random_num1 - log(random_num2, base)
        print(f"Ваш пример: {random_num1} - log{base}^{random_num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log(random_num1, base) - log(random_num2, base)
        # конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{random_num1} - log{base}^{random_num2}")

# синус
if choice2 == 2 and choice3 == 5 and choice1 == 2:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(random_num1)
        # конечный ответ
        otvet_sin_num1 = sin_num1 - random_num2
        print(f"Ваш пример: sin{random_num1} - {random_num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(random_num2)
        # конечный ответ
        otvet_sin_num2 = random_num1 - sin_num2
        print(f"Ваш пример: {random_num1} - sin{random_num2}")
    elif num_choice5 == 3:
        # конечный ответ
        sin_nums = sin(random_num1) - sin(random_num2)
        print(f"Ваш пример: sin{random_num1} - sin{random_num2}")

# косинус
if choice2 == 2 and choice3 == 6 and choice1 == 2:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(random_num1)
        # конечный ответ
        otvet_cos_num1 = cos_num1 - random_num2
        print(f"Ваш пример: cos{random_num1} - {random_num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(random_num2)
        # конечный ответ
        otvet_cos_num2 = random_num1 - cos_num2
        print(f"Ваш пример: {random_num1} - cos{random_num2}")
    elif num_choice6 == 3:
        # конечный ответ
        cos_nums = cos(random_num1) - cos(random_num2)
        print(f"Ваш пример: cos{random_num1} - cos{random_num2}")

# оставить все как есть
if choice3 == 7 and choice2 == 2 and choice1 == 2:
    print(f"Ваш пример: {random_num1} - {random_num2}")

# УМНОЖЕНИЕ

# степень
if choice2 == 3 and choice3 == 1 and choice1 == 2:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(random_num1, degree)
        # конечный ответ
        otvet1_in_degree = num1_in_degree * random_num2
        print(f"ваш пример: {random_num1}^{degree} * {random_num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(random_num2, degree)
        print(f"Ваш пример: {random_num1} * {random_num2}^{degree}")
        # конечный ответ
        otvet2_in_degree = random_num1 * num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        # конечный ответ
        nums_in_degree = pow(random_num1, degree) * pow(random_num2, degree)
        print(f"Ваш пример: {random_num1}^{degree} * {random_num2}^{degree}")

# извлечение корня
if choice2 == 3 and choice3 == 2 and choice1 == 2:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(random_num1)
        print(f"Ваш пример: ↓▬{random_num1} * {random_num2}")
        # конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 - random_num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(random_num2)
        print(f"Ваш пример: {random_num1} * ↓▬{random_num2}")
        # конечный ответ
        otvet_in_root_extraction2 = random_num1 * root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(random_num1) * sqrt(random_num2)
        print(f"Ваш пример: ↓▬{random_num1} * ↓▬{random_num2}")
        # конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

# модуль
if choice2 == 3 and choice3 == 3 and choice1 == 2:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        # конечный ответ
        otvet_in_module1 = abs(random_num1) * random_num2
        print(f"Ваш пример: |{random_num1}| * {random_num2}")
    if num_choice3 == 2:
        # конечный ответ
        otvet_in_module2 = random_num1 * abs(random_num2)
        print(f"Ваш пример: {random_num1} * |{random_num2}|")
    if num_choice3 == 3:
        module_nums = abs(random_num1) * abs(random_num2)
        # конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{random_num1}| * |{random_num2}|")

# логарифм
if choice2 == 3 and choice3 == 4 and choice1 == 2:
    print("Из какого числа хотите совершить логарифм?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num1 = log(random_num1, base) * random_num2
        print(f"Ваш пример: log{base}^{random_num1} * {random_num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num2 = random_num1 * log(random_num2, base)
        print(f"Ваш пример: {random_num1} * log{base}^{random_num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log(random_num1, base) * log(random_num2, base)
        # конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{random_num1} * log{base}^{random_num2}")

# синус
if choice2 == 3 and choice3 == 5 and choice1 == 2:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(random_num1)
        # конечный ответ
        otvet_sin_num1 = sin_num1 * random_num2
        print(f"Ваш пример: sin{random_num1} * {random_num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(random_num2)
        # конечный ответ
        otvet_sin_num2 = random_num1 * sin_num2
        print(f"Ваш пример: {random_num1} * sin{random_num2}")
    elif num_choice5 == 3:
        # конечный ответ
        sin_nums = sin(random_num1) * sin(random_num2)
        print(f"Ваш пример: sin{random_num1} * sin{random_num2}")

# косинус
if choice2 == 3 and choice3 == 6 and choice1 == 2:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(random_num1)
        # конечный ответ
        otvet_cos_num1 = cos_num1 * random_num2
        print(f"Ваш пример: cos{random_num1} * {random_num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(random_num2)
        # конечный ответ
        otvet_cos_num2 = random_num1 * cos_num2
        print(f"Ваш пример: {random_num1} * cos{random_num2}")
    elif num_choice6 == 3:
        # конечный ответ
        cos_nums = cos(random_num1) * cos(random_num2)
        print(f"Ваш пример: cos{random_num1} * cos{random_num2}")

# оставить все как есть
if choice3 == 7 and choice2 == 3 and choice1 == 2:
    print(f"Ваш пример: {random_num1} * {random_num2}")

# ДЕЛЕНИЕ

# степень
if choice2 == 4 and choice3 == 1 and choice1 == 2:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(random_num1, degree)
        # конечный ответ
        otvet1_in_degree = num1_in_degree / random_num2
        print(f"ваш пример: {random_num1}^{degree} : {random_num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(random_num2, degree)
        print(f"Ваш пример: {random_num1} : {random_num2}^{degree}")
        # конечный ответ
        otvet2_in_degree = random_num1 / num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        # конечный ответ
        nums_in_degree = pow(random_num1, degree) / pow(random_num2, degree)
        print(f"Ваш пример: {random_num1}^{degree} : {random_num2}^{degree}")

# извлечение корня
if choice2 == 4 and choice3 == 2 and choice1 == 2:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(random_num1)
        print(f"Ваш пример: ↓▬{random_num1} : {random_num2}")
        # конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 / random_num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(random_num2)
        print(f"Ваш пример: {random_num1} : ↓▬{random_num2}")
        # конечный ответ
        otvet_in_root_extraction2 = random_num1 / root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(random_num1) / sqrt(random_num2)
        print(f"Ваш пример: ↓▬{random_num1} : ↓▬{random_num2}")
        # конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

# модуль
if choice2 == 3 and choice3 == 3 and choice1 == 2:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        # конечный ответ
        otvet_in_module1 = abs(random_num1) / random_num2
        print(f"Ваш пример: |{random_num1}| : {random_num2}")
    if num_choice3 == 2:
        # конечный ответ
        otvet_in_module2 = random_num1 / abs(random_num2)
        print(f"Ваш пример: {random_num1} : |{random_num2}|")
    if num_choice3 == 3:
        module_nums = abs(random_num1) / abs(random_num2)
        # конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{random_num1}| : |{random_num2}|")

# логарифм
if choice2 == 4 and choice3 == 4 and choice1 == 2:
    print("Из какого числа хотите совершить логарифм?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num1 = log(random_num1, base) / random_num2
        print(f"Ваш пример: log{base}^{random_num1} : {random_num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        # конечный ответ
        otvet_log_num2 = random_num1 / log(random_num2, base)
        print(f"Ваш пример: {random_num1} : log{base}^{random_num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log(random_num1, base) / log(random_num2, base)
        # конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{random_num1} : log{base}^{random_num2}")

# синус
if choice2 == 4 and choice3 == 5 and choice1 == 2:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(random_num1)
        # конечный ответ
        otvet_sin_num1 = sin_num1 / random_num2
        print(f"Ваш пример: sin{random_num1} : {random_num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(random_num2)
        # конечный ответ
        otvet_sin_num2 = random_num1 / sin_num2
        print(f"Ваш пример: {random_num1} : sin{random_num2}")
    elif num_choice5 == 3:
        # конечный ответ
        sin_nums = sin(random_num1) / sin(random_num2)
        print(f"Ваш пример: sin{random_num1} : sin{random_num2}")

# косинус
if choice2 == 4 and choice3 == 6 and choice1 == 2:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(random_num1)
        otvet_cos_num1 = cos_num1 / random_num2
        print(f"Ваш пример: cos{random_num1} : {random_num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(random_num2)
        otvet_cos_num2 = random_num1 / cos_num2
        print(f"Ваш пример: {random_num1} : cos{random_num2}")
    elif num_choice6 == 3:
        cos_nums = cos(random_num1) / cos(random_num2)
        print(f"Ваш пример: cos{random_num1} : cos{random_num2}")

# оставить все как есть
if choice3 == 7 and choice2 == 4 and choice1 == 2:
    print(f"Ваш пример: {random_num1} : {random_num2}")

# Вывод ответов

# Числа пользователя

# Сложение

# степень
if choice1 == 1 and choice2 == 1 and choice3 == 1 and num_choice1 == 1:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 1 and choice2 == 1 and choice3 == 1 and num_choice1 == 2:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 1 and choice2 == 1 and choice3 == 1 and num_choice1 == 3:
    print(f"Ваш ответ: {nums_in_degree}")

# корень
if choice1 == 1 and choice2 == 1 and choice3 == 2 and num_choice2 == 1:
    print(f"Ваш ответ: {otvet_in_root_extraction1}")
elif choice1 == 1 and choice2 == 1 and choice3 == 2 and num_choice2 == 2:
    print(f"Ваш ответ: {otvet_in_root_extraction2}")
elif choice1 == 1 and choice2 == 1 and choice3 == 2 and num_choice2 == 3:
    print(f"Ваш ответ: {root_extraction_nums}")

# модуль
if choice1 == 1 and choice2 == 1 and choice3 == 3 and num_choice3 == 1:
    print(f"Ваш ответ: {otvet_in_module1}")
elif choice1 == 1 and choice2 == 1 and choice3 == 3 and num_choice3 == 2:
    print(f"Ваш ответ: {otvet_in_module2}")
elif choice1 == 1 and choice2 == 1 and choice3 == 3 and num_choice3 == 3:
    print(f"Ваш ответ: {otvet_in_module3}")

# логарифм
if choice1 == 1 and choice2 == 1 and choice3 == 4 and num_choice4 == 1:
    print(f"Ваш ответ: {otvet_log_num1}")
elif choice1 == 1 and choice2 == 1 and choice3 == 4 and num_choice4 == 2:
    print(f"Ваш ответ: {otvet_log_num2}")
elif choice1 == 1 and choice2 == 1 and choice3 == 4 and num_choice4 == 3:
    print(f"Ваш ответ: {otvet_log_num3}")

# синус
if choice1 == 1 and choice2 == 1 and choice3 == 5 and num_choice5 == 1:
    print(f"Ваш ответ: {sin_num1}")
elif choice1 == 1 and choice2 == 1 and choice3 == 5 and num_choice5 == 2:
    print(f"Ваш ответ: {sin_num2}")
elif choice1 == 1 and choice2 == 1 and choice3 == 5 and num_choice5 == 3:
    print(f"Ваш ответ: {sin_nums}")

# косинус
if choice1 == 1 and choice2 == 1 and choice3 == 6 and num_choice6 == 1:
    print(f"Ваш ответ: {otvet_cos_num1}")
elif choice1 == 1 and choice2 == 1 and choice3 == 6 and num_choice6 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 1 and choice2 == 1 and choice3 == 6 and num_choice6 == 3:
    print(f"Ваш ответ: {cos_nums}")

# оставить все как есть
if choice1 == 1 and choice2 == 1 and choice3 == 7:
    sum_nums = num1 + num2
    print(f"Ваш ответ: {sum_nums}")

# Вычитание

# степень
if choice1 == 1 and choice2 == 2 and choice3 == 1 and num_choice1 == 1:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 1 and choice2 == 2 and choice3 == 1 and num_choice1 == 2:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 1 and choice2 == 2 and choice3 == 1 and num_choice1 == 3:
    print(f"Ваш ответ: {nums_in_degree}")

# корень
if choice1 == 1 and choice2 == 2 and choice3 == 2 and num_choice2 == 1:
    print(f"Ваш ответ: {otvet_in_root_extraction1}")
elif choice1 == 1 and choice2 == 2 and choice3 == 2 and num_choice2 == 2:
    print(f"Ваш ответ: {otvet_in_root_extraction2}")
elif choice1 == 1 and choice2 == 2 and choice3 == 2 and num_choice2 == 3:
    print(f"Ваш ответ: {root_extraction_nums}")

# модуль
if choice1 == 1 and choice2 == 2 and choice3 == 3 and num_choice3 == 1:
    print(f"Ваш ответ: {otvet_in_module1}")
elif choice1 == 1 and choice2 == 2 and choice3 == 3 and num_choice3 == 2:
    print(f"Ваш ответ: {otvet_in_module2}")
elif choice1 == 1 and choice2 == 2 and choice3 == 3 and num_choice3 == 3:
    print(f"Ваш ответ: {otvet_in_module3}")

# логарифм
if choice1 == 1 and choice2 == 2 and choice3 == 4 and num_choice4 == 1:
    print(f"Ваш ответ: {otvet_log_num1}")
elif choice1 == 1 and choice2 == 2 and choice3 == 4 and num_choice4 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 1 and choice2 == 2 and choice3 == 4 and num_choice4 == 3:
    print(f"Ваш ответ: {otvet_log_num3}")

# синус
if choice1 == 1 and choice2 == 2 and choice3 == 5 and num_choice5 == 1:
    print(f"Ваш ответ: {sin_num1}")
elif choice1 == 1 and choice2 == 2 and choice3 == 5 and num_choice5 == 2:
    print(f"Ваш ответ: {sin_num2}")
elif choice1 == 1 and choice2 == 2 and choice3 == 5 and num_choice5 == 3:
    print(f"Ваш ответ: {sin_nums}")

# косинус
if choice1 == 1 and choice2 == 2 and choice3 == 6 and num_choice6 == 1:
    print(f"Ваш ответ: {otvet_cos_num1}")
elif choice1 == 1 and choice2 == 2 and choice3 == 6 and num_choice6 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 1 and choice2 == 2 and choice3 == 6 and num_choice6 == 3:
    print(f"Ваш ответ: {cos_nums}")

# оставить все как есть
if choice1 == 1 and choice2 == 2 and choice3 == 7:
    subtraction_nums = num1 - num2
    print(f"Ваш ответ: {subtraction_nums}")

# Умножение

# степень
if choice1 == 1 and choice2 == 3 and choice3 == 1 and num_choice1 == 1:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 1 and choice2 == 3 and choice3 == 1 and num_choice1 == 2:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 1 and choice2 == 3 and choice3 == 1 and num_choice1 == 3:
    print(f"Ваш ответ: {nums_in_degree}")

# корень
if choice1 == 1 and choice2 == 3 and choice3 == 2 and num_choice2 == 1:
    print(f"Ваш ответ: {otvet_in_root_extraction1}")
elif choice1 == 1 and choice2 == 3 and choice3 == 2 and num_choice2 == 2:
    print(f"Ваш ответ: {otvet_in_root_extraction2}")
elif choice1 == 1 and choice2 == 3 and choice3 == 2 and num_choice2 == 3:
    print(f"Ваш ответ: {root_extraction_nums}")

# модуль
if choice1 == 1 and choice2 == 3 and choice3 == 3 and num_choice3 == 1:
    print(f"Ваш ответ: {otvet_in_module1}")
elif choice1 == 1 and choice2 == 3 and choice3 == 3 and num_choice3 == 2:
    print(f"Ваш ответ: {otvet_in_module2}")
elif choice1 == 1 and choice2 == 3 and choice3 == 3 and num_choice3 == 3:
    print(f"Ваш ответ: {otvet_in_module3}")

# логарифм
if choice1 == 1 and choice2 == 3 and choice3 == 4 and num_choice4 == 1:
    print(f"Ваш ответ: {otvet_log_num1}")
elif choice1 == 1 and choice2 == 3 and choice3 == 4 and num_choice4 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 1 and choice2 == 3 and choice3 == 4 and num_choice4 == 3:
    print(f"Ваш ответ: {otvet_log_num3}")

# синус
if choice1 == 1 and choice2 == 3 and choice3 == 5 and num_choice5 == 1:
    print(f"Ваш ответ: {sin_num1}")
elif choice1 == 1 and choice2 == 3 and choice3 == 5 and num_choice5 == 2:
    print(f"Ваш ответ: {sin_num2}")
elif choice1 == 1 and choice2 == 3 and choice3 == 5 and num_choice5 == 3:
    print(f"Ваш ответ: {sin_nums}")

# косинус
if choice1 == 1 and choice2 == 3 and choice3 == 6 and num_choice6 == 1:
    print(f"Ваш ответ: {otvet_cos_num1}")
elif choice1 == 1 and choice2 == 3 and choice3 == 6 and num_choice6 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 1 and choice2 == 3 and choice3 == 6 and num_choice6 == 3:
    print(f"Ваш ответ: {cos_nums}")

# оставить все как есть
if choice1 == 1 and choice2 == 3 and choice3 == 7:
    multiplication_nums = num1 * num2
    print(f"Ваш ответ: {multiplication_nums}")

# Деление

# степень
if choice1 == 1 and choice2 == 4 and choice3 == 1 and num_choice1 == 1:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 1 and choice2 == 4 and choice3 == 1 and num_choice1 == 2:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 1 and choice2 == 4 and choice3 == 1 and num_choice1 == 3:
    print(f"Ваш ответ: {nums_in_degree}")

# корень
if choice1 == 1 and choice2 == 4 and choice3 == 2 and num_choice2 == 1:
    print(f"Ваш ответ: {otvet_in_root_extraction1}")
elif choice1 == 1 and choice2 == 4 and choice3 == 2 and num_choice2 == 2:
    print(f"Ваш ответ: {otvet_in_root_extraction2}")
elif choice1 == 1 and choice2 == 4 and choice3 == 2 and num_choice2 == 3:
    print(f"Ваш ответ: {root_extraction_nums}")

# модуль
if choice1 == 1 and choice2 == 4 and choice3 == 3 and num_choice3 == 1:
    print(f"Ваш ответ: {otvet_in_module1}")
elif choice1 == 1 and choice2 == 4 and choice3 == 3 and num_choice3 == 2:
    print(f"Ваш ответ: {otvet_in_module2}")
elif choice1 == 1 and choice2 == 4 and choice3 == 3 and num_choice3 == 3:
    print(f"Ваш ответ: {otvet_in_module3}")

# логарифм
if choice1 == 1 and choice2 == 4 and choice3 == 4 and num_choice4 == 1:
    print(f"Ваш ответ: {otvet_log_num1}")
elif choice1 == 1 and choice2 == 4 and choice3 == 4 and num_choice4 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 1 and choice2 == 4 and choice3 == 4 and num_choice4 == 3:
    print(f"Ваш ответ: {otvet_log_num3}")

# синус
if choice1 == 1 and choice2 == 4 and choice3 == 5 and num_choice5 == 1:
    print(f"Ваш ответ: {sin_num1}")
elif choice1 == 1 and choice2 == 4 and choice3 == 5 and num_choice5 == 2:
    print(f"Ваш ответ: {sin_num2}")
elif choice1 == 1 and choice2 == 4 and choice3 == 5 and num_choice5 == 3:
    print(f"Ваш ответ: {sin_nums}")

# косинус
if choice1 == 1 and choice2 == 4 and choice3 == 6 and num_choice6 == 1:
    print(f"Ваш ответ: {otvet_cos_num1}")
elif choice1 == 1 and choice2 == 4 and choice3 == 6 and num_choice6 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 1 and choice2 == 4 and choice3 == 6 and num_choice6 == 3:
    print(f"Ваш ответ: {cos_nums}")

# оставить все как есть
if choice1 == 1 and choice2 == 4 and choice3 == 7:
    division_nums = num1 / num2
    print(f"Ваш ответ: {division_nums}")

# Рандомные числа

# Сложение

# степень
if choice1 == 2 and choice2 == 1 and choice3 == 1 and num_choice1 == 1:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 2 and choice2 == 1 and choice3 == 1 and num_choice1 == 2:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 2 and choice2 == 1 and choice3 == 1 and num_choice1 == 3:
    print(f"Ваш ответ: {nums_in_degree}")

# корень
if choice1 == 2 and choice2 == 1 and choice3 == 2 and num_choice2 == 1:
    print(f"Ваш ответ: {otvet_in_root_extraction1}")
elif choice1 == 2 and choice2 == 1 and choice3 == 2 and num_choice2 == 2:
    print(f"Ваш ответ: {otvet_in_root_extraction2}")
elif choice1 == 2 and choice2 == 1 and choice3 == 2 and num_choice2 == 3:
    print(f"Ваш ответ: {root_extraction_nums}")

# модуль
if choice1 == 2 and choice2 == 1 and choice3 == 3 and num_choice3 == 1:
    print(f"Ваш ответ: {otvet_in_module1}")
elif choice1 == 2 and choice2 == 1 and choice3 == 3 and num_choice3 == 2:
    print(f"Ваш ответ: {otvet_in_module2}")
elif choice1 == 2 and choice2 == 1 and choice3 == 3 and num_choice3 == 3:
    print(f"Ваш ответ: {otvet_in_module3}")

# логарифм
if choice1 == 2 and choice2 == 1 and choice3 == 4 and num_choice4 == 1:
    print(f"Ваш ответ: {otvet_log_num1}")
elif choice1 == 2 and choice2 == 1 and choice3 == 4 and num_choice4 == 2:
    print(f"Ваш ответ: {otvet_log_num2}")
elif choice1 == 2 and choice2 == 1 and choice3 == 4 and num_choice4 == 3:
    print(f"Ваш ответ: {otvet_log_num3}")

# синус
if choice1 == 2 and choice2 == 1 and choice3 == 5 and num_choice5 == 1:
    print(f"Ваш ответ: {sin_num1}")
elif choice1 == 2 and choice2 == 1 and choice3 == 5 and num_choice5 == 2:
    print(f"Ваш ответ: {sin_num2}")
elif choice1 == 2 and choice2 == 1 and choice3 == 5 and num_choice5 == 3:
    print(f"Ваш ответ: {sin_nums}")

# косинус
if choice1 == 2 and choice2 == 1 and choice3 == 6 and num_choice6 == 1:
    print(f"Ваш ответ: {otvet_cos_num1}")
elif choice1 == 2 and choice2 == 1 and choice3 == 6 and num_choice6 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 2 and choice2 == 1 and choice3 == 6 and num_choice6 == 3:
    print(f"Ваш ответ: {cos_nums}")

# оставить все как есть
if choice1 == 2 and choice2 == 1 and choice3 == 7:
    sum_nums = num1 + num2
    print(f"Ваш ответ: {sum_nums}")

# Вычитание

# степень
if choice1 == 2 and choice2 == 2 and choice3 == 1 and num_choice1 == 1:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 2 and choice2 == 2 and choice3 == 1 and num_choice1 == 2:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 2 and choice2 == 2 and choice3 == 1 and num_choice1 == 3:
    print(f"Ваш ответ: {nums_in_degree}")

# корень
if choice1 == 2 and choice2 == 2 and choice3 == 2 and num_choice2 == 1:
    print(f"Ваш ответ: {otvet_in_root_extraction1}")
elif choice1 == 2 and choice2 == 2 and choice3 == 2 and num_choice2 == 2:
    print(f"Ваш ответ: {otvet_in_root_extraction2}")
elif choice1 == 2 and choice2 == 2 and choice3 == 2 and num_choice2 == 3:
    print(f"Ваш ответ: {root_extraction_nums}")

# модуль
if choice1 == 2 and choice2 == 2 and choice3 == 3 and num_choice3 == 1:
    print(f"Ваш ответ: {otvet_in_module1}")
elif choice1 == 2 and choice2 == 2 and choice3 == 3 and num_choice3 == 2:
    print(f"Ваш ответ: {otvet_in_module2}")
elif choice1 == 2 and choice2 == 2 and choice3 == 3 and num_choice3 == 3:
    print(f"Ваш ответ: {otvet_in_module3}")

# логарифм
if choice1 == 2 and choice2 == 2 and choice3 == 4 and num_choice4 == 1:
    print(f"Ваш ответ: {otvet_log_num1}")
elif choice1 == 2 and choice2 == 2 and choice3 == 4 and num_choice4 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 2 and choice2 == 2 and choice3 == 4 and num_choice4 == 3:
    print(f"Ваш ответ: {otvet_log_num3}")

# синус
if choice1 == 2 and choice2 == 2 and choice3 == 5 and num_choice5 == 1:
    print(f"Ваш ответ: {sin_num1}")
elif choice1 == 2 and choice2 == 2 and choice3 == 5 and num_choice5 == 2:
    print(f"Ваш ответ: {sin_num2}")
elif choice1 == 2 and choice2 == 2 and choice3 == 5 and num_choice5 == 3:
    print(f"Ваш ответ: {sin_nums}")

# косинус
if choice1 == 2 and choice2 == 2 and choice3 == 6 and num_choice6 == 1:
    print(f"Ваш ответ: {otvet_cos_num1}")
elif choice1 == 2 and choice2 == 2 and choice3 == 6 and num_choice6 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 2 and choice2 == 2 and choice3 == 6 and num_choice6 == 3:
    print(f"Ваш ответ: {cos_nums}")

# оставить все как есть
if choice1 == 2 and choice2 == 2 and choice3 == 7:
    subtraction_nums = num1 - num2
    print(f"Ваш ответ: {subtraction_nums}")

# Умножение

# степень
if choice1 == 2 and choice2 == 3 and choice3 == 1 and num_choice1 == 1:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 2 and choice2 == 3 and choice3 == 1 and num_choice1 == 2:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 2 and choice2 == 3 and choice3 == 1 and num_choice1 == 3:
    print(f"Ваш ответ: {nums_in_degree}")

# корень
if choice1 == 2 and choice2 == 3 and choice3 == 2 and num_choice2 == 1:
    print(f"Ваш ответ: {otvet_in_root_extraction1}")
elif choice1 == 2 and choice2 == 3 and choice3 == 2 and num_choice2 == 2:
    print(f"Ваш ответ: {otvet_in_root_extraction2}")
elif choice1 == 2 and choice2 == 3 and choice3 == 2 and num_choice2 == 3:
    print(f"Ваш ответ: {root_extraction_nums}")

# модуль
if choice1 == 2 and choice2 == 3 and choice3 == 3 and num_choice3 == 1:
    print(f"Ваш ответ: {otvet_in_module1}")
elif choice1 == 2 and choice2 == 3 and choice3 == 3 and num_choice3 == 2:
    print(f"Ваш ответ: {otvet_in_module2}")
elif choice1 == 2 and choice2 == 3 and choice3 == 3 and num_choice3 == 3:
    print(f"Ваш ответ: {otvet_in_module3}")

# логарифм
if choice1 == 2 and choice2 == 3 and choice3 == 4 and num_choice4 == 1:
    print(f"Ваш ответ: {otvet_log_num1}")
elif choice1 == 2 and choice2 == 3 and choice3 == 4 and num_choice4 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 2 and choice2 == 3 and choice3 == 4 and num_choice4 == 3:
    print(f"Ваш ответ: {otvet_log_num3}")

# синус
if choice1 == 2 and choice2 == 3 and choice3 == 5 and num_choice5 == 1:
    print(f"Ваш ответ: {sin_num1}")
elif choice1 == 2 and choice2 == 3 and choice3 == 5 and num_choice5 == 2:
    print(f"Ваш ответ: {sin_num2}")
elif choice1 == 2 and choice2 == 3 and choice3 == 5 and num_choice5 == 3:
    print(f"Ваш ответ: {sin_nums}")

# косинус
if choice1 == 2 and choice2 == 3 and choice3 == 6 and num_choice6 == 1:
    print(f"Ваш ответ: {otvet_cos_num1}")
elif choice1 == 2 and choice2 == 3 and choice3 == 6 and num_choice6 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 2 and choice2 == 3 and choice3 == 6 and num_choice6 == 3:
    print(f"Ваш ответ: {cos_nums}")

# оставить все как есть
if choice1 == 2 and choice2 == 3 and choice3 == 7:
    multiplication_nums = num1 * num2
    print(f"Ваш ответ: {multiplication_nums}")

# Деление

# степень
if choice1 == 2 and choice2 == 4 and choice3 == 1 and num_choice1 == 1:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 2 and choice2 == 4 and choice3 == 1 and num_choice1 == 2:
    print(f"Ваш ответ: {otvet1_in_degree}")
elif choice1 == 2 and choice2 == 4 and choice3 == 1 and num_choice1 == 3:
    print(f"Ваш ответ: {nums_in_degree}")

# корень
if choice1 == 2 and choice2 == 4 and choice3 == 2 and num_choice2 == 1:
    print(f"Ваш ответ: {otvet_in_root_extraction1}")
elif choice1 == 2 and choice2 == 4 and choice3 == 2 and num_choice2 == 2:
    print(f"Ваш ответ: {otvet_in_root_extraction2}")
elif choice1 == 2 and choice2 == 4 and choice3 == 2 and num_choice2 == 3:
    print(f"Ваш ответ: {root_extraction_nums}")

# модуль
if choice1 == 2 and choice2 == 4 and choice3 == 3 and num_choice3 == 1:
    print(f"Ваш ответ: {otvet_in_module1}")
elif choice1 == 2 and choice2 == 4 and choice3 == 3 and num_choice3 == 2:
    print(f"Ваш ответ: {otvet_in_module2}")
elif choice1 == 2 and choice2 == 4 and choice3 == 3 and num_choice3 == 3:
    print(f"Ваш ответ: {otvet_in_module3}")

# логарифм
if choice1 == 2 and choice2 == 4 and choice3 == 4 and num_choice4 == 1:
    print(f"Ваш ответ: {otvet_log_num1}")
elif choice1 == 2 and choice2 == 4 and choice3 == 4 and num_choice4 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 2 and choice2 == 4 and choice3 == 4 and num_choice4 == 3:
    print(f"Ваш ответ: {otvet_log_num3}")

# синус
if choice1 == 2 and choice2 == 4 and choice3 == 5 and num_choice5 == 1:
    print(f"Ваш ответ: {sin_num1}")
elif choice1 == 2 and choice2 == 4 and choice3 == 5 and num_choice5 == 2:
    print(f"Ваш ответ: {sin_num2}")
elif choice1 == 2 and choice2 == 4 and choice3 == 5 and num_choice5 == 3:
    print(f"Ваш ответ: {sin_nums}")

# косинус
if choice1 == 2 and choice2 == 4 and choice3 == 6 and num_choice6 == 1:
    print(f"Ваш ответ: {otvet_cos_num1}")
elif choice1 == 2 and choice2 == 4 and choice3 == 6 and num_choice6 == 2:
    print(f"Ваш ответ: {otvet_cos_num2}")
elif choice1 == 2 and choice2 == 4 and choice3 == 6 and num_choice6 == 3:
    print(f"Ваш ответ: {cos_nums}")

# оставить все как есть
if choice1 == 2 and choice2 == 4 and choice3 == 7:
    division_nums = num1 / num2
    print(f"Ваш ответ: {division_nums}")
