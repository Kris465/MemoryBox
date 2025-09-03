import random

riddles = {
    "Что всегда идет, но никогда не приходит?": "Время",
    "Что можно увидеть один раз в минуту, дважды в моменте, но ни разу в тысяче лет?": "Буква 'м'",
}


riddle, answer = random.choice(list(riddles.items()))
user_answer = input(riddle + " ")
if user_answer.lower() == answer.lower():
    print("Правильно!")
else:
    print(f"Неправильно! Правильный ответ: {answer}.")
