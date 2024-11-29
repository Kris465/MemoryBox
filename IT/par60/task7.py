from random import randint


def cubes():
    cube1 = randint(1, 7)
    cube2 = randint(1, 7)
    return cube1, cube2


print(cubes())
