num = input("Введите трехзначное число: ")

print(num[::-1])

n1 = num[0]
n2 = num[1]
n3 = num[2]

print(f"{n3}{n2}{n1}")

n1 = int(num) // 100
n2 = (int(num) // 10) % 10
n3 = int(num) % 10

print(f"{n3}{n2}{n1}")
