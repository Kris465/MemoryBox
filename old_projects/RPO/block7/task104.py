numbers = []
for i in range(10):
    number = int(input(f"Введите {i+1}-е целое число: "))
    numbers.append(number)


count = sum(1 for x in numbers if x <= 50.55)

if count % 4 == 0:
    print("Количество чисел меньше 50,55 кратно 4")
else:
    print("Количество чисел меньше 50.55 не кратно 4")
