from math import sin, sqrt


a = int(input("Введите число a: "))


result_a = sqrt(2 * a) + sin(abs(3 * a)) / 3.56


result_a_rounded = round(result_a, 2)


print(f"sqrt(2 * a) + sin(abs(3 * a)) / 3.56 = {result_a_rounded}")


x = int(input("Введите число x: "))


if x == 0:
    print("Ошибка: x не может быть равен 0, \
          так как это приведет к делению на ноль.")
else:
    if (1 - x) < 0:
        print("Ошибка: выражение (1 - x) должно быть неотрицательным для\
               извлечения квадратного корня.")
    else:
        result_x = sin((3.2 + sqrt(1 - x)) / abs(5 * x))

        result_x_rounded = round(result_x, 4)

        print(f"sin((3.2 + sqrt(1 - x)) / abs(5 * x)) = {result_x_rounded}")
