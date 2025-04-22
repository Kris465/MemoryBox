import re


def max_number_in_text(text):

    numbers = re.findall(r'-?\d+\.?\d*', text)

    if numbers:
        max_number = max(float(num) for num in numbers)
        return max_number
    else:
        return None


input_text = "В этом тексте есть 3 яблока, 4.5 апельсина и -2 груши."
result = max_number_in_text(input_text)
print(result)
