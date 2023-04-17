import re

def cut():
    f = open('Untitled-1.txt', 'r')
    text = f.read()
    lst = text.split("\t")
    new_lst = []
    for elem in lst:
        if 'novelupdates' in elem:
            new_lst.append(elem)
    
    with open(f"new.txt", "w", encoding="utf-8") as file:
        for elem in new_lst:
            file.write(elem + '\n')
    # result = re.findall(r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?', text)
    # print(result)

cut()
    