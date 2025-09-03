total_area = 0


for i in range(1, 13):

    population = float(input(f"Введите количество жителей в районе {i} (в тыс. чел.): "))
    density = float(input(f"Введите плотность населения в районе {i} (в тыс. чел./км²): "))
    

    if density > 0:

        area = population / density

        total_area += area
    else:
        print("Ошибка: Плотность населения не может быть равна нулю.")


print("Общая площадь территории области (в км²):", total_area)
