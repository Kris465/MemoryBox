jiteli = int(input("Количество жителей: "))
teritoria = float(input("Площадь территории: "))

if teritoria != 0:
    plotnost = jiteli / teritoria
    print(f"Плотность: {plotnost} человек на единицу площади")
else:
    print("Площадь не может быть равна нулю.")
