n = int(input("введите наткральное число n: "))


number = []
for i in range(n):
    num = float(input(f"Введите вещественное число a{i+1}: "))
    number.append(num)


total_sum = sum(number)


print("сумма всех веществ чисел:", total_sum)
