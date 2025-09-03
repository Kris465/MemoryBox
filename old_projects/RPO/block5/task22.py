lis = [x for x in range(100, 2000 + 1, 100)]
cost = float(input('Стоимость 1000 г конфет (в рублях): '))
print("Стоимость:")
for x in lis:
    print(f'{x} грамма - {cost * x / 1000} рублей')
