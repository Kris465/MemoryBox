from math import sqrt

catheter1 = int(input("Введите значение первого катета: "))
catheter2 = int(input("Введите значение второго катета: "))
hypotenuse = catheter1 ** 2 + catheter2 ** 2

perimeter = catheter1 + catheter2 + sqrt(hypotenuse)
print(perimeter)
