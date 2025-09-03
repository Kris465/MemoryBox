def remove_min_max(arr):
    if len(arr) <= 2:
        return []
    min_val = min(arr)
    max_val = max(arr)
    new_arr = [x for x in arr if x != min_val and x != max_val]
    return new_arr
