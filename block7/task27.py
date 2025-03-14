count = 0
n = 1

while True:
    bn = n ** 3
    if bn >= 100:
        break
    count += 1
    n += 1

print(count)
