from random import randint


def find_first_pair_of_adjacent_odds(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] % 2 != 0 and sequence[i + 1] % 2 != 0:
            return i + 1, i + 2
    return None


sequence = [randint(0, 100) for i in range(20)]
result = find_first_pair_of_adjacent_odds(sequence)

if result:
    print(f'Первая пара соседних нечетных чисел\
        находится на позициях: {result}')
else:
    print('Нет пары соседних нечетных чисел')
