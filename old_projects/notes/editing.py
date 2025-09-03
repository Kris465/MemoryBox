from datetime import datetime
import reader
import writer

def edit(id_note, lst_args):
    data = reader.read()

    now = datetime.now()

    data["id"].insert(id_note, {
        'title': lst_args[0],
        'message': lst_args[1],
        'time': now
    })

    data["id"].pop(id_note + 1)

    writer.write(data)
