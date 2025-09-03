def guess_who():
    questions = [
        "Это животное? (да/нет)",
        "Он/она говорит? (да/нет)",
        "Это главный герой? (да/нет)"
    ]

    answers = []

    for question in questions:
        answer = input(question + " ").lower()
        answers.append(answer)

    if answers == ['да', 'да', 'да']:
        print("Это может быть Губка Боб!")
    elif answers == ['да', 'нет', 'нет']:
        print("Это может быть Симба!")
    else:
        print("Я не знаю, кто это!")


guess_who()
