mas = [int(i) for i in input("Введите массив: ").split()]
flag = 0
for i in mas:
    if i % 2 == 0:
        max = min = i
        flag = 1
        break
if flag == 0:
    print("Четных нет")
    exit()
for i in mas:
    if i % 2 == 0 and i > max:
        max = i
    if i % 2 == 0 and i < min:
        min = i
        
print(max, min)
