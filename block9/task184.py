text = "(a + b) * (c - d))"


def check_brackets(text):
    balance = 0
    for char in text:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return "нет"
    return "да" if balance == 0 else "нет"


print("9.184 а)", check_brackets(text))


def check_brackets_extended(text):
    balance = 0
    for i, char in enumerate(text):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return f"Лишняя закрывающая скобка на позиции {i}"
    if balance > 0:
        return f"Лишних открывающих скобок: {balance}"
    return "Скобки расставлены правильно"


print("9.184 б)", check_brackets_extended(text))
