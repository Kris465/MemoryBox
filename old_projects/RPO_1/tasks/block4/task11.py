mass1 = float(input("Введите массу первого тела: "))
volume1 = float(input("Введите объем первого тела: "))

mass2 = float(input("Введите массу второго тела: "))
volume2 = float(input("Введите объем второго тела: "))

density1 = mass1 / volume1
density2 = mass2 / volume2

print(f"Плотность первого тела: {density1}")
print(f"Плотность второго тела: {density2}")

if density1 > density2:
    print("Материал первого тела имеет большую плотность.")
elif density1 < density2:
    print("Материал второго тела имеет большую плотность.")
else:
    print("Материалы двух тел имеют одинаковую плотность.")
