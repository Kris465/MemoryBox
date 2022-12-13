# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def points_in_square():
    part = int(input("Input the number of the square: "))

    # Код с четвертями, начиная с правой верхней четверти где x > и y > 0, и далее по часовой стрелке (по ответам из прошлого задания)

    if part == 1:
        print("x is from 0 to infinite, y is from 0 to infinite")
    elif part == 2:
        print("x is from -infinite to 0, y is from 0 to infinite")
    elif part == 3:
        print("x is from -infinite to 0, y is from -infinite to 0")
    elif part == 4:
        print("x is from 0 to infinite, y is from -infinite to 0")


points_in_square()