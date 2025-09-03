# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

def points_in_square():
    part = int(input("Input the number of the square: "))

    if part == 1:
        print("x > 0 and y > 0")
    elif part == 2:
        print("x < 0 and y > 0")
    elif part == 3:
        print("x < 0 and y < 0")
    elif part == 4:
        print("x > 0 and y < 0")
    else: print("Error, try again.")

points_in_square()