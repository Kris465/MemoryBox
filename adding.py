from datetime import datetime
import reader
import writer

def add_(name, body):
    data = reader.read()

    now = datetime.now()
    current_time = now.strftime("%H:%M")

    data["id"].append({
        'title': name,
        'message': body,
        'time': current_time
    })
    writer.write(data)
