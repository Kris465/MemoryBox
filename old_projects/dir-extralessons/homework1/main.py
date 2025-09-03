"""

There is the main module

"""

import os
from menu import first_menu
from menu import second_menu
from menu import third_menu

def main():
    print("Hello!")
    ls = []
    choic = first_menu()
    os.system('cls' if os.name == 'nt' else 'clear')

    while choic != 4:
        if choic == 1:
            print("Your list is: ")
            third_menu(ls)
            choic = first_menu()
            os.system('cls' if os.name == 'nt' else 'clear')
        else: 
            ls = second_menu(choic, ls)
            choic = first_menu()
            os.system('cls' if os.name == 'nt' else 'clear')
    
    third_menu("Bye!")

main()
