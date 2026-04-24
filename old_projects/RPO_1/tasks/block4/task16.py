import math

S_circle = float(input("Введите площадь круга: "))
S_square = float(input("Введите площадь квадрата: "))

r = math.sqrt(S_circle / math.pi)
a = math.sqrt(S_square)

diameter_circle = 2 * r
fits_circle_in_square = diameter_circle <= a

diagonale_square = a * math.sqrt(2)
diameter_circle = 2 * r
fits_square_in_circle = diagonale_square <= diameter_circle

if fits_circle_in_square:
    print("Круг уместится в квадрате")
else:
    print("Круг не уместится в квадрате")
if fits_square_in_circle:
    print("Квадрат уместится в круге")
else:
    print("Квадрат не уместится в круге")
