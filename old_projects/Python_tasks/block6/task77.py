heights = input("Введите рост учащихся через пробел: ").split()

heights = [float(height) for height in heights]

is_descending = True

for i in range(1, len(heights)):
    if heights[i] > heights[i - 1]:
        is_descending = False
        break


if is_descending:
    print("Ученики перечислены в порядке убывания роста.")
else:
    print("Ученики перечислены НЕ в порядке убывания роста.")
