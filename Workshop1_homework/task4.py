# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Первая четверть: x > 0 и y > 0, вторая четверть: x < 0 и y > 0, третья четверть: x < 0 и y < 0, четвертая четверть: x > 0 и y < 0.

def x_y_value():
    part_of_square = int(input("Input the number of part: "))

    if part_of_square == 1:
        print("x is from 0 to infinite, y is from 0 to infinite")
    elif part_of_square == 2:
        print("x is from -infinite to 0, y is from 0 to infinite")
    elif part_of_square == 3:
        print("x is from -infinite to 0, y is from -infinite to 0")
    elif part_of_square == 4:
        print("x is from 0 to infinite, y is from -infinite to 0")

x_y_value()