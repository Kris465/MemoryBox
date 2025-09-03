def cartoon_by_character():
    characters_to_cartoons = {
        "Микки Маус": "Микки Маус",
        "Супермен": "Супермен",
        "Губка Боб": "Губка Боб Квадратные Штаны",
    }

    character = input("Введите имя персонажа: ")

    if character in characters_to_cartoons:
        print(f"{character} появляется в мультфильме '{
            characters_to_cartoons[character]}'.")
    else:
        print("Извините, я не знаю этот персонаж.")


cartoon_by_character()
