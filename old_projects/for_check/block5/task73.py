def calculate_yield(initial_yield, area_increase, yield_decrease):
    # Рассчитываем новую площадь
    final_area = initial_yield * (1 + area_increase)

    # Рассчитываем снижение урожайности
    final_yield_per_hectare = initial_yield * (1 - yield_decrease)

    # Общее количество урожая
    total_yield = final_area * final_yield_per_hectare

    return total_yield


initial_yield = 20  # Урожайность на гектар
area_increase = 0.03  # Увеличение площади в процентах
yield_decrease = 0.03  # Снижение урожайности в процентах

final_yield = calculate_yield(initial_yield, area_increase, yield_decrease)
print("Общий урожай в этом году: {:.2f} центнеров".format(final_yield))
