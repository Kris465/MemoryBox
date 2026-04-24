points = [list(map(int, input("Введите массив: ")))]
n = int(input("Введите искомые очки команды"))

place = points.index(n) + 1
print(place)
