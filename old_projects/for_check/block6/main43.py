def analyze_sequence():
    numbers = []
    print("Введите последовательность вещественных чисел, заканчивающуюся 1000:")
    
    while True:
        number = float(input())
        if number == 1000:
            break
        numbers.append(number)

    if not numbers:  # Если последовательность пустая
        print("Последовательность не должна быть пустой.")
        return

    count_equal = 0  # Количество подряд идущих равных чисел
    count_distinct = 0  # Количество различных чисел
    current_number = numbers[0]
    current_count = 1
    
    for i in range(1, len(numbers)):
        if numbers[i] == current_number:
            current_count += 1
        else:
            if current_count > 1:
                count_equal += current_count
            current_number = numbers[i]
            current_count = 1

    # Обработка последней группы
    if current_count > 1:
        count_equal += current_count

    count_distinct = len(set(numbers))  # Количество различных чисел
    
    print("Количество подряд идущих равных чисел:", count_equal)
    print("Количество различных чисел:", count_distinct)


# Запускаем анализ последовательности
analyze_sequence()
