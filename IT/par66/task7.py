def replace_all_recursive(s, old, new):
    if old not in s:
        return s
    return replace_all_recursive(s.replace(old, new, 1), old, new)


input_string = input("Введите строку: ")
result_recursive = replace_all_recursive(input_string, 'а', 'б')
print("Рекурсивный результат:", result_recursive)
