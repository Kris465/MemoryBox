# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import re
import itertools

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

def clear_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]

    for i in pol:
        if i[0] == 'x':
            i.insert(0, 1)
        if i[-1] == 'x':
            i.append(1)
        if len(i) == 1:
            i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]

    return pol

def sum_up(pol1, pol2):
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))

    for i in pol1 + pol2:
        x[i[1]] += i[0]
    coef_degr = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    coef_degr.sort(key = lambda r: r[1], reverse = True)

    print(coef_degr)
    return coef_degr

def sum_up_polinom(lst):
    var = ['*x^'] * len(lst)
    coefs = [x[0] for x in lst]
    degr = [x[1] for x in lst]
    new_pol = [[str(a), str(b), str(c)]
               for a, b, c in (zip(coefs, var, degr))]

    for x in new_pol:
        x.append(' + ')
    new_pol = list(itertools.chain(* new_pol))
    new_pol[-1] = ' = 0'
    print("".join(map(str, new_pol)).replace(' 1*x', ' x'))
    return "".join(map(str, new_pol)).replace(' 1*x', ' x')


# Get it!
pol1 = read_pol("task4.txt")
pol2 = read_pol("task5.txt")
print(pol1, pol2)

# clear it!
cl_pol1 = clear_pol(pol1)
cl_pol2 = clear_pol(pol2)
print(cl_pol1, cl_pol2)

# sup up numbers!
a_new_pol = sum_up(cl_pol1, cl_pol2)

# make a new one!
beautiful_pol = sum_up_polinom(a_new_pol)

# write it!
pol_in_file = open("task5_done_poli.txt", "w")
pol_in_file.write(beautiful_pol)
pol_in_file.close

