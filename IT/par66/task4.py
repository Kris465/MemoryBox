summa = 0
line = "1 + 25 + 3"
spisok = line.split(" + ")
for elem in spisok:
    summa += int(elem)
print(summa)
