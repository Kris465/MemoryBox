x = input("Введите true или false: ")
y = input("Введите true или false: ")

rez1 = not x and not y
rez2 = x or (not x and y)
rez3 = (not x and y) or y

print("a)", rez1)
print("б)", rez2)
print("в)", rez3)
