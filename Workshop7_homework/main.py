"""
The MAIN module

This module is a point of entry. So run it to run the app

"""

from user_menu import input_menu
from user_menu import output_menu
import mod1
import mod2
from exception import second_check
from logg import logger

def main():
    use_lst = input_menu()
    logger()
    k = second_check(str(use_lst))
    print(k)
    if k == 1:
        temp = mod1.cut(use_lst)
        result = mod1.calculator(temp)
    else:
        temp = mod2.cut(use_lst)
        result = mod2.calculator(temp)
    output_menu(result)

main()