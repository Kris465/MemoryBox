# Здесь интерфейс


def start_menu():
    
    print('Добро пожаловать в калькулятор. С какими числами работаем?')
    print('1 - Рациональные?')
    print('2 - Комплексные?')
    print('3 - Выход')
    
    match menu_point:= input('Выберите пункт меню '):
        case '1':
            get_value()
        case '2':
            get_value()
        case '3':
            print('Заходите ещё! Всегда будем рады!')
    if menu_point != '3':
        start_menu() 

def view(data):
    print(data)


def get_value():
    return input("Input you operation. Please separate numbers from the sign of operation with space: ") # число пробел знак пробел число

def srch(inp):
    result = []
    n = 0
    for i in range(len(inp)):
        if inp[i] in ("+", "-", "*", "/"):
            result.append(int(inp[n:i]))
            result.append(inp[i])
            n = i + 1
    result.append(int(inp[i:]))
    return result

def output(result):
    if str(result).isdigit():
        print(f"Your result is:", *result)
    else: print(result)

start_menu()
