num = input("Введите четырехзночное число: ")

sum1 = num[0]
sum2 = num[1]
sum3 = num[2]
sum4 = num[3]
print(int(''.join([sum4, sum3, sum2, sum1])))
print(int(''.join([sum2, sum1, sum4, sum3])))
print(int(''.join([sum1, sum3, sum2, sum4])))
print(int(''.join([sum3, sum4, sum1, sum2])))
