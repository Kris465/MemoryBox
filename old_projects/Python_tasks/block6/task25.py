spisok = []
user_input = ''
while user_input != '0':
    user_input = input("Введите число и в конце введите 0: ")
    spisok.append(user_input)


flag = 0
counted = 0
for i in spisok:
    old_flag = flag
    if int(i) < 0:
        flag = True
    else:
        flag = False
    
    if old_flag != flag:
        counted += 1
    

print(counted)