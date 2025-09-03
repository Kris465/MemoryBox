def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def sort_by_digit_sum(arr):
    return sorted(arr, key=sum_of_digits)


array = [23, 45, 12, 34, 56]
sorted_array = sort_by_digit_sum(array)
print("Отсортированный массив по сумме цифр:", sorted_array)
