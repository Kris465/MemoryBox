from random import randint


def cyclic_shift_right(arr, shift):
    shift %= len(arr)
    return arr[-shift:] + arr[:-shift]


array = [randint(0, 10) for _ in range(10)]
print("Исходный массив :", array)
print("Массив после циклического сдвига вправо на 4 элемента:",
      cyclic_shift_right(array, 4))
