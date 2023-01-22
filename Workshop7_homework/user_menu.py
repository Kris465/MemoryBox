"""
There is a user menu.

Only this module is shown to user.

input_menu calls sub_menu to get user's string
output_menu shows user a result. It calls in main

"""
from exception import errors

def input_menu():
    print("Hello! I'm a calculator. Let's count? \n")
    print('''Input your statement usually: -2 + 3. 
    For addition: '+' 
    For subtraction: '-' 
    For multiplication: '*' 
    For divining: '/'
    For divining without  fraction: '//'
    For fraction from divining: '%'
    For power: '^' 
    For square root put 's' before the number.\n
    For complex numbers you shoul use: -2+3j. Without spaces inside the number. If you don't have any value before j, you should put 1, like: 6+1j''')
    print("Don't forget to separete '(' and ')' with spaces.\n")

    result = " "

    while isinstance(result, str):
        us_string = input("Input your statement. If you want to come back, press 0: \n")
        result = errors(us_string)

    print(result)
    return result

def output_menu(result_in_main):
    print("Your answer is: ", result_in_main)

