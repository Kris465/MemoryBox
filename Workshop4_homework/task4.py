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
    
    print("".join(map(str, polynomial)).replace(' 1*x', ' x'))
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


def text_writing(pol, name):
    text_to_file = open(f"{name}", "w")
    text_to_file.write(pol)
    text_to_file.close()

polinom = random_polinom()
text_writing(polinom, "task4.txt")

#for the fifth task:
print("Input data for the fifth task.")
polinom2 = random_polinom()
text_writing(polinom2, "task5.txt")
