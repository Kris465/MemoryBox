def calculate_deposit():
    initial_amount = 1000  # Начальная сумма вклада
    monthly_interest = 0.02  # Ежемесячный процент (2%)
    month = 0  # Счетчик месяцев
    
    # Переменные для хранения результатов
    month_increase_exceeds_30 = None
    month_amount_exceeds_1200 = None
    
    current_amount = initial_amount
    
    while True:
        month += 1
        increase = current_amount * monthly_interest  # Ежемесячное увеличение
        current_amount += increase  # Обновляем сумму вклада
        
        # Проверяем условие для пункта а)
        if month_increase_exceeds_30 is None and increase > 30:
            month_increase_exceeds_30 = month
        
        # Проверяем условие для пункта б)
        if month_amount_exceeds_1200 is None and current_amount > 1200:
            month_amount_exceeds_1200 = month
        
        # Если оба условия выполнены, выходим из цикла
        if month_increase_exceeds_30 is not None and month_amount_exceeds_1200 is not None:
            break
    
    return month_increase_exceeds_30, month_amount_exceeds_1200

# Вызов функции и вывод результатов
month_increase, month_amount = calculate_deposit()
print(f"а) Величина ежемесячного увеличения вклада превысит 30 руб. на {month_increase} месяце.")
print(f"б) Размер вклада превысит 1200 руб. через {month_amount} месяцев.")
