a = int(input("Прибытие часов: "))
b = int(input("Прибытие минут: "))
c = int(input("Отбытие часов: "))
d = int(input("Отбытие минут: "))
n = int(input("Пришел часов: "))
m = int(input("Пришел минут: "))
if a < n < c or a == n and b < m or c == n and m < d:
    print("Будет стоять")
else:
    print("Не будет стоять")
