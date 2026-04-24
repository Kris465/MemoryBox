from math import sqrt

a = int(input("Введите число a: "))

numerator = a * a + 10
denominator = sqrt(a * a + 1)
result = numerator / denominator

print(f"Числитель: {numerator}")
print(f"Знаменатель: {denominator:.4f}")
print(f"Результат: {result:.4f}")
