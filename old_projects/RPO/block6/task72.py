def is_sorted_descending(heights):
    return heights == sorted(heights, reverse=True)


n = int(input("Введите кол-во команд: "))
heights = []

for i in range(n):
    height = int(input(f"Введите сколько очков у {i + 1} команды: "))
    heights.append(height)


if is_sorted_descending(heights):
    print("Список упорядочен по занятым местам.")
else:
    print("Список не упорядочен")
