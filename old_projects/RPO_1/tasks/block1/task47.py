x = int(input("Введите координату x: "))
x1 = int(input("Введите координату x1: "))
more = 0
smaller = 0

if x > x1:
    more = x
    smaller = x1
else:
    more = x1
    smaller = x

distance = more - smaller

print("Расстояние между двумя точками: ", distance)
