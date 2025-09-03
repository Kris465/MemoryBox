def average_mass(masses):
    full = [m for m in masses if m > 100]
    others = [m for m in masses if m <= 100]

    avg_full = sum(full) / len(full)
    avg_others = sum(others) / len(others)

    return avg_full, avg_others


masses = [85, 105, 90, 110, 95, 120]
avg_full, avg_others = average_mass(masses)
print(f"Средняя масса полных людей: {avg_full}")
print(f"Средняя масса остальных людей: {avg_others}")
