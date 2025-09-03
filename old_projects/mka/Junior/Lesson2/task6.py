def favorite_character():
    characters = ["Губка Боб", "Патрик", "Скуби-Ду"]
    print("Выберите своего любимого персонажа:")

    for i, character in enumerate(characters, start=1):
        print(f"{i}. {character}")

    choice = int(input("Введите номер вашего выбора: ")) - 1
    if 0 <= choice < len(characters):
        print(f"Ваш любимый персонаж: {characters[choice]}")
    else:
        print("Неверный выбор.")


favorite_character()
