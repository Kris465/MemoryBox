from random import randint


def find_neighboring_odd_pair(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] % 2 == 1 and sequence[i + 1] % 2 == 1:
            return (i + 1, i + 2)

        return None


sequence = [randint(1, 1000) for i in range(9999)]

result = find_neighboring_odd_pair(sequence)

if result:
    print(f"Found pair of odd numbers at positions {result[0]} and \
          {result[1]}")
else:
    print("No pair of neighboring odd numbers found")
