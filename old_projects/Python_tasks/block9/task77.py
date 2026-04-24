sentence = "Мама мыла раму"
has_a = 'а' in sentence
first_a = sentence.index('а') + 1 if has_a else -1
print(f"Есть ли 'а'? {has_a}")
if has_a:
    print(f"Порядковый номер первой 'а': {first_a}")
