def characters_by_color():
    characters = {
        "желтый": ["Губка Боб", "Патрик"],
        "красный": ["Супермен", "Спайдермен"],
        "синий": ["Соник", "Дарт Вейдер"],
    }

    color = input("Введите цвет: ").lower()

    if color in characters:
        print("Персонажи этого цвета:", ", ".join(characters[color]))
    else:
        print("Нет персонажей этого цвета.")


characters_by_color()
