def is_sorted_by_score(scores):
    """
    Определяет, отсортирован ли список очков команд в порядке убывания,
    что соответствует порядку мест в чемпионате.

    Args:
        scores: список целых чисел, представляющих очки команд.

    Returns:
        tuple: (bool, int).
            - bool: True, если список отсортирован по убыванию, False в
                    противном случае.
            - int: порядковый номер первой команды, нарушающей порядок
                   (нумерация с 1), или 0, если список отсортирован.
    """
    if len(scores) < 2:
        return True, 0  # Если меньше двух команд, то считается, что порядок соблюден

    for i in range(len(scores) - 1):
        if scores[i] < scores[i + 1]:
            return False, i + 2 # Индекс команды, нарушающей порядок

    return True, 0


# Примеры использования:
scores1 = [100, 90, 80, 70, 60]
result1, index1 = is_sorted_by_score(scores1)
print(f"Список {scores1} соответствует порядку мест в чемпионате: {result1}, индекс нарушения: {index1}")

scores2 = [100, 90, 80, 60, 70]
result2, index2 = is_sorted_by_score(scores2)
print(f"Список {scores2} соответствует порядку мест в чемпионате: {result2}, индекс нарушения: {index2}")

scores3 = [100, 100, 90, 80] # Пример с одинаковыми очками
result3, index3 = is_sorted_by_score(scores3)
print(f"Список {scores3} соответствует порядку мест в чемпионате: {result3}, индекс нарушения: {index1}")


scores4 = [100] # Пример с одной командой
result4, index4 = is_sorted_by_score(scores4)
print(f"Список {scores4} соответствует порядку мест в чемпионате: {result4}, индекс нарушения: {index4}")
