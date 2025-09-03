x = 2


S = 0


for n in range(11):

    term = (n + 1) / (n + 2) * (x ** n)

    if n % 2 != 0:
        term = -term

    S += term


print("Сумма ряда S(2) =", S)
