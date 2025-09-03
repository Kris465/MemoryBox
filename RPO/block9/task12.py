a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
b, a, c = c, b, a
print(a, b, c)
b, c, a = a, b, c
print(a, b, c)
