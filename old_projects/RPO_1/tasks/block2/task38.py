k = int(input("Введите чило k:"))
stroka = ''
stroka1 = ''
stroka2 = ''

for i in range(101, 150):
    stroka += str(i)

print(stroka)

if k % 3 == 0:
    print(stroka.index(str(k)) + 1)
else:
    print("k не кратно трем!")

j = 1
while j < 150:
    stroka1 += str(j)
    j += 3


if str(k) in stroka1:
    print(stroka.index(str(k)) + 1)
else:
    print("Число не входит в эту последовательность!")

j = 2
while j < 150:
    stroka2 += str(j)
    j += 3

if str(k) in stroka2:
    print(stroka.index(str(k)) + 1)
else:
    print("Число не входит в эту последовательность!")
