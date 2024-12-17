from random import randint


def med():
    syr = [randint(1, 50) for i in range(7)]
    print(syr)
    return sorted(syr, key=lambda x: x % 10)


print(med())
