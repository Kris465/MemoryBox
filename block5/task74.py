a = float(input("Введите вещественное число a: "))
n = int(input("Введите натуральное число n: "))


current_value = a


print(current_value)


for i in range(2, n+1):
    current_value *= a
    print(current_value)
