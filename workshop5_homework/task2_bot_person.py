# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint


def sweets_game():
    name = input("What's your name? ")
    sweets = int(input("How many sweets do we have? "))
    step = int(input("How many sweets will we take at once? "))
    if input("Imput 'yes' if you want to take sweets first, otherwise I'll be first: ") == 'yes':
        current_turn = True
    else: current_turn = False

    while sweets > 0:
        if current_turn == True:
            user_action = int(input(f"Your turn, {name}, take sweets, please: "))
            while user_action > step:
                print(f"You can't take more sweets than {step}. Try again!")
                user_action = int(input())
            if user_action > sweets:
                yes_mes = input(f"You can take just {sweets}. Would you like take them and win? Input 'yes'.")
                if yes_mes == 'yes':
                    print("Congratulations!")
                else: print("Thank you, so I won!")
            sweets -= user_action
            current_turn = False
        else:
            print("Oh, it's my turn!")
            my_action = randint(1, step)
            print(f"I'll take {my_action}")
            if sweets < my_action and sweets != 0:
                my_action = sweets
            else:
                sweets -= my_action
                current_turn = True

        if sweets > 0:
            print(f"There are {sweets} sweets.")
        elif sweets <= 0:
            print(f"There are 0 sweets")
            if current_turn == True:
                print("I have won!")
            else: print("You have won!")

sweets_game()
