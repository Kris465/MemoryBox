"""

There is a block of errors

"""

def num_input_check(use_string):
    if use_string in "1234":
        return int(use_string)
    else: return use_string 