arr = [list(map(int, input("Введите массив: ").split()))]
n = int(input("Введите искомые очки команды"))

try:
    index = arr.index(n)
    print(arr[:index])
except ValueError:
    print(arr)
