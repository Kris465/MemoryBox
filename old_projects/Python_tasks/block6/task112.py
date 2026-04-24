a = list(input("Введите число: "))
k = 0
for i in range(0, len(a)):
    if (a[i] == '3'):
        k = i
        print(i)
if (k == 0):
    print("0")

a = list(input())
k = 0
for i in range(0, len(a)):
    if (a[i] == '3'):
        k = i
        print(i+1)
if (k == 0):
    print("0")
