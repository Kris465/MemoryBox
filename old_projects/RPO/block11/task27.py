rainfall = [5, 3, 0, 2, 4, 1, 0, 3, 2, 4,
            6, 2, 1, 3, 0, 2, 4, 5, 1, 0,
            3, 2, 4, 1, 0, 2, 3, 4, 2, 1]

if len(rainfall) !=30:
    print("Длина массива должна быть равна 30.")
else:
    first_decade_avg = sum(rainfall[0:10]) /10
    second_decade_avg = sum(rainfall[10:20]) /10
    third_decade_avg = sum(rainfall[20:30]) /10

    print(f"Среднее количество осадков в первую декаду: {first_decade_avg:.2f}")
    print(f"Среднее количество осадков во вторую декаду: {second_decade_avg:.2f}")
    print(f"Среднее количество осадков в третью декаду: {third_decade_avg:.2f}")