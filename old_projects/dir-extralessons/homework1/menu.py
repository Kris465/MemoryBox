"""

User_menu

1. First menu - input
2. Second menu - subinput (string)
3. Third menu - output
"""

from exceptions import num_input_check

def first_menu():
    print("1. Show the list \n2. Add element at the end of the list \n3. Delete the last element \n4. Exit")

    result = ""
    while isinstance(result, str):
        user_str = input("Input your choice, please: ")
        result = num_input_check(user_str)
    
    return result

def second_menu(use_num, ls):
    if use_num == 2:
        elem = input("Input the element that you wish to add: ")
        ls.append(elem)
        print("Success!")
    else:
        del(ls[-1])
        print("Success!")
    
    return ls


def third_menu(something):
    print(something)
