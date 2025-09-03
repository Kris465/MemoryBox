from random import randint

block = randint(1, 8)
match block:
    case 1:
        print(block, randint(1, 62))
    case 2:
        print(block, randint(1, 43))
    case 3:
        print(block, randint(1, 35))
    case 4:
        print(block, randint(1, 141))
    case 5:
        print(block, randint(1, 96))
    case 6:
        print(block, randint(1, 115))
    case 7:
        print(block, randint(1, 128))
    case 8:
        print(block, randint(1, 59))
    case _:
        print("something went wrong")
