import reader
import writer

def add_(name, body):
    data = reader.read()
    data["id"].append({
        'title': name,
        'message': body
    })
    writer.write(data)
