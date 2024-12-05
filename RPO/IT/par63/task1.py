def find_min_max_even_positive(arr):
    even_positive = [x for x in arr if x > 0 and x % 2 == 0]

    if not even_positive:
        print("Нет четных положительных значений.")
    else:
        print("Минимальное:", min(even_positive))
        print("Максимальное:", max(even_positive))


array = [1, -2, 3, 4, 5, 6, -8]
find_min_max_even_positive(array)
