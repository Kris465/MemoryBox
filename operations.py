# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

def calc(action, kind):
    data = action.split()
    sign = data[1]
    
    if kind == "NUM":
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

    else:
        first_num = complex(data[0])
        second_num = complex(data[2])
        if sign == "+":
            answer = first_num + second_num
        elif sign == "-":
            answer = first_num - second_num
        elif sign == "*":
            answer = first_num * second_num
        elif sign == "/":
            answer = first_num / second_num

    return answer

