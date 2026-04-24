x = int(input("Введите значение x: "))
y = int(input("Введите значение y: "))
z = int(input("Введите значение z: "))

condition_a = (x % 2 != 0) and (y % 2 != 0)

condition_b = (x < 20 and y >= 20) or (x >= 20 and y < 20)

condition_v = (x == 0) or (y == 0)

condition_g = (x < 0) and (y < 0) and (z < 0)

condition_d = (
    (x % 5 == 0 and y % 5 != 0 and z % 5 != 0)
    or (x % 5 != 0 and y % 5 == 0 and z % 5 != 0)
    or (x % 5 != 0 and y % 5 != 0 and z % 5 == 0)
)

condition_e = (x > 100) or (y > 100) or (z > 100)

print("Условие а (x и y нечетны):", condition_a)
print("Условие б (только одно из x и y меньше 20):", condition_b)
print("Условие в (хотя бы один из x или y равен 0):", condition_v)
print("Условие г (x, y, z отрицательны):", condition_g)
print("Условие д (одно кратно 5):", condition_d)
print("Условие е (хотя бы одно больше 100):", condition_e)
