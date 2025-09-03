def count_unique_numbers(arr):
    unique_numbers = set(arr)
    return len(unique_numbers)


array = [3, 1, 2, 2, 3, 4, 5, 1]
array.sort()  # Сортируем массив
print("Отсортированный массив:", array)
print("Количество различных чисел:", count_unique_numbers(array))
