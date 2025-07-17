kotlet = int(input("Сколько котлет нужно приготовить Губке Бобу?"))

for kotleta in range(kotlet):
    if kotleta <= 20:
        print(f"Котлета {kotleta + 1} готова! Плюшкинс доволен!")
    else:
        print(f"Ой-ой, ингредиенты закончились на котлете {kotleta + 1}!")
