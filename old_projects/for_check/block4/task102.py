x = int(input("Введите число x: "))
y = int(input("Введите число y: "))


def chetvert(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4


print("Четверть:", chetvert(x, y))
