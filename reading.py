import reader

def read(id_note):
    data = reader.read()
    if id_note:
        opt = int(input("How would you like to see notes? id (1) or time (2)?\n"))
        if opt == 2:
            lst = data.get("id")
            lst = sorted(lst, key=lambda x: x['time'], reverse=False)
            return lst
        else:
            return data
    else:
        return data.get("id")[id_note]
