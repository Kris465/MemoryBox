# 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"

# out

# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']}, 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}

def names_dictionary():
    num = int(input("How many names would you like to input?: "))
    users_names = [input() for i in range(num)]
    keys_surs = {[name[name.find(" ") + 1] for name in users_names]}
    keys_names = sorted([name[0] for name in users_names])
    i = 0
    s = 0
    n = 0

    while i < num:
        ls = []
        if users_names[i][0] == keys_names[n] and keys_surs[s] in users_names[i]:
            ls.append(users_names[i])
            n += 1
        dictionary = {keys_surs[s]: {keys_names: ls}}
        i += 1
        s += 1

    print(keys_surs, keys_names)

names_dictionary()
