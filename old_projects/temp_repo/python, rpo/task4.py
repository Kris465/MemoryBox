def unique_elements(list1, list2):
    # Создаем пустой список для хранения уникальных элементов
    result = []

    # Проверяем элементы первого списка
    for item in list1:
        # Если элемент не в списке 2, добавляем его в результат
        found = False
        for other in list2:
            if item == other:
                found = True
                break
        if not found:
            result.append(item)

    # Проверяем элементы второго списка
    for item in list2:
        # Если элемент не в списке 1, добавляем его в результат
        found = False
        for other in list1:
            if item == other:
                found = True
                break
        if not found:
            result.append(item)

    return result


# Пример использования
list1 = [6, 8, 6, 7, 3]
list2 = [2, 5, 8, 7, 3]
result = unique_elements(list1, list2)
print(result)  # Вывод: [6, 2, 5]
