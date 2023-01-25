"""
Menu

1. options is a start menu.


"""

import check
import read_mod

def options():
    print("Choose one option: ")
    choic = input("1. Show all \n2. Find information \n3. Add information \n4. Correct information \n5. Delete information \n6. Export/Import \n7. Exit \n")
    ticket = check.check_in(choic, "1234567")
    if choic == "7":
        end_menu("Bye!")
    elif ticket == False:
        end_menu("Sorry, your phrase is incorrect, try again.")
    else: return choic

def first_menu(use_choice):
    everything = read_mod.reader("0" + use_choice)
    end_menu(everything)

def second_menu():
    in_str = input("What kind of information would you like? \n1. Line \n2. Column \n")
    if check.check_in(in_str, "12"):
        if in_str == "1":
            line = input("Which line would you like to see?\n")
            inf = in_str + line
            answer = read_mod.reader(inf)
        else: 
            column = input("Whick column would you like to see?\n")
            inf = in_str + column
            answer = read_mod.reader(inf)

        end_menu(answer)
    else: end_menu("Incorrect input!")

def third_menu():
    pass # add information

def fourth_menu():
    pass # correct information

def fifth_menu():
    pass # delete information

def sixth_menu():
    pass # export\import

def end_menu(output):
    print(output)
