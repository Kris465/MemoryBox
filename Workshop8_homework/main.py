"""
Main part. It controls menus

"""

import menu

def main():
    k = 0
    while k < 100:
        choic = menu.options()
        if choic == "1":
            menu.first_menu(choic)
        elif choic == "2":
            wished = menu.second_menu()
            if wished != False:
                menu.end_menu(wished)
            else: continue
        elif choic == "3":
            menu.third_menu(choic)
            break
        elif choic == "4":
            menu.fourth_menu(choic)
            break
        elif choic == "5":
            menu.fifth_menu(choic)
            break
        elif choic == "6":
            menu.sixth_menu(choic)
            break
        else: continue

main()