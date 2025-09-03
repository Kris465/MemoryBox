from random import randint


def guess_number():
    number = randint(1, 100)
    guess = None
    attempts = 0

    while guess != number:
        guess = int(input("Угадай число от 1 до 100: "))
        attempts += 1
        if guess < number:
            print("Слишком маленькое число!")
        elif guess > number:
            print("Слишком большое число!")

    print(f"Поздравляем! Вы угадали число {number} за {attempts} попыток")


guess_number()
