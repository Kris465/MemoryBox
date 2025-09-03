def average_mass(masses):
    if len(masses) == 0:
        return None

    total_mass = sum(masses)
    average = total_mass / len(masses)
    return average


masses = [5, 8, 12, 7, 9]
average_value = average_mass(masses)
print(f"Средняя масса: {average_value}")
