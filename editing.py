import reader
import writer

def edit(id_note, name, body):
    data = reader.read()

    data["id"].insert(id_note, {
        'title': name,
        'message': body
    })

    data["id"].pop(id_note + 1)

    writer.write(data)
