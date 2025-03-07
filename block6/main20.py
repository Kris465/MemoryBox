def generate_sequence(x, y0, max_iter=100):
    """
    Генерирует последовательность y_i = 1/2(y_{i-1} + x/y_{i-1} - 1)
    
    Параметры:
    x -- параметр последовательности
    y0 -- начальное значение
    max_iter -- максимальное количество итераций
    """
    sequence = [y0]
    
    for i in range(max_iter):
        prev_y = sequence[-1]
        next_y = 0.5 * (prev_y + x/prev_y - 1)
        sequence.append(next_y)
        
        # Проверяем сходимость
        if abs(next_y - prev_y) < 1e-10:
            break
            
    return sequence

# Пример использования
x = 4.0  # Задайте значение x
y0 = 2.0  # Задайте начальное значение y0

result = generate_sequence(x, y0)
print(f"Первые 10 членов последовательности:")
print(result[:10])
print(f"\nКоличество итераций до сходимости: {len(result)}")
