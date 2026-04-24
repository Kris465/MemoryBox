x = input("Введите true или false: ")
y = input("Введите true или false: ")
z = input("Введите true или false: ")

resX = not (x or not y and z)
resY = y or (x and not y or z)
resZ = not (not x and y or z)

print("a)", resX)
print("б)", resY)
print("в)", resZ)
