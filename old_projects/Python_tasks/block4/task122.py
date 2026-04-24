a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
if a + b > c and a + c > b and b + c > a:
    print("Можно сделать треугольник")
else:
    print("Нельзя сделать треугольник")
