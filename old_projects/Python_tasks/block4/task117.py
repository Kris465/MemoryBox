num1 = input("Введите число от 10 до 99: ")
num2 = input("Введите число от 10 до 99: ")
a2 = num1[0]
a1 = num1[1]

b2 = num2[0]
b1 = num2[1]
flag = False

if int(a1) < int(b1):
    res = (10 - int(b1))
    res2 = int(a2) - int(b2)
    flag = True
else:
    res = int(a1) - int(b1)
    res2 = int(a2) - int(b2)
    flag = False

if flag:
    print(f"Результат будет: {(int(res2) - 1)}{int(res) + int(a1)}")
else:
    print(f"Результат будет: {res2}{res}")
