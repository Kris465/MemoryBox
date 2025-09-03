from datetime import datetime
import reader
import writer

def add_(lst_args):
    data = reader.read()

    now = datetime.now()
    
    data["id"].append({
        'title': lst_args[0],
        'message': lst_args[1],
        'time': now
    })
    writer.write(data)
