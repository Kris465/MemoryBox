def replaysnew(spisok, indev, new_el):
    spisok[indev] = new_el
    return spisok


spisok = [1, 3, 4, 54, 52, 69]
indev = int(input('Введите индекс '))
new_el = int(input('Введите новый элемент '))
print(replaysnew(spisok, indev, new_el))
