temperatures = [
    25, 27, 30, 29, 31, 28, 26,
    32, 33, 31, 30, 29, 28, 27,
    34, 35, 33, 32, 31, 30, 29,
    28, 27, 26, 25, 24, 23, 22,
]

if len(temperatures) < 7:
    print("Ошибка: данных недостаточно для анализа недель.")
else:
    max_temp_in_window = float('-inf')
    start_index_of_max_window = 0

    for i in range(len(temperatures) - 6):
        current_window = temperatures[i:i+7]
        max_temp_in_current_window = max(current_window)

        if max_temp_in_current_window > max_temp_in_window:
            max_temp_in_window = max_temp_in_current_window
            start_index_of_max_window = i

    warmest_week = temperatures[start_index_of_max_window : start_index_of_max_window + 7]

    print(f"Самые теплые семь дней: {warmest_week}")
    print(f"Максимальная температура в этом интервале: {max_temp_in_window}")
