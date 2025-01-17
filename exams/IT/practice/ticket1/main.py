text = input("Введите текст: ")
text1 = text
text2 = text
unikslov = 0
znak = 0
unicznak = 0
slov = 0
for i in ",.()!?:;-":
    resultlne = text.replace(i, "")
    text = resultlne
print(resultlne)
spisok = resultlne.split()
dlina = len(spisok)
print("Количество слов: ", dlina)
clean_spisok = []
for i in spisok:
    if i not in clean_spisok:
        clean_spisok.append(i)
print("Уникальных слов: ", len(clean_spisok))
kolichestvo = 0
i = 0

while i < len(text1):
    if text1[i] in ",.()!?:;-":
        kolichestvo += 1
    i += 1
print("Колличество знаков припинания: ", kolichestvo)
spisok1 = []
for i in text1:
    if i not in spisok1 and i in ",.()!?:;-":
        spisok1.append(i)
print(spisok1)
