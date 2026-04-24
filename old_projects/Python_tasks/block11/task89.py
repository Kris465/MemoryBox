def is_boys_avg_height_10cm_more(heights):
    boys = [abs(h) for h in heights if h < 0]
    girls = [h for h in heights if h > 0]

    if not boys or not girls:
        return False  # если нет мальчиков или девочек, условие не выполняется

    avg_boys = sum(boys) / len(boys)
    avg_girls = sum(girls) / len(girls)

    return avg_boys - avg_girls > 10

# Пример использования:
heights = [-170, 160, -180, 155, -175, 165]  # рост мальчиков задан отрицательными числами
print(is_boys_avg_height_10cm_more(heights))  # Проверяем условие