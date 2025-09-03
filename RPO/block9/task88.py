def print_between_commas(s):
    first_comma = s.find(',')
    if first_comma != -1:
        second_comma = s.find(',', first_comma + 1)
        if second_comma != -1:
            result = s[first_comma +1 : second_comma].strip()
        else:
            result = s[first_comma+1:].strip()
    else:
        result = ''
    return result


s = input('Введите любой текст в котором есть минимум две ",": ')
print(print_between_commas(s))
