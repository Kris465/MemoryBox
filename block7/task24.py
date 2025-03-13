spisok = []
user_input = ''
while user_input != 'exit':
    num = int(input("Введите количество учащихся: "))
    spisok.append(num)

total_students = sum(spisok[i] for i in range
                     (0, len(spisok), 2))
print("Общее число детей в нечетных классах: ", total_students)
exit
