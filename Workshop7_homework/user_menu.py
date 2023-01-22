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
    For square root put 's' before the number.\n''')
    print("Don't forget to separete '(' and ')' with spaces.\n")

    result = " "

    while isinstance(result, str):
        us_string = sub_menu()
        result = errors(us_string)

    print(result)
    return result, kind

def sub_menu():
    c = 0

    options = input("What kind of numbers would you like to count? \n 1 - rational numbers \n 2 - complex numbers \n 3 - exit \n")
    if options == "1":
        print("Thank you!")
        user_string = input("Input your statement. Please, separate symbols from numbers. If you want to come back, press 0: \n")
    elif options == "2":
        print("So nice from you!")
        user_string = input("Input you statemen. Plese, separate symbols from numbers, but symbol 'j' you don't have to separate. If you want to come back, press 0: \n")
    elif options == "3" or c == 100:
        print("Good bye!")
        user_string = " "
    else: 
        print("I didn't understand you, try again: ")
        c += 1

    return user_string

def output_menu(result_in_main):
    print("Your answer is: ", result_in_main)

