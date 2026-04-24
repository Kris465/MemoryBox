def process_sequense(sequense):
    product = 1
    for i, num in enumerate(sequense):
        if num == 0:
            yield 0 
            break
    product *= num
    if i % 2 == 0:
        yield product
        
        
sequense = [2, 3, 4, 5, 6, 0]
result = list(process_sequense(sequense))
print(result)
