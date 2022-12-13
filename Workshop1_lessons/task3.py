# 3. Напишите программу, которая будет на вход принимать
# число N и выводить числа от -N до N

def range_numbers_n():
    n = int(input("Input your number: "))
    print(*range(-n, n + 1))

range_numbers_n()