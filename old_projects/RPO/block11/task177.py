def fix_sorted_array(arr, k):
    if k < 0 or k >= len(arr):
        return arr

    element = arr.pop(k)

    insert_pos = 0
    while insert_pos < len(arr) and arr[insert_pos] < element:
        insert_pos += 1

    arr.insert(insert_pos, element)
    return arr


speeds = [100, 120, 140, 160, 180, 150, 200]
fixed_speeds = fix_sorted_array(speeds, 5)
print(fixed_speeds)
