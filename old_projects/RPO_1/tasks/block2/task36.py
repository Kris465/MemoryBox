a3 = int(input("12345"))
a2 = int(input("a2"))
a1 = int(input("a3"))
b2 = int(input("a1"))
b1 = int(input("a2"))

A = 100 * a3 + 10 * a2 + a1
B = 10 * b2 + b1

sum_ = A + B

x3 = sum_ // 100               # сотни
x2 = (sum_ % 100) // 10        # десятки
x1 = sum_ % 10                 # единицы

print(x3)
print(x2)
print(x1)
