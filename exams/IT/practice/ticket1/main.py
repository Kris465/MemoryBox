text = input("Введите текст: ")
unikslov = 0
znak = 0
unicznak = 0
slov = 0
cleanline = text
for i in ",.()!?:;-":
    resultlne = cleanline.replace(i, "")
    cleanline = resultlne
print(resultlne)
spisok = resultlne.split()
spisok2 = len(spisok)
print(spisok2)
