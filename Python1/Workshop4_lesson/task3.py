# 3. На вход программе подается число n.
#    Программа печатает численный треугольник.
#    Используем вложенные циклы.

def pyramid():
    n = int(input("Input the number: "))
    
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="")
        print()

pyramid()
