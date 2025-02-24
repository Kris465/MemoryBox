sum_numbers = 0
count = 0

print("Введите последовательность целых чисел, оканчивающуюся нулём:")
while True:
    num = int(input("Введите число: "))  
    if num == 0:
        break  
    sum_numbers += num  
    count += 1  

print("Сумма всех чисел:", sum_numbers)
print("Количество всех чисел:", count)
