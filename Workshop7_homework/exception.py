"""
This module checks user string for correct input

It gets string and returns list
first check returns False if there isn't a space in user's string
Second check returns the type of operation
third check returns False if divining on zero
# Третья проверка на знаки в строке, должны быть только необходимые знаки
# Обработки - 's' - привести к виду num s 0.5
"""

import logg

def errors(users_string):
    ch1 = first_check(users_string)
    logg.logging.info(f"first check: {ch1}")
    ch3 = third_check(users_string)
    logg.logging.info(f"third check: {ch3}")
    
    if ch3 != users_string:
        print(ch3)
        return users_string

    
        
    use_lst = users_string.split()

    return use_lst

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
    k = second_check(use_string)
    if k == 1:
        for el in use_string:
            if el in "^+-%/*s0123456789 ":
                return use_string
            else:
                return "invalid character"
    if k == 2:
        for el in use_string:
            if el in "+-/*0123456789j ":
                return use_string
            else:
                return "invalid character"

def fourth_check(use_lst):
    indexes = [i + 1 for i in range(0, len(use_lst)) if use_lst[i] == "/"] # Берем следующие после / индексы в списке
    pass

def fifth_check(use_lst):
    if "s" in use_lst:
        k = use_lst.index("s")
        if use_lst[k + 1].isdigit() or use_lst[k + 2].isdigit():
            !!!!!!!
    




