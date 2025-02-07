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

if choice2 == 1 and choice1 == 1:
    print(f"Ваш пример: {num1} + {num2}")
elif choice2 == 2 and choice1 == 1:
    print(f"Ваш пример: {num1} - {num2}")
elif choice2 == 3 and choice1 == 1:
    print(f"Ваш пример: {num1} * {num2}")
elif choice2 == 4 and choice1 == 1:
    print(f"Ваш пример: {num1} : {num2}")


print("Выберите доп.функции: ")
print("1 - возведение в степень")
print("2 - извлечение корня")
print("3 - модуль")
print("4 - логарифм")
print("5 - синус")
print("6 - косинус")
print("7 - оставить как есть")
choice3 = int(input("Ваш выбор: "))

#СЛОЖЕНИЕ

#степень
if choice2 == 1 and choice3 == 1:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(num1, degree)
        #конечный ответ
        otvet1_in_degree = num1_in_degree + num2
        print(f"ваш пример: {num1}^{degree} + {num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(num2, degree)
        print(f"Ваш пример: {num1} + {num2}^{degree}")
        #конечный ответ
        otvet2_in_degree = num1 + num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        #конечный ответ
        nums_in_degree = pow(num1, degree) + pow(num2, degree)
        print(f"Ваш пример: {num1}^{degree} + {num2}^{degree}")

#извлечение корня
if choice2 == 1 and choice3 == 2:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(num1)
        print(f"Ваш пример: {num1}^2 + {num2}")
        #конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 + num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(num2)
        print(f"Ваш пример: {num1} + {num2}^2")
        #конечный ответ
        otvet_in_root_extraction2 = num1 + root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(num1) + sqrt(num2)
        print(f"Ваш пример: {num1}^2 + {num2}^2")
        #конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

#модуль
if choice2 == 1 and choice3 == 3:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        module_num1 = abs(num1)
        #конечный ответ
        otvet_in_module1 = module_num1 + num2
        print(f"Ваш пример: |{num1}| + {num2}")
    if num_choice3 == 2:
        module_num2 = abs(num2)
        #конечный ответ
        otvet_in_module2 = num1 + module_num2
        print(f"Ваш пример: {num1} + |{num2}|")
    if num_choice3 == 3:
        module_nums = module_num1 + module_num2
        #конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{num1}| + |{num2}|")

#логарифм    
if choice2 == 1 and choice3 == 4:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        log_num1 = log(num1, base)
        #конечный ответ
        otvet_log_num1 = log_num1 + num2
        print(f"Ваш пример: log{base}^{num1} + {num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        log_num2 = log(num2, base)
        #конечный ответ
        otvet_log_num2 = num1 + log_num2
        print(f"Ваш пример: {num1} + log{base}^{num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log_num1 + log_num2
        #конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{num1} + log{base}^{num2}")

#синус
if choice2 == 1 and choice3 == 5:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(num1)
        #конечный ответ
        otvet_sin_num1 = sin_num1 + num2
        print(f"Ваш пример: sin{num1} + {num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(num2)
        #конечный ответ
        otvet_sin_num2 = num1 + sin_num2
        print(f"Ваш пример: {num1} + sin{num2}")
    elif num_choice5 == 3:
        #конечный ответ
        sin_nums = sin(num1) + sin(num2)
        print(f"Ваш пример: sin{num1} + sin{num2}")
        
#косинус
if choice2 == 1 and choice3 == 6:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(num1)
        otvet_cos_num1 = cos_num1 + num2
        print(f"Ваш пример: cos{num1} + {num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(num2)
        otvet_cos_num2 = num1 + cos_num2
        print(f"Ваш пример: {num1} + cos{num2}")
    elif num_choice6 == 3:
        cos_nums = cos(num1) + cos(num2)
        print(f"Ваш пример: cos{num1} + cos{num2}")

#оставить все как есть
if choice3 == 7 and choice2 == 1:
    print(f"Ваш пример: {num1} + {num2}")

#ВЫЧИТАНИЕ

#степень
if choice2 == 2 and choice3 == 1:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(num1, degree)
        #конечный ответ
        otvet1_in_degree = num1_in_degree - num2
        print(f"ваш пример: {num1}^{degree} - {num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(num2, degree)
        print(f"Ваш пример: {num1} - {num2}^{degree}")
        #конечный ответ
        otvet2_in_degree = num1 - num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        #конечный ответ
        nums_in_degree = pow(num1, degree) - pow(num2, degree)
        print(f"Ваш пример: {num1}^{degree} - {num2}^{degree}")

#извлечение корня
if choice2 == 2 and choice3 == 2:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(num1)
        print(f"Ваш пример: {num1}^2 - {num2}")
        #конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 - num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(num2)
        print(f"Ваш пример: {num1} - {num2}^2")
        #конечный ответ
        otvet_in_root_extraction2 = num1 - root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(num1) - sqrt(num2)
        print(f"Ваш пример: {num1}^2 - {num2}^2")
        #конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

#модуль
if choice2 == 2 and choice3 == 3:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        module_num1 = abs(num1)
        #конечный ответ
        otvet_in_module1 = module_num1 - num2
        print(f"Ваш пример: |{num1}| - {num2}")
    if num_choice3 == 2:
        module_num2 = abs(num2)
        #конечный ответ
        otvet_in_module2 = num1 - module_num2
        print(f"Ваш пример: {num1} - |{num2}|")
    if num_choice3 == 3:
        module_nums = module_num1 - module_num2
        #конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{num1}| - |{num2}|")

#логарифм    
if choice2 == 2 and choice3 == 4:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        log_num1 = log(num1, base)
        #конечный ответ
        otvet_log_num1 = log_num1 - num2
        print(f"Ваш пример: log{base}^{num1} - {num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        log_num2 = log(num2, base)
        #конечный ответ
        otvet_log_num2 = num1 - log_num2
        print(f"Ваш пример: {num1} - log{base}^{num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log_num1 - log_num2
        #конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{num1} - log{base}^{num2}")

#синус
if choice2 == 2 and choice3 == 5:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(num1)
        #конечный ответ
        otvet_sin_num1 = sin_num1 - num2
        print(f"Ваш пример: sin{num1} - {num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(num2)
        #конечный ответ
        otvet_sin_num2 = num1 - sin_num2
        print(f"Ваш пример: {num1} - sin{num2}")
    elif num_choice5 == 3:
        #конечный ответ
        sin_nums = sin(num1) - sin(num2)
        print(f"Ваш пример: sin{num1} - sin{num2}")

#косинус
if choice2 == 2 and choice3 == 6:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(num1)
        otvet_cos_num1 = cos_num1 - num2
        print(f"Ваш пример: cos{num1} - {num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(num2)
        otvet_cos_num2 = num1 - cos_num2
        print(f"Ваш пример: {num1} - cos{num2}")
    elif num_choice6 == 3:
        cos_nums = cos(num1) - cos(num2)
        print(f"Ваш пример: cos{num1} - cos{num2}")

#оставить все как есть
if choice3 == 7 and choice2 == 2:
    print(f"Ваш пример: {num1} - {num2}")

#УМНОЖЕНИЕ

#степень
if choice2 == 3 and choice3 == 1:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(num1, degree)
        #конечный ответ
        otvet1_in_degree = num1_in_degree * num2
        print(f"ваш пример: {num1}^{degree} * {num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(num2, degree)
        print(f"Ваш пример: {num1} * {num2}^{degree}")
        #конечный ответ
        otvet2_in_degree = num1 * num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        #конечный ответ
        nums_in_degree = pow(num1, degree) * pow(num2, degree)
        print(f"Ваш пример: {num1}^{degree} * {num2}^{degree}")
        
#извлечение корня
if choice2 == 3 and choice3 == 2:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(num1)
        print(f"Ваш пример: {num1}^2 * {num2}")
        #конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 - num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(num2)
        print(f"Ваш пример: {num1} * {num2}^2")
        #конечный ответ
        otvet_in_root_extraction2 = num1 * root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(num1) * sqrt(num2)
        print(f"Ваш пример: {num1}^2 * {num2}^2")
        #конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

#модуль
if choice2 == 3 and choice3 == 3:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        module_num1 = abs(num1)
        #конечный ответ
        otvet_in_module1 = module_num1 * num2
        print(f"Ваш пример: |{num1}| * {num2}")
    if num_choice3 == 2:
        module_num2 = abs(num2)
        #конечный ответ
        otvet_in_module2 = num1 * module_num2
        print(f"Ваш пример: {num1} * |{num2}|")
    if num_choice3 == 3:
        module_nums = module_num1 * module_num2
        #конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{num1}| * |{num2}|")

#логарифм    
if choice2 == 3 and choice3 == 4:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        log_num1 = log(num1, base)
        #конечный ответ
        otvet_log_num1 = log_num1 * num2
        print(f"Ваш пример: log{base}^{num1} * {num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        log_num2 = log(num2, base)
        #конечный ответ
        otvet_log_num2 = num1 * log_num2
        print(f"Ваш пример: {num1} * log{base}^{num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log_num1 * log_num2
        #конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{num1} * log{base}^{num2}")

#синус
if choice2 == 3 and choice3 == 5:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(num1)
        #конечный ответ
        otvet_sin_num1 = sin_num1 * num2
        print(f"Ваш пример: sin{num1} * {num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(num2)
        #конечный ответ
        otvet_sin_num2 = num1 * sin_num2
        print(f"Ваш пример: {num1} * sin{num2}")
    elif num_choice5 == 3:
        #конечный ответ
        sin_nums = sin(num1) * sin(num2)
        print(f"Ваш пример: sin{num1} * sin{num2}")

#косинус
if choice2 == 3 and choice3 == 6:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice6 = int(input("Ваш выбор: "))
    if num_choice6 == 1:
        cos_num1 = cos(num1)
        otvet_cos_num1 = cos_num1 * num2
        print(f"Ваш пример: cos{num1} * {num2}")
    elif num_choice6 == 2:
        cos_num2 = cos(num2)
        otvet_cos_num2 = num1 * cos_num2
        print(f"Ваш пример: {num1} * cos{num2}")
    elif num_choice6 == 3:
        cos_nums = cos(num1) * cos(num2)
        print(f"Ваш пример: cos{num1} * cos{num2}")

#оставить все как есть
if choice3 == 7 and choice2 == 3:
    print(f"Ваш пример: {num1} * {num2}")

#ДЕЛЕНИЕ

#степень
if choice2 == 4 and choice3 == 1:
    print("Какое число вы хотите возвести в степень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice1 = int(input("Ваш выбор: "))

    if num_choice1 == 1:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num1_in_degree = pow(num1, degree)
        #конечный ответ
        otvet1_in_degree = num1_in_degree / num2
        print(f"ваш пример: {num1}^{degree} : {num2}")
    elif num_choice1 == 2:
        degree = int(input("Введите в какую степень хотите возвести: "))
        num2_in_degree = pow(num2, degree)
        print(f"Ваш пример: {num1} : {num2}^{degree}")
        #конечный ответ
        otvet2_in_degree = num1 / num2_in_degree
    elif num_choice1 == 3:
        degree = int(input("Введите в какую степень хотите возвести: "))
        #конечный ответ
        nums_in_degree = pow(num1, degree) / pow(num2, degree)
        print(f"Ваш пример: {num1}^{degree} : {num2}^{degree}")

#извлечение корня
if choice2 == 4 and choice3 == 2:
    print("Из какого числа хотите извлечь корень?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice2 = int(input("Ваш выбор: "))

    if num_choice2 == 1:
        root_extraction_num1 = sqrt(num1)
        print(f"Ваш пример: {num1}^2 : {num2}")
        #конечный ответ
        otvet_in_root_extraction1 = root_extraction_num1 / num2
    if num_choice2 == 2:
        root_extraction_num2 = sqrt(num2)
        print(f"Ваш пример: {num1} : {num2}^2")
        #конечный ответ
        otvet_in_root_extraction2 = num1 / root_extraction_num2
    if num_choice2 == 3:
        root_extraction_nums = sqrt(num1) / sqrt(num2)
        print(f"Ваш пример: {num1}^2 : {num2}^2")
        #конечный ответ
        otvet_in_root_extraction3 = root_extraction_nums

#модуль
if choice2 == 3 and choice3 == 3:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice3 = int(input("Ваш выбор: "))
    if num_choice3 == 1:
        module_num1 = abs(num1)
        #конечный ответ
        otvet_in_module1 = module_num1 / num2
        print(f"Ваш пример: |{num1}| : {num2}")
    if num_choice3 == 2:
        module_num2 = abs(num2)
        #конечный ответ
        otvet_in_module2 = num1 / module_num2
        print(f"Ваш пример: {num1} : |{num2}|")
    if num_choice3 == 3:
        module_nums = module_num1 / module_num2
        #конечный ответ
        otvet_in_module3 = module_nums
        print(f"Ваш пример: |{num1}| : |{num2}|")

#логарифм    
if choice2 == 4 and choice3 == 4:
    print("Из какого числа хотите совершить модуль?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice4 = int(input("Ваш выбор: "))
    if num_choice4 == 1:
        base = int(input("Введите основание логарифма: "))
        log_num1 = log(num1, base)
        #конечный ответ
        otvet_log_num1 = log_num1 / num2
        print(f"Ваш пример: log{base}^{num1} : {num2}")
    if num_choice4 == 2:
        base = int(input("Введите основание логарифма: "))
        log_num2 = log(num2, base)
        #конечный ответ
        otvet_log_num2 = num1 / log_num2
        print(f"Ваш пример: {num1} : log{base}^{num2}")
    if num_choice4 == 3:
        base = int(input("Введите основание логарифма: "))
        log_nums = log_num1 / log_num2
        #конечный ответ
        otvet_log_num3 = log_nums
        print(f"Ваш пример: log{base}^{num1} : log{base}^{num2}")

#синус
if choice2 == 3 and choice3 == 5:
    print("Из какого числа вы хотите сделать синус?")
    print("1 - первое число")
    print("2 - второе число")
    print("3 - оба числа")
    num_choice5 = int(input("Ваш выбор: "))
    if num_choice5 == 1:
        sin_num1 = sin(num1)
        #конечный ответ
        otvet_sin_num1 = sin_num1 / num2
        print(f"Ваш пример: sin{num1} : {num2}")
    elif num_choice5 == 2:
        sin_num2 = sin(num2)
        #конечный ответ
        otvet_sin_num2 = num1 / sin_num2
        print(f"Ваш пример: {num1} : sin{num2}")
    elif num_choice5 == 3:
        #конечный ответ
        sin_nums = sin(num1) / sin(num2)
        print(f"Ваш пример: sin{num1} : sin{num2}")
