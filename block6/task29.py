def find_position(n):
    num_str = str(n)
    
    max_from_start = 0
    max_from_end = 0
    min_from_start = 0
    min_from_end = 0
    
    for i in range(len(num_str)):
        if num_str[i] == max(num_str):
            max_from_start = i + 1
            max_from_end = len(num_str) - i
        if num_str[i] == min(num_str):
            min_from_start = i + 1
            min_from_end = len(num_str) - i
            
    return {
        'макс_от_начала': max_from_start,
        'макс_от_конца': max_from_end,
        'мин_от_начала': min_from_start,
        'мин_от_конца': min_from_end
    }
    
examples = [
    12345,
    54321,
    987654,
    12345
]

for number in examples:
    result = find_position(number)
    print(f"\nАнализ числа {number}:")
    for key, value in result.items():
        print(f" {key}: {value}")
