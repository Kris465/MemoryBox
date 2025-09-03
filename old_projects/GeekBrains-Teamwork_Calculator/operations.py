# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

def calc(data):

    if 'j' in data:
        print(data)
        sign = data[4]
        if sign == "+":
            answer = str(float(data[0]) + float(data[5])) + "+" + str(float(data[2]) + float(data[7])) + "j"
        elif sign == "-":
            answer = str(float(data[0]) - float(data[5])) + "-" + str(float(data[2]) - float(data[7])) + "j"
        elif sign == "/":
            answer = str((float(data[0]) * float(data[5]) + float(data[2]) * float(data[7])) / (float(data[5]) ** 2 + float(data[7]) ** 2)) + "+" + str((float(data[5]) * float(data[2]) - float(data[0]) * float(data[7])) / (float(data[5]) ** 2 + float(data[7]) ** 2)) + "j"
        elif sign == "*":
            answer = str(float(data[0]) * float(data[5]) - float(data[2]) * float(data[7])) + "+" + str(float(data[0]) * float(data[7]) + float(data[2]) * float(data[5])) + "j"
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

