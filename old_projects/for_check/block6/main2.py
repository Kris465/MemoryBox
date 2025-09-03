total = 0
count = 0

while True:
    num = int(input("Введите число: "))
    if num < 0:
        break
    total += num
    count += 1

print(total / count if count > 0 else 0)
