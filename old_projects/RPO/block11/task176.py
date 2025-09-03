def fix_sorted_array(arr):
    if len(arr) < 2:
        return arr

    last_element = arr[-1]
    del arr[-1]

    insert_pos = 0
    while insert_pos < len(arr) and arr[insert_pos] < last_element:
        insert_pos += 1

    arr.insert(insert_pos, last_element)
    return arr


cities = [list(map(int, input("ВВедите массив")))]
fixed_cities = fix_sorted_array(cities)
print(fixed_cities)
