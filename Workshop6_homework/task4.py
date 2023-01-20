# 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"

# out

# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']}, 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}

from collections import OrderedDict

def main_func():
    num = int(input("How many names would you like to input?: "))
    users_names = [input() for i in range(num)]
    
    for name in users_names:
        users_names.setdefault(name.split[1][0], {}).setdefault(name.split[0][0], []).append(name)
        return dict(OrderedDict(sorted(users_names.items(), k=lambda x: x[0])))
    
    
print(main_func())
