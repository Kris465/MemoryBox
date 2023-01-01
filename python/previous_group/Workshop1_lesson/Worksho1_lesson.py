# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.  
#   *Примеры:* 
#   
#   - 5, 25 -> да
#   - 4, 16 -> да
#   - 25, 5 -> да
#   - 8,9 -> нет
# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#a = int(input("Input your number: "))
#b = int(input("Input second number: "))

#if a * a == b or b * b == a:
#    print("yes")
#else:
#    print("no")

#sp = []
#
#for i in range(1,6):
#    sp.append(i)
#print(sp)
#
#print(max(sp))

# try:
#     number1 = int(input('Введите первое число: '))
#     number2 = int(input('Введите второе число: '))
#     if number1 ** 2 == number2:
#         print(f'{number2} является квадратом числа {number1}')
#     elif number2 ** 2 == number1:
#         print(f'{number1} является квадратом числа {number2}')
#     else:
#         print('Ни одно из числе не является квадратом другого')
# except:
#     print('Введите целое число')
       
# number = int(input('...'))

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.


# def printarray(num):
#     for i in range(-num, num + 1):
#         print(i, end = ' ')
    
# printarray(number)

# def firstdigit():
#     number = float(input('...'))
#     number = number * 10
#     if number % 10 == 0:
#         print("no")
#     else: print(int(number % 10))

# firstdigit()

def divinefive():
    number = int(input('...'))
    if number % 30 == 0:
        print("no")
    elif number % 5 == 0 and number % 10 == 0 or number % 15 == 0:
        print("yes")
    else: print("Something was going wrong...")


divinefive()