from random import randint

n = int(input("Введите число: "))
arr = [randint(-10, 10) for _ in range(n)]
print(arr)
min_pos = None
for num in arr:
    if min_pos is not None and 0 < num < min_pos\
          or num > 0 and min_pos is None:
        min_pos = num
print(min_pos)
