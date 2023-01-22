"""
This module checks user string for correct input

It gets string and returns list
first check returns False if there isn't a space in user's string
Second check returns the type of operation
third check returns False if divining on zero
# Третья проверка на знаки в строке, должны быть только необходимые знаки
# Обработки - 's' - привести к виду num s 0.5
"""

def errors(users_string):
    ch1 = first_check(users_string)

    use_lst = users_string.split()
    # ch2 = second_check(use_lst)

    return use_lst

def first_check(use_string):
    if " " in use_string:
        return False
    else: return True

def second_check(use_string):
    if "j" in use_string:
        return 2
    else: return 1

def trird_check(use_lst):
    indexes = [i + 1 for i in range(0, len(use_lst)) if use_lst[i] == "/"] # Берем следующие после / индексы в списке
    pass
    




