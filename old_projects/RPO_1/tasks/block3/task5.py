a = True
b = False
c = False

rez1 = a or b and not c
rez2 = not a and not b
rez3 = not (a and c) or b
rez4 = a and not b or c
rez5 = a and (not b or c)
rez6 = a or (not (b and c))

print("Значение логического выражения А: ", rez1)
print("Значение логического выражения Б: ", rez2)
print("Значение логического выражения В: ", rez3)
print("Значение логического выражения Г: ", rez4)
print("Значение логического выражения Д: ", rez5)
print("Значение логического выражения Е: ", rez6)
