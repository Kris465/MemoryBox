abc = int(input("Введите число: "))
n1 = abc // 100
n2 = abc // 10 % 10
n3 = abc % 10
acb = n1 * 100 + n3 * 10 + n2
bac = n2 * 100 + n1 * 10 + n3
bca = n2 * 100 + n3 * 10 + n1
cab = n3 * 100 + n1 * 10 + n2
cba = n3 * 100 + n2 * 10 + n1
print(abc)
print(acb)
print(bac)
print(bca)
print(cab)
print(cba)
