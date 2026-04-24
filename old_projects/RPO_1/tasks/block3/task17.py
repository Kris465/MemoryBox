a = input("Введите true или false: ")
в = input("Введите true или false: ")

e1 = not a and not в or a
e2 = в or a and not в
e3 = в and not (a and not в)

print("a)", e1)
print("б)", e2)
print("в)", e3)
