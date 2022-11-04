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