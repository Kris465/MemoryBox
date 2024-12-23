import re


text = 'Привет, как твои дела? Взрытый, выплыть.'

k = int(input("Введите количество букв искомого слова: "))

text = re.sub(r'[,.?]', '', text)
words = text.lower().split()
result_list = []

for i in words:
    if "ы" in i and len(i) == k:
        result_list.append(i)

print(result_list)
