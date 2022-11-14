# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

def calc(action):
    data = action.split()
    sign = data[1]

    if sign == "+":
        answer = float(data[0]) + float(data[2])
    elif sign == "-":
        answer = float(data[0]) - float(data[2])
    elif sign == "*":
        answer = float(data[0]) * float(data[2])
    elif sign == "/":
        if data[2] == "0":
            answer = "division for zero"
        else: answer = float(data[0]) / float(data[2])
    else: answer = "Something unexpected happened"

    return answer

