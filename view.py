# Здесь интерфейс
from os import system

def start_menu():
    system('cls')
    print('Добро пожаловать в калькулятор. С какими числами работаем?')
    print('1 - Рациональные?')
    print('2 - Комплексные?')
    print('3 - Выход')
    
    match menu_point:= input('Выберите пункт меню '):
        case '1':
            get_value1()
        case '2':
            get_value2()
        case '3':
            print('Заходите ещё! Всегда будем рады!')
    if menu_point != '3':
        start_menu() 

def view(data):
    print(data)

def get_value1():
    return input("Input you operation. Please separate numbers from the sign of operation with space: ") # число пробел знак пробел число

def get_value2():
    return input("Input you operation. Please separate numbers from the sign of operation with space: ") # комплексные?

def output(result):
    if str(result).isdigit():
        print(f"Your result is:", *result)
    else: print(result)

start_menu()
