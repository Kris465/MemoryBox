

def bisection_method(f, a, b, eps=0.001):
    """ Метод деления отрезка пополам для нахождения корня уравнения f(x) = 0\
        на отрезке [a, b]. :param f: функция f(x) :param a: левая граница\
            отрезка :param b: правая граница отрезка :param eps: точность\
                :return: приближенное значение корня """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("Корень не найден на данном отрезке.")
        return None

    while abs(b - a) > eps:
        c = (a + b) / 2
        fc = f(c)

        if fc == 0:
            return c
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2

# Задача a


def f_a(x):
    return x**2 + 2*x - x - 1


root_a = bisection_method(f_a, 0, 1)
if root_a is not None:
    print(f"Корень уравнения f_a(x): {root_a:.3f}")
else:
    print("Корень не найден.")

# Задача b


def f_b(x):
    return x**2 - 0.2*x - 0.2*x**2 - 1.2


root_b = bisection_method(f_b, 1, 1.5)
if root_b is not None:
    print(f"Корень уравнения f_b(x): {root_b:.3f}")
else:
    print("Корень не найден.")
