def find_max_min(numbers):
    if not numbers:
        return None, None

    max_num = min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num


numbers = [3.5, 2.1, 7.8, 5.4, 1.2]
max_num, min_num = find_max_min(numbers)
print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
