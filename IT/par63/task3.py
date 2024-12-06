def find_three_minimus(arr):
    unique_elements = list(set(arr))
    unique_elements.sort()
    if len(unique_elements) < 3:
        print("Недостаточно уникальных элементов.")
        return
    return unique_elements[:3]


array = [7, 1, 3, 2, 5, 2, 4]
print("Три минимума:", find_three_minimus(array))
