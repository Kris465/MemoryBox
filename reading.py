import reader

def read(id_note):
    if id_note == 0:
        print(reader.read())
    else:
        data = reader.read()
        print(data.get("id")[id_note])
