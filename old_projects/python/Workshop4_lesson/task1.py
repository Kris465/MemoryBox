# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
    
#     2) с помощью дополнительных библиотек Python
    
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# st = input().split()
# nums = list(map(int, st))
# print(nums)

# nums = list(map(int, input().split()))

# def max_min():
#     max_ = 0
#     min_ = nums[0]
#     for i in nums[0:]:
#         if max_ > nums[i]:
#             max_ = nums[i]
#         elif min_ < nums[i]:
#             min_ = nums[i]

# max_min()

def third_task():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))

    mult = num1 * num2
    try_num = mult - 1

    while try_num != 0:
        if try_num % num1 == 0 and try_num % num2 == 0:
            mult = try_num
            try_num -= 1
        else:
            try_num -= 1
    print(mult)

third_task()


# nums = list(map(int, input('введите числа:').split()))

# max_ = 0
# min_ = nums[0]

# for i in nums[0:]:
#     if i > max_:
#         max_ = i
#     elif i < min_:
#         min_ = i
# print(min_)
# print(max_)

# num_1 = int(input('введите число:'))
# num_2 = int(input('введите число:'))

# i = min(num_1, num_2)

# while True:
#     if i % num_1 == 0 and i % num_2 == 0:
#         break
#     i += 1
# print(i)

import math

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
res = math.lcm(a, b)
print(f'НОК =', res)
