# Вывести на экран числа от -N до N

n = int(input("Input yout number: "))
for i in range(-n, n+1): # можно третьим аргументом указать шаг
    print(i, end = ' ') # \n - переход на новую строку
