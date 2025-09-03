
n = int(input("Введите натуральное число: "))


n_str = str(n)


is_sorted = True
for i in range(len(n_str) - 1):
    if n_str[i] > n_str[i + 1]:
        is_sorted = False
        break

# Вывод результата
if is_sorted:
    print("Цифры упорядочены по возрастанию при просмотре слева направо.")
else:
    print("Цифры не упорядочены по возрастанию при просмотре слева направо.")
