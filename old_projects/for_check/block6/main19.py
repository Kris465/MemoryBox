def next_fraction(prev_numerator, prev_denominator, curr_numerator, curr_denominator):
    """Вычисляет следующую дробь в последовательности"""
    next_numerator = prev_numerator + curr_numerator
    next_denominator = prev_denominator + curr_denominator
    return next_numerator, next_denominator

def fraction_value(numerator, denominator):
    """Вычисляет значение дроби как float"""
    return numerator / denominator

def find_close_fractions():
    # Начальные значения
    prev_num, prev_denom = 1, 1  # Первая дробь: 1/1
    curr_num, curr_denom = 2, 1  # Вторая дробь: 2/1
    
    i = 2  # Начинаем с индекса 2, так как у нас уже есть первые две дроби
    while True:
        # Вычисляем следующую дробь
        next_num, next_denom = next_fraction(prev_num, prev_denom, 
                                           curr_num, curr_denom)
        
        # Вычисляем значения текущей и следующей дроби
        curr_val = fraction_value(curr_num, curr_denom)
        next_val = fraction_value(next_num, next_denom)
        
        # Проверяем разницу
        diff = abs(curr_val - next_val)
        if diff <= 0.001:
            print(f"Найдены близкие дроби:")
            print(f"{curr_num}/{curr_denom} ≈ {curr_val:.6f}")
            print(f"{next_num}/{next_denom} ≈ {next_val:.6f}")
            print(f"Разница: {diff:.6f}")
            break
            
        # Обновляем значения для следующей итерации
        prev_num, prev_denom = curr_num, curr_denom
        curr_num, curr_denom = next_num, next_denom
        i += 1
        
        # Защита от зацикливания
        if i > 100:
            print("Превышено максимальное количество итераций")
            break

# Запускаем поиск
find_close_fractions()
