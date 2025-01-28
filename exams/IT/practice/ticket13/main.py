import random


def read_words(file_path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        words = file.read().splitlines()
        return words
    
def play_game(words):
    word_to_guess = random.choice(words)
    hidden_word = '_' * len(word_to_guess)


    print("Угадайте слово, оно состоит из", len(word_to_guess), "букв")
    print(hidden_word)


    guessed_letters = set()
    tries = len(word_to_guess) + 10


    while tries > 0 and '_' in hidden_word:
        letter = input("Введите букву").lower()
        if letter in guessed_letters:
            print("Вы уже вводили эту букву.")
        continue

    guessed_letters.add(letter)


    if letter in word_to_guess:
        print("Верно!")
        hidden_word = ''.join([letter if word_to_guess[i] == letter 
                               else hidden_word[i] for i in range(len \
                                   (word_to_guess ))])
    else:
        print("Неверно")
        tries -= 1
    
        print(hidden_word)
        print("Оставлось попыток: ", tries)

    if '_' not in hidden_word:
        print("Поздравляю, вы угадали.")
    else:
        print("Вы проиграли. Слово было: ", word_to_guess)

    
words = read_words('words.txt')
play_game(words)


play_game()
