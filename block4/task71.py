a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))

mx = a

if b > mx:
    mx = b
if c > mx:
    mx = c

print(mx)
