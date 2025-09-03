sentence = input()
total_letters = sum(1 for c in sentence if c.isalpha())
count_a = sum(1 for c in sentence.lower() if c == 'а')
percentage = (count_a / total_letters * 100) if total_letters > 0 else 0
print(percentage)
