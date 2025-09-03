n = int(input("Введите натуральное число: "))

n_str = str(n)

is_sorted = True
for i in range(len(n_str) - 1):
    if n_str[len(n_str) - 1 - i] > n_str[len(n_str) - 2 - i]:
        is_sorted = False
        break


if is_sorted:
    print("Цифры упорядочены по возрастанию при просмотре справа налево.")
else:
    print("Цифры не упорядочены по возрастанию при просмотре справа налево.")
