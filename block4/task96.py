import math


def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f'Два вещественных корня: {root1:.2f}, {root2:.2f}'
    elif discriminant == 0:
        root = -b / (2*a)
        return f'Один вещественный корень: {root:.2f}'
    else:
        return 'Вещественных корней нет.'


a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))


result = quadratic_roots(a, b, c)
print(result)
