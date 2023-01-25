"""
Menu

1. options is a start menu. Relying on check_in() it check correct input and continue asking or finishes app if user chose it.


"""

import check
import read_mod


def options():
    print("Hello!")
    choic = ""

    while isinstance(choic, str):
        print("Choose one option: ")
        choic = input("1. Show all \n2. Find information \n3. Add information \n4. Correct information \n5. Delete information \n6. Export/Import \n7. Exit \n")
        ticket = check.check_in(choic, "1234567")
        if choic == "7":
            end_menu("Bye!")
            break
        elif ticket == False:
            end_menu("Sorry, your phrase is incorrect, try again.")
            continue
        else: return choic

def first_menu(use_choice):
    bus_line = read_mod.reader(use_choice)
    end_menu(bus_line)

def second_menu():
    in_str = print("What kind of information would you like? \n1. Lines \n 2. Columns")
    if check.check_in(in_str, "12"):
        if in_str == "1":
            line = input("Input the number your wished line: ")
            if check.check_in(line, "123456789"):
                return int(line)
            else: 
                end_menu("You added something strange.")
                return False
        else:
            columns = input("Input numbers your wished columns using space: ")
            if check.check_in(columns, "123456789 "):          
                columns.split()
                return list(columns)
            else:
                end_menu("You added something strange.")
                return False
    else: return False


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
