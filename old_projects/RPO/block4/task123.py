def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0] + sides[1] > sides[2] and abs(
        sides[0] + sides[1] - sides[2]) < 1e-9


a = float(input("Введите положительное первое вещественное число: "))
b = float(input("Введите положительное второе вещественное число: "))
c = float(input("Введите положительное третье вещественное число: "))

if is_right_triangle(a, b, c):
    print("Прямоугольный треугольник")
else:
    print("Не прямоугольный треугольник")
