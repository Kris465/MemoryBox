chislo = input("Введите число: ")
cifra = [int(i) for i in chislo]
min_num = min(cifra)
count = 0
for i in cifra:
    if i == min_num:
        count += 1
        
print("Наименьших цифр:", count)