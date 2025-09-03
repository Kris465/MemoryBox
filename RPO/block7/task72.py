def min_current_resistance(voltages, resistances):
    currents = [v / r for v, r in zip(voltages, resistances) if r != 0]
    return currents.index(min(currents)) + 1


voltages = [10, 20, 15]
resistances = [5, 10, 3]
result = min_current_resistance(voltages, resistances)
print(f"Сопротивление с минимальным током: №{result}")
