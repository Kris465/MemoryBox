def are_same_color(a, b, c, d):
    return (a + b) % 2 == (c + d) % 2


a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))

if are_same_color(a, b, c, d):
    print("Поля ({}, {}) и ({}, {}) одного цвета.".format(a, b, c, d))
else:
    print("Поля ({}, {}) и ({}, {}) разного цвета.".format(a, b, c, d))
