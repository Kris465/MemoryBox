def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def sort_by_digit_sum(arr):
    return sorted(arr, key=sum_of_digits, reverse=True)


arr = [34, 23, 12, 45, 56]
print(sort_by_digit_sum(arr))
