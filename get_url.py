def read(title):
    with open('links_novelupdates.txt', 'r', encoding="UTF-8") as file:
        text = file.read()
        lst = text.split()
        for elem in lst:
            if title in elem:
                return elem
