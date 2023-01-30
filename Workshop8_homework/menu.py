"""
Menu

options is a start menu.
first_menu is reading the whole file
second_menu is reading line and column
third_menu adds line at the end of the file
fourth_menu loads information from file, adds one line in asked index and writes back to the file
fifth_menu loads information from file and deletes asked line with pop()
sixth_menu reads - writes (csv - txt, txt - csv)
"""

import check
import read_mod
import write_mod


def options():
    print("Choose one option: ")
    choic = input("1. Show all \n2. Find information \n3. Add information \n4. Correct information \n5. Delete information \n6. Export/Import \n")
    ticket = check.check_in(choic, "1234567")
    if choic == "7":
        end_menu("Bye!")
    elif ticket == False:
        end_menu("Sorry, your phrase is incorrect, try again.")
    else: return choic


def first_menu():
    everything = read_mod.reader("0")
    return everything


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
    lst = first_menu()
    print("What would you like to add? ")
    add_lst = [input() for i in range(4)]
    lst.append(add_lst)
    write_mod.writer(lst)
    end_menu(first_menu())


def fourth_menu():
    all_inf = first_menu()
    end_menu(all_inf)
    num_line = input("Which line would you like to correct?\n")
    num_line = check.check_in(num_line, "1234567890")
    if num_line == True:
        lst = [input() for i in range(4)]
        all_inf.insert(num_line, lst)
        all_inf.pop(num_line + 1)
        write_mod.writer(all_inf)
        end_menu(first_menu())
    else: end_menu("Sorry, try again.")


def fifth_menu():
    all_inf = first_menu()
    end_menu(all_inf)
    num_line = input("Which line would you like to delete?\n")
    num_line = check.check_in(num_line, "1234567890")
    all_inf.pop(num_line)
    write_mod.writer(all_inf)
    end_menu(first_menu())


def sixth_menu():
    in_str = input("1. Export\n2. Import\n")
    checked_str = check.check_in(in_str, "12")

    if checked_str == True:
        if in_str == "1":
            all_inf = first_menu()
            with open("eximp.txt", "w") as f:
                for elem in all_inf:
                    elem = ",".join([ch for ch in elem if ch != "[" or ch != "]"])
                    f.write(elem + "\n")
        else:
            ls = []
            with open("eximp.txt", "r") as f:
                for line in f:
                    ls.append(line.rstrip().split(','))
            # lst = first_menu()
            # lst.append(ls)
            write_mod.writer(ls)
    else: 
        print("Try again.")

    end_menu(first_menu())


def end_menu(output):
    if isinstance(output, list):
        for i in range(len(output)):
            print(*output[i])
    elif isinstance(output, str):
        print(output)
    elif isinstance(output, int):
        print(output)
