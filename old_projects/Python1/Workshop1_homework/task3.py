# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def square_part(): 
    x = int(input("Input x: "))
    y = int(input("Input y: "))

    if x > 0 and y > 0:
        print(f"Your part is 1")
    elif x > 0 and y < 0:
        print(f"Your part is 4")
    elif x < 0 and y < 0:
        print(f"Your part is 3")
    elif x < 0 and y > 0:
        print(f"Your part is 2")
    else: print("Try again, plese.")

square_part()
