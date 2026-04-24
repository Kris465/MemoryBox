import math

def find_n(a):
    
    n = int(math.ceil((1 - a) / a))
    
    return n


a = 1.25  
result = find_n(a)
print(f"Наименьшее n = {result}")
