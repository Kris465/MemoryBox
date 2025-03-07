def find_neighboring_odd_pair(sequence):
    
    if len(sequence) != 20:
        raise ValueError("Sequence must contain exactly 20 numbers")
        
    for i in range(len(sequence) - 1):
       
        if sequence[i] % 2 == 1 and sequence[i + 1] % 2 == 1:
            return (i + 1, i + 2)
            
    return None


sequence = [2, 3, 5, 7, 8, 9, 11, 13, 15, 17,
           19, 21, 23, 25, 27, 29, 31, 33, 35, 37]

result = find_neighboring_odd_pair(sequence)

if result:
    print(f"Found pair of odd numbers at positions {result[0]} and {result[1]}")
else:
    print("No pair of neighboring odd numbers found")
