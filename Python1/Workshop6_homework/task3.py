# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def names_dictionary():
    num = int(input("How many names would you like to input?: "))
    names = sorted([input() for i in range(num)])
    dictionary = {}
    for i in names:
        letter = i[0]
        if letter not in dictionary:
            dictionary[letter] = [i]
        else:
            dictionary[letter] += [i] 
    return dictionary

print(names_dictionary())
