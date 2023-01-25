"""
Menu

options is a start menu.
first_menu is reading the whole file
second_menu is reading line and column

"""

import check
import read_mod
import write_mod

def options():
    print("Choose one option: ")
    choic = input("1. Show all \n2. Find information \n3. Add information \n4. Correct information \n5. Delete information \n6. Export/Import \n7. Exit \n")
    ticket = check.check_in(choic, "1234567")
    if choic == "7":
        end_menu("Bye!")
    elif ticket == False:
        end_menu("Sorry, your phrase is incorrect, try again.")
    else: return choic

def first_menu():
    everything = read_mod.reader("0")
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
    print("What would you like to add? ")
    lst = [input() for i in range(4)]
    lst.append(0)
    answer = write_mod.writer(lst)
    end_menu(answer)

def fourth_menu():
    first_menu()
    num_line = input("Which line would you like to correct?")
    num_line = check.check_in(num_line, "1234567890")
    lst = [input() for i in range(4)]
    lst.append(num_line)
    lst.append(1)
    answer = write_mod.writer(lst)
    


def fifth_menu():
    pass # delete information

def sixth_menu():
    pass # export\import

def end_menu(output):
    print(output)
