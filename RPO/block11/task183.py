import bisect


arr = [1, 3, 5, 7, 9, 11, 13, 15]
a = 8


index = bisect.bisect_left(arr, a)
print("а)", *arr[:index])


left_index = index - 1
right_index = index
print("б) Элементы между которыми находится a:")
print(f"   [{left_index}] {arr[left_index]}")
print(f"   [{right_index}] {arr[right_index]}")


candidates = [(abs(a - arr[left_index]), left_index),
              (abs(a - arr[right_index]), right_index)]
_, best_index = min(candidates)
print(f"в) Ближайший элемент: [{best_index}] {arr[best_index]}")
