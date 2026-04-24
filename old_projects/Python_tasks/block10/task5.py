# Ваирант А
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))


if x < 0:
    sign_x = -1
elif x == 0:
    sign_x = 0
else:
    sign_x = 1


if y < 0:
    sign_y = -1
elif y == 0:
    sign_y = 0
else:
    sign_y = 1


z = sign_x + sign_y


print(f"Значение z (без функции sign): {z}")

# Вариант Б


def sign(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1


x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

sign_x = sign(x)
sign_y = sign(y)

z = sign_x + sign_y

print(f"Значение z (с использованием функции sign): {z}")
