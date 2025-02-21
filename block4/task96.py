import math


def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f'два вещественных корня: {root1:.2f}, {root2:.2f}'
    elif discriminant == 0:
        root = -b / (2*a)
        return f'один вещественных корня: {root:.2f}'
    else:
        return 'Вещественных корней нет.'


a = float(input('Введите коэффицент a: '))
b = float(input('Введите коэффицент b: '))
c = float(input('Введите коэффицент c: '))


resultat = quadratic_roots(a, b, c)
print(resultat)
