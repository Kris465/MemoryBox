import random


def longest_equal_sequence(arr):
    max_length = current_length = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)


array = [random.randint(10, 12) for _ in range(20)]
print("Массив:", array)
print("Длина самой длинной последовательности:", longest_equal_sequence(array))
