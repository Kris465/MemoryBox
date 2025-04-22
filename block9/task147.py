def calculate_sum_from_text(text):
    # Разделяем текст на строки
    lines = text.strip().splitlines()

    total_sum = 0

    for line in lines:
        if line.strip():
            numbers = map(int, line.split())
            total_sum += sum(numbers)

    return total_sum


input_text = """
1 2
3 4
5 6
"""
result = calculate_sum_from_text(input_text)
print(result)
