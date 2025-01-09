from random import choice

def rock_paper_scissors():
    options = ["камень", "ножницы", "бумага"]
    computer_choice = choice(options)
    player_choice = input("Выберите (камень, ножницы, бумага): ")

    if player_choice not in options:
        print("Неверный выбор!")
        return
    
    print(f"Компьютер выбрал: {computer_choice}")
    
    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == "камень" and computer_choice == "ножницы") or (player_choice == "ножницы" and computer_choice == "бумага") or (player_choice == "бумага" and computer_choice == "камень"):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")

rock_paper_scissors()
