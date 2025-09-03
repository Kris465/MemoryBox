n = input("Введите натуральное число: ")
is_non_decreasing = True
for i in range(len(n) - 1):
    if n[i] > n[i + 1]:
        is_non_decreasing = False
        break
if is_non_decreasing:
    print("Цифры упорядочены по неубыванию при просмотре слева направо.")
else:
    print("Цифры не упорядочены по неубыванию при просмотре слева направо.")
