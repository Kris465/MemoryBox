a = int(input())
b = int(input())
maxx = 0
minn = 0

if a > b:
    maxx = a
else:
    maxx = b

if b < a:
    minn = b
else:
    minn = a

print(f"Максимальное значение: {maxx}")
print(f"Минимальное значение: {minn}")
