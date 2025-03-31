<<<<<<< HEAD
precipitation = [5, 10, 0, 8, 12, 7, 0, 9, 11, 6, 0, 10, 8, 12, 7, 0, 9, 11,
                 6, 0, 10, 8, 12, 7, 0, 9, 11, 6, 0, 10]

total_precipitation = sum(filter(lambda x: precipitation.index(x) % 2 == 0,
                                 precipitation))

print("Общее количество осадков за четные дни месяца:", total_precipitation)
=======
precipitation = [0.5, 0.0, 1.2, 0.8, 0.0, 0.6, 2.3, 0.0, 1.0, 0.4,
                 0.2, 0.0, 0.3, 0.5, 0.0, 0.1, 0.4, 0.0, 0.6, 0.0,
                 1.5, 0.0, 0.2, 0.3, 0.0, 0.7, 0.1, 0.0, 0.4, 0.5]

total_precipitation = 0.0


for i in range(1, len(precipitation), 2):
    total_precipitation += precipitation[i]

print(f"Общее количество осадков, выпавших 2-го, 4-го и т.д. числа месяца: \
    {total_precipitation} мм")
>>>>>>> db601d430cb832b2128b1b19d7480eb6966c95df
