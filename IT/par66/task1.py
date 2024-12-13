def replace_letters(input_string):
    result = ""
    for char in input_string:
        if char == 'a':
            result += 'б'
        elif char == 'б':
            result += 'a'
        elif char == 'Б':
            result += 'A'
        else:
            result += char
    return result


input_str = "абсABC"
output_str = replace_letters(input_str)
print("Результат:", output_str)
