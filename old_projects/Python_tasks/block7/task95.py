def is_product_greater(ds, s):
    product = 1.0
    for d in ds:
        product *= d
    if product > s:
        return "Да"
    else:
        return "Нет"


n = int(input("Введите количество вещественных чисел: "))
ds = list(map(float, input("Введите вещественные числа через пробел: ")
              .split()))
s = float(input("Введите число s: "))

result = is_product_greater(ds, s)
print(result)
