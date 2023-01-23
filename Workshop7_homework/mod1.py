"""
Numbers are counted in this module
    
in: list.split()
out: list[0]

actions: **, *, /, //, %, +, -, s(sqrt)
"""

import logg

actions = {
    "**": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "//": lambda x, y: str(int(x) // int(y)),
    "%": lambda x, y: str(int(x) % int(y)),
    "s": lambda x, y: str(float(x) ** float(y))
}

def calculator(new_lst):
    
    for i, val in enumerate(new_lst):
        if isinstance(val, list):
            new_lst[i] = calculator(val)

    index_lst = [i for i, val in enumerate(new_lst) if val in "s*/%"]

    while index_lst:
        index_op = index_lst[0]
        a, b, c = new_lst[index_op - 1: index_op + 2]
        new_lst.insert(index_op - 1, actions[b](a, c))
        del new_lst[index_op: index_op + 3]
        index_lst = [i for i, val in enumerate(new_lst) if val in "s*/%"]
    
    while len(new_lst) > 1:
        a, b, c = new_lst[:3]
        del new_lst[:3]
        new_lst.insert(0, actions[b](a, c))
    
    return new_lst[0]

def cut(ls):
    lst = []
    index_ = 0

    while index_ < len(ls):
        if ls[index_] == "(":
            end = ls.index(")")
            lst.append(ls[index_ + 1:end])
            index_ = end
        else: 
            lst.append(ls[index_])
        index_ += 1
    
    return lst