x = int(input("Введите число x: "))
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))


print(f"a) -1 / x * x = {round(-1 / x * x, 2)}")
print(f"б) a / (b * c) = {round(a / (b * c), 2)}")
print(f"в) a / b * c = {round(a / b * c, 2)}")
print(f"г) (a + b) / c = {round((a + b) / c, 2)}")
print(f"д) 5.45 * ((a + 2 * b) / (2 - a)) = \
    {round(5.45 * ((a + 2 * b) / (2 - a)), 2)}")
print(f"е) (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a) = \
    {round((-b + (b * b - 4 * a * c) ** 0.5) / (2 * a), 2)} ")
print(f"ж) (-b + 1 / a) / (2 / c) = {round((-b + 1 / a) / (2 / c), 2)}")
print(f"з) 1 / (1 + ((a + b) / 2)) = {round(1 / (1 + ((a + b) / 2)), 2)}")
print(f"и) 1 / (1 + (1 / (2 + (1 / (2 + 3 / 5))))) = \
    {round(1 / (1 + (1 / (2 + (1 / (2 + 3 / 5))))), 2)}")
print(f"к) (2 ** m) ** n = {round((2 ** m) ** n, 2)}")
