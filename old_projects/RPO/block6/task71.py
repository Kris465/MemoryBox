def is_sorted_descending(heights):
    return heights == sorted(heights, reverse=True)


n = int(input("Введите количество учеников: "))
heights = []

for i in range(n):
    height = int(input(f"Введите рост {i + 1} ученика: "))
    heights.append(height)


if is_sorted_descending(heights):
    print("Список упорядочен по убыванию роста.")
else:
    print("Список не упорядочен")
