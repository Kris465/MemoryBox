# Подумайте как наделить бота "интеллектом"

def sweets_game():
    print("Hello! Nobody wants to lose, so let's have some fun!")
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
            k = sweets % 2
            my_action = 0
            if 1 < k and k < step:
                my_action = k
            elif k == 0:
                my_action = step - 1
            elif sweets < step and sweets != 0:
                if k == 0:
                    my_action = sweets - 2
                else: my_action = sweets - 1
            else: my_action = step
            
            print(f"I'll take {my_action} sweets.")
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
