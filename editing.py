from datetime import datetime
import reader
import writer

def edit(id_note, name, body):
    data = reader.read()

    now = datetime.now()

    data["id"].insert(id_note, {
        'title': name,
        'message': body,
        'time': now
    })

    data["id"].pop(id_note + 1)

    writer.write(data)
