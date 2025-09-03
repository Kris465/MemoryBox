arr = [3, 5, 2, 3, 8, 5, 1, 2]


def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result
