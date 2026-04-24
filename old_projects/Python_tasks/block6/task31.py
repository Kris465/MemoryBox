chislo = input("Введите число: ")
cifra = [int(i) for i in chislo]
max_num = max(cifra)
count = 0
for i in cifra:
    if i == max_num:
        count += 1
        
print("Наибольших цифр:", count)