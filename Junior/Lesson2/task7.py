def characters_starting_with_letter():
    characters = ["Микки Маус", "Супермен", "Дональд Дак", "Губка Боб"]
    letter = input("Введите букву: ").upper()

    found_characters = [char for char in characters if char.startswith(letter)]
    if found_characters:
        print("Персонажи, начинающиеся на букву", letter + ":")
    for char in found_characters:
        print(char)
    else:
        print("Нет персонажей на эту букву.")


characters_starting_with_letter()
