"""
The MAIN module

This module is a point of entry. So run it to run the app

"""

import logg
from user_menu import input_menu
from user_menu import output_menu
import mod1
import mod2
from exception import second_check

def main():
    use_lst = input_menu()

    ch2 = second_check(str(use_lst))
    logg.logging.info(f"second check (1 - numbers, 2 - complex): {ch2}")
    if ch2 == 1:
        temp = mod1.cut(use_lst)
        result = mod1.calculator(temp)
    else:
        temp = mod2.cut(use_lst)
        result = mod2.calculator(temp)

    output_menu(result)


main()