import random


def guess_superpower():
    powers = {
        "Человек-муравей": "Уменьшение размеров и увеличение силы.",
        "Железный человек": "Технологический гений и броня.",
        "Капитан америка": "Суперсила и мастер боевых искусскуств."
    }

    character, power = random.choice(list(powers.items()))

    guess = input("Угадайте суперспособность человека-муравья: ")
    if guess.lower() in power.lower():
        print("Правильно!")
    else:
        print(f"Неправильно! Это {power}")


guess_superpower()
