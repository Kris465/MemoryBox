def guess_character():
    hints = {
        "Гарри Поттер": "Он волшебник из Хогвартса",
        "Гермиона Грейнджер": "Очень умная волшебница",
        "Рон Уизли": "Рыжий волшебник, который всегда готов помочь друзьям"
    }

    for character, hint in hints.items():
        answer = input(f"Угадайте персонажа: {hint}")
        if answer == character:
            print("Правильно!")
        else:
            print(f"Неправильно! Это {character}.")


guess_character()
