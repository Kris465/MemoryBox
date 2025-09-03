def find_number_linear(sequence, n):

    for i, num in enumerate(sequence):
        if num > n:
            return i + 1  
    return None
