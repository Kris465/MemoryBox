def find_adjacent_pairs(sequence):
 
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            return True, (i + 1, i + 2) 
    return False, None


test_sequences = [
    [1, 2, 3, 4, 5, 6],           
    [1, 1, 2, 3, 4, 5],           
    [1, 2, 3, 3, 4, 5],          
    [1, 2, 3, 4, 5, 5],         
    [1, 1, 2, 2, 3, 3],          
]

for seq in test_sequences:
    print(f"\nПоследовательность: {seq}")
    found, positions = find_adjacent_pairs(seq)
    if found:
        print(f"Найдена пара одинаковых соседних чисел на позициях {positions[0]} и {positions[1]}")
    else:
        print("Пар одинаковых соседних чисел нет")
