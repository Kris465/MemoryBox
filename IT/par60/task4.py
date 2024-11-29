num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))


def nod(num1, num2):
    spisok1 = []
    spisok2 = []
    spisok3 = []
    for i in range(1, num1):
        if num1 % i == 0:
            spisok1.append(i)
    for i in range(1, num2):
        if num2 % i == 0:
            spisok2.append(i)
    if len(spisok1) >= len(spisok2):
        for i in spisok1:
            if i in spisok2:
                spisok3.append(i)
    elif len(spisok1) <= len(spisok2):
        for i in spisok2:
            if i in spisok1:
                spisok3.append(i)
    return spisok3


print(nod(num1, num2))
