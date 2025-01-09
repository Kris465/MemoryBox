def quiz(questions):
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            score += 1
            print("Правильно!")
        else:
            print("Неправильно.")
    print(f"Ваш результат: {score}/{len(questions)}")

# Пример использования
questions = {
    "Кто сильнее: Супермен или Бэтмен?": "Супермен",
    "Какой цвет у костюма Чудо-женщины?": "Красный",
}
quiz(questions)