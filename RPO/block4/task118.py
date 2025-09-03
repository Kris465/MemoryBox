def find_digits_sum(aaa, bb):
    result = 340 + aaa + bb
    x = result // 10
    y = (result % 100) // 10
    z = result % 10
    return x, y, z


aaa = 123
bb = 45
x, y, z = find_digits_sum(aaa, bb)
print(f"Цифры числа-суммы: {x}, {y}, и {z}")
