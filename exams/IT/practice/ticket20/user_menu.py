from random import randint
from calculate import Calculator


class User_menu:
    def __init__(self):
        self.us_input = ""
        self.start_num = 0
        self.end_num = 0

    def logic(self):
        num1, num2, sign = self.user_input()
        calc = Calculator(num1, num2)
        match sign:
            case "+":
                result = calc.sum_up()
            case "-":
                result = calc.minus()
            case ":":
                result = calc.delen()
            case "/":
                result = calc.delen()
            case "*":
                result = calc.ymnoz()
            case "**":
                result = calc.v_stepen()
            case "pow":
                result = calc.korenb()
            case "abs":
                result = calc.module()
            case "log":
                result = calc.log()
            case "sin":
                result = calc.sin()
            case "cos":
                result = calc.cos()
            case "round":
                result = calc.okryglenie()
        self.user_output(result)

    def user_input(self):
        # возвращает num1 num2 sign
        spisok = []
        user_string = input("Введите выражение: ")
        for char in user_string:
            spisok.append(char)
        print(spisok)
        return 1, 1, "+"
        # num1 = int(user_list[0])
        # num2 = int(user_list[2])
        # sign = user_list[1]
        # return num1, num2, sign

    def checking_the_expression_formatting(self):
        # проверка выражения
        pass

    def user_output(self, result):
        print(f"Ваш ответ: {result}")

    def random_num(self):
        return randint(self.start_num, self.end_num)
