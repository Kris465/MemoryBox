"""
This module checks user string for correct input

it gets string and returns list
first check returns False if there isn't a space in user's string
second check returns the type of operation
third check returns string to menu, if it is invalid
fourth check report about divining by zero
fifth check formats s-string to give it to calculator
"""

import logg
from end_menu import output

def errors(users_string):
    ch1 = first_check(users_string)
    logg.logging.info(f"first check: {ch1}")

    if ch1 == False:
        print("I couldn't find statement in your input.")
        output(users_string)
        
    ch3 = third_check(users_string)
    logg.logging.info(f"third check: {ch3}")   
    
    if ch3 != users_string:
            print("Please, check it again.")
            output(ch3)
    
    ch4 = fourth_check(users_string)
    logg.logging.info(f"fourth check: {ch4}")

    if ch4 == users_string:
        use_lst = users_string.split()
    else: return users_string

    if "s" in users_string:
        ch5 = fifth_check(use_lst)
        logg.logging.info(f"fifth check: {ch5}")
        return ch5
    else: return use_lst
    

def first_check(use_string):
    empty = " "
    if empty in use_string:
        return True
    else: return False

def second_check(use_string):
    if "j" in use_string:
        return 2
    else: return 1

def third_check(use_string):
    answer = ""
    k = second_check(use_string)
    if k == 1:
        for el in use_string:
            if el in "^+-%/*s0123456789() ":
                answer += el
            else:
                answer = "invalid character"
                break
    elif k == 2:
        for el in use_string:
            if el in "+-/*0123456789j() ":
                answer += el
            else:
                answer = "invalid character"
                break
    return answer


def fourth_check(use_string):
    indexes = [i + 2 for i in range(len(use_string)) if use_string[i] == "/"]
    answer = use_string
    for ind in indexes:
        if use_string[ind] == "0":
            answer = "division by zero"
        else: answer = use_string

    return answer

def fifth_check(use_lst):
    new_lst = []
    for i in range(len(use_lst)):
        if "s" in use_lst[i]:
            new_lst.append(use_lst[i][1:])
            new_lst.append(use_lst[i][0])
            new_lst.append("0.5")
        else:
            new_lst.append(use_lst[i])

    return new_lst
    




