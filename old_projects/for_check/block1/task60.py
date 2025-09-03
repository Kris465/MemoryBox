a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

b, a, c = c, b, a
print(f"а) a = {a}, b = {b}, c = {c}")

b, c, a = a, b, c
print(f"б) a = {a}, b = {b}, c = {c}")
