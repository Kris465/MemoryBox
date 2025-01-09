from random import choice


def guess_the_word():
    words = ["python", "программирование",
             "машинное", "обучение", "искусственный"]
    word_to_guess = choice(words)
    guessed_letters = []

    while True:
        display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word_to_guess)
        print(f"Слово: {display_word}")

        guess = input("Угадайте букву: ").lower()

        if guess in word_to_guess:
            guessed_letters.append(guess)
            print("Правильно!")
        else:
            print("Неправильно!")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Поздравляем! Вы угадали слово '{word_to_guess}'")
            break


guess_the_word()
