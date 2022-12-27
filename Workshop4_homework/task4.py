# * 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import randint

def random_polinom(user_len):   
    rand_lst = []

    for i in range(1, user_len + 1): 
        rand_lst.append(randint(-9, 9))
           
    print(rand_lst)
    return(rand_lst)

def file_writing(lst, user_len):
    lst_polinom = []
    for i in range(0, user_len):
        if lst[i] > 0: 
            polinom_part = "+ " + str(lst[i]) + "*x^" + str(user_len)
            lst_polinom.append(polinom_part)
            user_len -= 1
        elif lst[i] < 0:
            polinom_part = "- " + str(abs(lst[i])) + "*x^" + str(user_len)
            lst_polinom.append(polinom_part)
            user_len -= 1
        else:
            user_len -= 1

    if "+" in lst_polinom[0]:
        str_lst = str(lst_polinom[0])
        str_lst = str_lst[2:]
        lst_polinom[0] = str_lst

    pol = " ".join(lst_polinom) + " = 0"
    print(pol)
    text_to_file = open("task4.txt", "a") # Здесь можно поменять название файла на task5_input.txt чтобы сделать многочлен для 5 
    text_to_file.write(pol + "\n")
    text_to_file.close


user_number = int(input("Inpit the length of your wished polinom: "))
lst_pol = random_polinom(user_number)
file_writing(lst_pol, user_number)
