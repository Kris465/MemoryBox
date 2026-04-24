x = input("Введите true или false: ")
y = input("Введите true или false: ")

rez1 = (not (x and not y)) or x
rez2 = (y and not x) or (not y)
rez3 = (not y and not x) or y

print("a)", rez1)
print("б)", rez2)
print("в)", rez3)
