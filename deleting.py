import writer
import reader

def delete(id_note):
    data = reader.read()

    data["id"].pop(id_note + 1)

    writer.write(data)
