n = int(input('Введите число: '))
all_a = {
    'a0': 1
}
a0 = 0

for i in range(1, n + 1):
    all_a[f'a{i}'] = round(i * all_a[f'a{i - 1}'] + 1/i, 2)

for i in range(len(all_a)):
    print(f'a{i}   =  {all_a[f'a{i}']}')
