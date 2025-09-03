def guess_character():
    characters = {
        "Микки Маус": "Кто всегда в красных шортах?",
        "Супермен": "Кто летает и спасает мир?",
        "Дональд Дак": "Кто не любит работать?",
    }

    for character, hint in characters.items():
        print(hint)
        answer = input("Ваш ответ: ")
        if answer.lower() == character.lower():
            print("Правильно!")
        else:
            print(f"Неправильно! Правильный ответ: {character}")


guess_character()
