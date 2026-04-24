def boundary_line(x):
    return 2 * x


x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

if y <= boundary_line(x):
    print("Точка попадает в область I")
else:
    print("Точка попадает в область II")
