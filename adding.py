from datetime import datetime
import reader
import writer

def add_(name, body):
    data = reader.read()

    now = datetime.now()
    
    data["id"].append({
        'title': name,
        'message': body,
        'time': now
    })
    writer.write(data)
