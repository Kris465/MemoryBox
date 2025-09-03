def count_plus_minus(text):
    return text.count("+") + text.count("-")


text = "2 + 3 - 5 + 7"
print(count_plus_minus(text))
