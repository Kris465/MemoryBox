a = input("Введите значение первого операнда (True/False) ")
b = input("Введите значение второго операнда (True/False) ")
c = input("Введите значение третьего операнда (True/False) ")
d = input('Введите тип логической операции(`and`, `or`, `xor`)')
results = True

if d == 'or':
    results = a or b or c
elif d == 'and':
    results = a and b and c
elif d == 'xor':
    results = a ^ b ^ c
else:
    print('Неправильно введены данные')

print(f'{a} {d} {b} {d} {c} = {results}')
