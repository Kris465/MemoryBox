def calculate_parallel_resistance(resistances):
    total_conductance = sum(1 / r for r in resistances)
    return 1 / total_conductance

# Пример использования функции
resistances = [10, 20, 30]
total_resistance = calculate_parallel_resistance(resistances)
print(f"Общее сопротивление: {total_resistance:.3f} Ом")
