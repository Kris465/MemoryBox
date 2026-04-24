h = int(input("Введите число h: "))
m = int(input("Введите число m: "))
s = int(input("Введите число s: "))

if not (0 < h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
    print("Ошибка: значения должны быть в диапазонах 0<h<23, 0<m<59, 0<s<59")
else:
    ang1le = (h % 12) * 30 + m * 0.5 + s * (1 / 120)
    print(ang1le)


def hour_hand_angle(h, m, s):
    h = h % 12
    total_seconds = h * 3600 + m * 60 + s
    angle = (total_seconds / 43200) * 360
    print(angle)
    return angle
