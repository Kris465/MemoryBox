def find_first_greater(limit):
    n = 1
    while True:
        term = 1 + sum(1 / i for i in range(1, n + 1))
        if term > limit:
            return term
        n += 1
        
        
print(find_first_greater(3))
