num1 = input('Введите цифру a 10-99: ')
num2 = input('Введите цифру б 0-9: ')


a2 = num1[0]
a1 = num1[1]

b1 = num2[0]
flag = False

if int(a1) < int(b1):
    res = 10 - int(b1)
    flag = True
else:
    res = int(a1) - int(b1)
    flag = False

if flag:
    print(f"Результат будет: {(int(a2) - 1)}{res}")
else:
    print(f"Результат будет: {a2}{res}")
