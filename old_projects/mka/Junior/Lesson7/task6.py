import random


def darth_vader_quotes():
    quotes = [
        "Я твой отец",
        "Сила - это мощная вещь",
        "Не недооценивай силу темной стороны"
    ]

    character = input("Введите имя персонажа (Дарт Вейдер): ")
    if character == "Дарт Вейдер":
        print(random.choice(quotes))
    else:
        print("Персонаж не найден!")


darth_vader_quotes()
