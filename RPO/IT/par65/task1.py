def sort_and_find(arr, target):
    # Сортируем массив по убыванию
    sorted_arr = sorted(arr, reverse=True)
    print(f"Отсортированный массив: {sorted_arr}")

    # Находим все значения, равные введенному числу
    occurrences = [
        index for index, value in enumerate(sorted_arr) if value == target]

    if occurrences:
        print(f"Число {target} найдено на позициях: {occurrences}")
    else:
        print(f"Число {target} не найдено в массиве.")


# Пример использования
array = [5, 3, 6, 2, 8, 5, 1, 7]
target_number = int(input("Введите число для поиска: "))
sort_and_find(array, target_number)


def sort_and_find(arr, target):
    # Сортируем массив по убыванию
    sorted_arr = sorted(arr, reverse=True)
    print(f"Отсортированный массив: {sorted_arr}")

    # Находим все значения, равные введенному числу
    occurrences = [
        index for index, value in enumerate(sorted_arr) if value == target]

    if occurrences:
        print(f"Число {target} найдено на позициях: {occurrences}")
    else:
        print(f"Число {target} не найдено в массиве.")


# Пример использования
array = [5, 3, 6, 2, 8, 5, 1, 7]
target_number = int(input("Введите число для поиска: "))
sort_and_find(array, target_number)
