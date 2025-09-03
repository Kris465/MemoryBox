def process_sequence(sequence):
    product = 1
    for i, num in enumerate(sequence):
        if num == 0:
            yield 0
            break
        product *= num
        if i % 2 == 0:
            yield product


sequence = [2, 3, 4, 5, 6, 0]
result = list(process_sequence(sequence))
print(result)
