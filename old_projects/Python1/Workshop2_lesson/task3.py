# 3. Напишите программу, в которой пользователь будет задавать две строки,
#    программа - определять количество вхождений одной строки в другой.

def two_lines():
    line_1 = input("Input your line: ")
    line_2 = input("Input your line: ")
    print(line_1.count(line_2))

two_lines()