def find_duplicate(nums):
    n = len(nums) - 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return actual_sum - expected_sum


arr = [1, 2, 3, 4, 5, 2]
print(find_duplicate(arr))
