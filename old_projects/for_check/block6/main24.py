def analyze_sequence(sequence, x):
    # а) Сумма всех чисел, больших x
    sum_greater_x = sum(num for num in sequence if num > x)
    
    # б) Количество четных чисел
    count_even = sum(1 for num in sequence if num % 2 == 0)
    
    return {
        'сумма_больше_x': sum_greater_x,
        'количество_четных': count_even
    }

# Пример использования
sequence = [1, 2, 3, 4, 5, 0]  # последовательность должна оканчиваться нулем
x = 3  # значение для сравнения

result = analyze_sequence(sequence, x)
print(f"Анализ последовательности {sequence}:")
for key, value in result.items():
    print(f"{key}: {value}")
