# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

def calc(input_dict):

    current = input_dict.get('useroperation')

    if current == None:
        answer = "Попробуйте еще раз"
    else:
        cur_data = current.replace('j', ' ')
        data = cur_data.split()
        
    if 'j' in current:
        sign = data[3]
        if sign == "+":
            answer = str(float(data[0]) + float(data[4])) + "+" + str(float(data[2]) + float(data[6])) + "j"
        elif sign == "-":
            answer = str(float(data[0]) - float(data[4])) + "-" + str(float(data[2]) - float(data[6])) + "j"
        elif sign == "/":
            answer = str((float(data[0]) * float(data[4]) + float(data[2]) * float(data[6])) / (float(data[4]) ** 2 + float(data[6]) ** 2)) + "+" + str((float(data[4]) * float(data[2]) - float(data[0]) * float(data[6])) / (float(data[4]) ** 2 + float(data[6]) ** 2)) + "j"
        elif sign == "*":
            answer = str(float(data[0]) * float(data[4]) - float(data[2]) * float(data[6])) + "+" + str(float(data[0]) * float(data[6]) + float(data[2]) * float(data[4])) + "j"
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
                answer = "Деление на ноль!"
            else: answer = int(data[0]) / int(data[2])
        else: answer = "Нежданчик!"

    return answer

