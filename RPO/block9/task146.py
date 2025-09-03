def calculate_expression(expr):
    expr = expr.replace(' ', '')
    result = 0
    current_number = ''
    current_sign = '+'

    for char in expr:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                if current_sign == '+':
                    result += int(current_number)
                elif current_sign == '-':
                    result -= int(current_number)
            current_sign = char
            current_number = ''

    if current_number:
        if current_sign == '+':
            result += int(current_number)
        elif current_sign == '-':
            result -= int(current_number)

    return result


text = "3 - 1 + 4 - 2"
result = calculate_expression(text)
print(result)
