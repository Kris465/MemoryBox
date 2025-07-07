def run_quiz():
    country = {
        "Франция": "Париж",
        "Россия": "Москва",
        "Беларусь": "Минск",
        "Италия": "Рим",
        "Германия": "Берлин",
        "Турция": "Стамбул",
        "Египет": "Каир",
        "Швейцария": "Берн",
    }
    score = 0
    print("Напишите столицу для каждой страны")
    for country, capital in country.items():
        answer = input(f"Напишите столицу этой страны: {country}\n ").strip()
        if answer.lower() == capital.lower():
            print("Правильно\n")
            score += 1
        else:
            print(f"Неправильно. Правильный ответ: {capital}\n")
            score -= 1
    print(f"Ваш результат: {score}")


run_quiz()
