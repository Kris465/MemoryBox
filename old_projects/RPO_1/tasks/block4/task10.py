radius = float(input("Введите радиус круга: "))

side = float(input("Введите сторону квадрата: "))

area_circle = 3.141592653589793 * radius ** 2

area_square = side ** 2

print(f"Площадь круга: {area_circle}")
print(f"Площадь квадрата: {area_square}")

if area_circle > area_square:
    print("Площадь круга больше.")
elif area_circle < area_square:
    print("Площадь квадрата больше.")
else:
    print("Площади равны.")
