from datetime import datetime
import writer

def sample_():
    now = datetime.now()

    data = {}
    data['id'] = []

    data["id"].append({
        'title': "title",
        'message': "message",
        'time': now
    })
    
    writer.write(data)
