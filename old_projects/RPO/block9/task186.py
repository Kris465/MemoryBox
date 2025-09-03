
text = "Дана строка текста"
target_length = 30


def adjust_text_length(text, target_length):
    words = text.split()
    if len(words) == 1:
        return text

    total_spaces_needed = target_length - len(text.replace(" ", ""))
    gaps = len(words) - 1
    spaces_per_gap = total_spaces_needed // gaps
    extra_spaces = total_spaces_needed % gaps

    result = ""
    for i, word in enumerate(words):
        result += word
        if i < gaps:
            result += " " * (spaces_per_gap + (1 if i < extra_spaces else 0))
    return result


print("9.186", adjust_text_length(text, target_length))
