from random import randint


def generate_fibonacci_up_to(n):
    fibs = [0, 1]
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])
    return set(fibs)


def find_fibonacci_numbers(arr):
    fib_set = generate_fibonacci_up_to(max(arr))
    return [x for x in arr if x in fib_set]


array = [randint(0, 100) for _ in range(20)]
print("Массив:", array)
print("Числа Фибоначчи в массиве:", find_fibonacci_numbers(array))
