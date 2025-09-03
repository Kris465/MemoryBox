# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def distance():
    x1 = float(input("Input x of the first point: "))
    y1 = float(input("Input y of the first point: "))
    x2 = float(input("Input x of the second point: "))
    y2 = float(input("Input y of hte second point: "))

    if x1 > x2:
        side1 = x1 - x2
    else: side1 = x2 - x1

    if y1 > y2:
        side2 = y1 - y2
    else: side2 = y2 - y1

    distance_is = (side1 * side1 + side2 * side2) ** (0.5)
    distance_is = round(distance_is, 3)

    print(f'The distance between points is: {distance_is}')

distance()