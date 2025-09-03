a = 10
b = 5
i = a
while i >= b:
    print(f"Корень из {i} = {i ** 0.5}")
    i -= 1


a = 10
b = 5
i = a
while True:
    print(f"Корень из {i} = {i ** 0.5}")
    i -= 1
    if i < b:
        break
