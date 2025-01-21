from random import randint


hislo = int(input("напишите диапазон начала: "))
hislo1 = int(input("напишите диапазон конеца: "))
hisloline = int(input("напиши размер списка: "))

spisokdline = []
i = 0
for i in range(hisloline):
    spisokdline.append(randint(hislo, hislo1))
    spisokdline.sort()
print(spisokdline)
