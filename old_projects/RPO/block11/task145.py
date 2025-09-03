arr = [1, 2, 3, 4, 5, 6]

half = len(arr) // 2
swapped_halves = arr[half:] + arr[:half]
print("а)", swapped_halves)

for i in range(0, len(arr), 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print("б)", arr)

half = len(arr) // 2
for i in range(half):
    arr[i], arr[-i-1] = arr[-i-1], arr[i]
print("в)", arr)
