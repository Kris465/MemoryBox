# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools


def random_polinom():
    k = int(input('Input the numbers of parts, please: '))
    lst = [randint(-10, 10) for n in range(1, k + 1)] 
    print("The list of polynomial coefficients is: ")
    print(lst)

    structure = ['*x^'] * (k - 1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(
        lst, structure, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(* polynomial))
    polynomial[-1] = ' = 0'

    put_text = open('task4.txt', 'w')
    put_text.write("".join(map(str, polynomial)).replace(' 1*x', ' x'))
    put_text.close()

    print("".join(map(str, polynomial)).replace(' 1*x', ' x'))
    

random_polinom()

