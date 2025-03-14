precipitation = [0.5, 0.0, 1.2, 0.8, 0.0, 0.6, 2.3, 0.0, 1.0, 0.4,
                 0.2, 0.0, 0.3, 0.5, 0.0, 0.1, 0.4, 0.0, 0.6, 0.0,
                 1.5, 0.0, 0.2, 0.3, 0.0, 0.7, 0.1, 0.0, 0.4, 0.5]

total_precipitation = 0.0


for i in range(1, len(precipitation), 2):
    total_precipitation += precipitation[i]

print(f"Общее количество осадков, выпавших 2-го, 4-го и т.д. числа месяца: \
    {total_precipitation} мм")
