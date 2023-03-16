import writer
import reader

def delete(id_note):
    data = reader.read()

    data["id"].pop(id_note)

    writer.write(data)
