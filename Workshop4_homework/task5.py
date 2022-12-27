# ** 5. Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!

def reading_file(file):
    with open(file, 'r') as data:
        pol = data.read()
    return pol

def clearing(polinom):
    polinom = polinom[:-5]
    polinom = polinom.replace("- ", "+ -" )
    for parts in polinom:
        polinom = polinom.replace("*x^", " ")
        parts = polinom.split()
    for part in parts:
        if "+" in part:
            parts.remove(part)
        else:
            continue

    poli = []
    for i in parts:
        for k in i:
            if k.isdigit() and i[0] == '-':
                poli.append(-int(k))
            elif k.isdigit():
                poli.append(int(k))
            else:
                continue
    
    return(poli)

def summing_up(pol1, pol2):
    sum_lst = []

    if len(pol1) > len(pol2):
        length_pol = len(pol1)
    else:
        length_pol = len(pol2)

    a = 1
    b = 1

    while length_pol // 2 > 0:
        try:
            if pol1[a] == pol2[b]:
                sum_lst.append(pol1[a - 1] + pol2[b - 1])
                a += 2
                b += 2
                length_pol -= 1
            elif pol1[a] > pol2[b]:
                sum_lst.append(pol1[a - 1])
                a += 2
                length_pol -= 1
            elif pol1[a] < pol2[b]:
                sum_lst.append(pol2[b - 1])
                b += 2
                length_pol -= 1
            else: print("!!!")
        except:
            break

    sum_lst.reverse()
    return sum_lst, length_pol

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
    text_to_file = open("task5_output.txt", "a") # Здесь можно поменять название файла на task5_input.txt чтобы сделать многочлен для 5 
    text_to_file.write(pol + "\n")
    text_to_file.close

first = clearing(reading_file("task4.txt"))
second = clearing(reading_file("task5_input.txt"))
new_lst, number = summing_up(first, second)
file_writing(new_lst, number)
