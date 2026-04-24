arr = [3, 4, 6, 5, 8, 7, 9, 10, 15]


arr_a = [x for i, x in enumerate(arr) if not (i % 2 == 1 and x % 2 == 0)]
print("а)", arr_a)

arr_b = [x for x in arr if x % 3 != 0 and x % 5 != 0]
print("б)", arr_b)
