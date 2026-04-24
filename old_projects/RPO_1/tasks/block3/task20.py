x = input("Введите true или false: ")
y = input("Введите true или false: ")

rez1 = not (not x or y) or not x
rez2 = not (not x and not y) and x
rez3 = not (x or not y) or not y

print("a)", rez1)
print("б)", rez2)
print("в)", rez3)
