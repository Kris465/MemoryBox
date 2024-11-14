apples = int(input("Введите количество яблок: "))
fallen = []

for i in range(apples):
    apple_color = input(f"Введите цвет яблока {i + 1}: ")

    fallen.append(apple_color)

print("Яблоки упали таких цветов:", *fallen)
