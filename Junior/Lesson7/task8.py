def superhero_colors():
    colors = {}

    while True:
        superhero = input("Введите имя супергероя: ")
        if superhero.lower() == 'стоп':
            break
        color = input(f"Какой цвет ассоциируется с {superhero}?")
        colors[superhero] = color
        print("Цвета супергероев: ")
        for hero, color in colors.items():
            print(f"{hero}: {color}")


superhero_colors()
