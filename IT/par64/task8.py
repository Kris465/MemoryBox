from random import randint

N = 1000
a = []
raz = 0
for i in range(N):
    a.append(randint(1, 99))
print(a)
for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            raz += 1
        a[j], a[j + 1] = [j + 1], a[j]
print(a, f'Колличество перествновок: {raz}')
