"""
The MAIN module

This module is a point of entry. So run it to run the app

"""

from user_menu import input_menu
from user_menu import output_menu
from mod1 import calculator
from mod1 import cut

def main():
    use_lst = input_menu()
    result = calculator(cut(use_lst))
    output_menu(result)

main()