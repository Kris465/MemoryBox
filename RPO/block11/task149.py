arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

arr.pop(2)
print("а)", arr)

k = int(input("Введите номер элемента для удаления (от 1 до 10): "))
index = k - 1

if 0 <= index < len(arr):
    arr.pop(index)
    print("б)", arr)
else:
    print("Ошибка: некорректный номер!")
