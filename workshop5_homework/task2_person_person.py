# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

def sweet_game():
    player1 = input("Input first player's name: ")
    player2 = input("Input second player's name: ")
    sweets = int(input("How many sweets do we have? "))
    step = int(input("How many sweets would you like to take at once? "))

    while sweets > 0:
        print(f"Your turn, {player1}: ")
        play1 = int(input())
        while play1 > step or step > sweets:
            print(f"You should take less {step} sweets or leftover sweets.")
            play1 = int(input())
            if sweets - play1 == 0:
                winner = player1
        else:
            sweets -= play1
            print(f"There are {sweets} sweets.")
            winner = player1
        

        print(f"Your turn, {player2}: ")
        play2 = int(input())
        while play2 > step or step > sweets:
            print(f"You should take less {step} sweets or leftover sweets.")
            play2 = int(input())
            if sweets - play2 == 0:
                winner = player2
        else:
            sweets -= play2
            print(f"There are {sweets} sweets.")
            winner = player2
            
    print(f"The winner is {winner}")
    
sweet_game()