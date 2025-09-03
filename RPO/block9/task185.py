
expression = "(a + (b * c) - (d / e))"


def check_expression_brackets(expression):
    balance = 0
    for char in expression:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return "нет"
    return "да" if balance == 0 else "нет"


print("9.185 а)", check_expression_brackets(expression))


def check_expression_brackets_extended(expression):
    balance = 0
    for i, char in enumerate(expression):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return f"Лишняя закрывающая скобка на позиции {i}"
    if balance > 0:
        return f"Лишних открывающих скобок: {balance}"
    return "Скобки расставлены правильно"


print("9.185 б)", check_expression_brackets_extended(expression))
