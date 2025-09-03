def print_square_numbers(n):
    i = 1
    print("Натуральные числа, квадрат которых не превышает n: ")
    while i * i <= n:
        print(i * i)
        i +=1

n = int(input("Введите число: "))
