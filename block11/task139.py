floors = [list(map(int, input("Введите массив: ").split()))]
floors_copy = floors.copy()
min1_index = floors_copy.index(min(floors_copy))
min1_value = floors_copy[min1_index]
floors_copy[min1_index] = float('inf')
min2_index = floors_copy.index(min(floors_copy))
min2_value = floors_copy[min2_index]
print(f"Этажи с наименьшим количеством людей:\
    {min1_index + 1} и {min2_index + 1}")
