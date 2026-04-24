result = list(range(13, 100, 13))
print(result)


numbers = []
for i in range(1, 100):
    if i % 13 == 0:
        numbers.append(i)
print(numbers)
