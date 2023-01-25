"""
Main part. It controls menus

"""

import menu

def main():
    print("Hello!")
    choic = menu.options()
    if choic == "1":
        menu.first_menu()
    elif choic == "2":
        menu.second_menu()
    elif choic == "3":
        menu.third_menu()
    elif choic == "4":
        menu.fourth_menu()
    elif choic == "5":
        menu.fifth_menu(choic)
    elif choic == "6":
        menu.sixth_menu(choic)
    else: k += 1

main()