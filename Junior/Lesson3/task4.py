def flashcards():
    cards = {
        "apple": "яблоко",
        "banana": "банан",
        "orange": "апельсин",
        "grape": "виноград",
        "peach": "персик"
    }
    
    for english, russian in cards.items():
        answer = input(f"Как переводится '{english}'? ")
        if answer.lower() == russian:
            print("Правильно!")
        else:
            print(f"Неправильно! Правильный ответ: {russian}")


flashcards()
