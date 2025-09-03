array = [3, -5, 8, 0, -2, 7]

s = int(input("Введите индекс s-го элемента: "))

if 0 <= s < len(array):
    if array[s] > 0:
        print(f"s-й элемент ({array[s]}) является положительным числом.")
    else:
        print(f"s-й элемент ({array[s]}) не является положительным числом.")
else:
    print("Некорректный индекс s.")

k = int(input("Введите индекс k-го элемента: "))

if 0 <= k < len(array):
    if array[k] % 2 == 0:
        print(f"k-й элемент ({array[k]}) является четным числом.")
    else:
        print(f"k-й элемент ({array[k]}) не является четным числом.")
else:
    print("Некорректный индекс k.")

s = int(input("Введите индекс s-го элемента: "))
k = int(input("Введите индекс k-го элемента: "))

if (0 <= s < len(array)) and (0 <= k < len(array)):
    if array[s] > array[k]:
        print(f"Элемент {array[s]} (s-й) больше элемента {array[k]} (k-й).")
    elif array[s] < array[k]:
        print(f"Элемент {array[k]} (k-й) больше элемента {array[s]} (s-й).")
    else:
        print(f"Элементы равны: {array[s]} и {array[k]}.")
else:
    print("Один или оба индекса некорректны.")
