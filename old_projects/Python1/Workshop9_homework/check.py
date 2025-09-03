"""
This module cheks input

in: string
out: string if input was incorrect, True if usual numbers, False if complex numbers

"""

def checking(use_str):
    if universal_check(use_str, "^+-%/*s0123456789(). ") and zero_check(use_str):
        return True
    elif universal_check(use_str, "+-/*0123456789j() ") and zero_check(use_str):
        return False
    else:
        return "Input is wrong!"

def universal_check(use_string, example_string):
    i = 0

    while i < len(use_string):
        if use_string[i] in example_string:
            answer = True
        else:
            answer = False
            break
        i += 1

    return answer

def zero_check(use_string):
    indexes = [i + 2 for i in range(len(use_string)) if use_string[i] == "/"]
    answer = use_string
    for ind in indexes:
        if use_string[ind] == "0":
            answer = False
        else: answer = True

    return answer

def pow_remake(use_lst):
    new_lst = []
    for i in range(len(use_lst)):
        if "s" in use_lst[i]:
            new_lst.append(use_lst[i][1:])
            new_lst.append(use_lst[i][0])
            new_lst.append("0.5")
        else:
            new_lst.append(use_lst[i])
    return new_lst