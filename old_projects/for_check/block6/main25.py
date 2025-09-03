def count_sign_changes(sequence):
    # Инициализируем счетчик смен знака
    sign_changes = 0
    
    # Пропускаем первый элемент, так как у него нет предыдущего для сравнения
    for i in range(1, len(sequence)):
        # Проверяем, что текущий и предыдущий элементы не равны нулю
        if sequence[i] != 0 and sequence[i-1] != 0:
            # Если знаки различаются, увеличиваем счетчик
            if (sequence[i] > 0) != (sequence[i-1] > 0):
                sign_changes += 1
    
    return sign_changes

# Примеры использования
examples = [
    [10, -4, 12, 56, -4, 0],  # 3 смены знака
    [1, 2, 3, -4, 5, 0],      # 1 смена знака
    [-1, -2, -3, 0],          # 1 смена знака
    [1, -1, 1, -1, 0],        # 4 смены знака
    [5, 0, -3, 0, 2, 0]       # 2 смены знака (нули пропускаются)
]

for sequence in examples:
    changes = count_sign_changes(sequence)
    print(f"Последовательность: {sequence}")
    print(f"Количество смен знака: {changes}\n")
