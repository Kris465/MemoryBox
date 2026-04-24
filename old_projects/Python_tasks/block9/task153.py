def max_consecutive_characters(text):
    max_count = 0
    current_count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1

    max_count = max(max_count, current_count)

    return max_count


text = "aaabbbccccddddddeee"
result = max_consecutive_characters(text)
print("Наибольшее количество идущих подряд одинаковых символов:", result)
