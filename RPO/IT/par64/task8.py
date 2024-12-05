def count_bubble_swaps(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
                swapped = True
        if not swapped:
            break
    return swap_count


def count_stone_swaps(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        max_index = 0
        for j in range(1, n - i):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != n - i - 1:
            arr[max_index], arr[n - i - 1] = arr[n - i - 1], arr[max_index]
            swap_count += 1
    return swap_count


def test_sorting_methods():
    arrays_to_test = {
        "Уже отсортированный": [1, 2, 3, 4, 5],
        "Убывающий": [5, 4, 3, 2, 1],
        "Случайный": [3, 1, 4, 2, 5]
    }

    for description, array in arrays_to_test.items():
        print(f"\nТест для: {description}")

        bubble_array = array.copy()
        stone_array = array.copy()

        bubble_swaps = count_bubble_swaps(bubble_array)
        stone_swaps = count_stone_swaps(stone_array)

        print(f"Количество перестановок (пузырек): {bubble_swaps}")
        print(f"Количество перестановок (метод камня): {stone_swaps}")


test_sorting_methods()
