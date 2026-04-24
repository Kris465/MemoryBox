import re


def sum_of_numbers_in_text(text):
    numbers = re.findall(r'-?\d+\.?\d*', text)
    total_sum = sum(float(num) for num in numbers)
    return total_sum


input_text = "В этом тексте есть 3 яблока, 4.5 апельсина и -2 груши."
result = sum_of_numbers_in_text(input_text)
print(result)
