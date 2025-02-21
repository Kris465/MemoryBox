january_precipitation = [2.5, 1.2, 0.8, 3.1, 2.0, 1.5, 0.9, 2.3, 1.7, 2.9,
                         1.8, 0.6, 1.4, 2.2, 1.9, 0.7, 2.3, 1.5, 2.1, 1.3,
                         0.8, 1.6, 2.4, 1.1, 0.5, 1.3, 2.0, 1.2, 0.7, 2.1, 1.4]


march_precipitation = [1.9, 0.7, 2.3, 1.5, 2.1, 1.3, 0.8, 1.6, 2.4, 1.1,
                       0.5, 1.3, 2.0, 1.2, 0.7, 2.1, 1.4, 1.8, 0.6, 1.4,
                       2.2, 1.9, 0.7, 2.3, 1.5, 2.1, 1.3, 0.8, 1.6, 2.4, 1.1]


def calculate_average_precipitation(precipitation_list):
    total_precipitation = sum(precipitation_list)
    days_in_month = len(precipitation_list)
    average_precipitation = total_precipitation / days_in_month
    return average_precipitation


january_avg = calculate_average_precipitation(january_precipitation)
print(f"Среднедневное количество осадков за январь: {january_avg:.2f}")


march_avg = calculate_average_precipitation(march_precipitation)
print(f"Среднедневное количество осадков за март: {march_avg:.2f}")
