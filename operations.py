# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

def calc(data):

    if 'j' in data:
        answer = "Complex numbers"
    else:
        sign = data[1]
    
        if sign == "+":
            answer = int(data[0]) + int(data[2])
        elif sign == "-":
            answer = int(data[0]) - int(data[2])
        elif sign == "*":
            answer = int(data[0]) * int(data[2])
        elif sign == "/":
            if data[2] == "0":
                answer = "division for zero"
            else: answer = int(data[0]) / int(data[2])
        else: answer = "Something unexpected happened"

    return answer

