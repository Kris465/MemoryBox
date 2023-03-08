from datetime import datetime
import writer

def sample_():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    data = {}
    data['id'] = []

    data["id"].append({
        'title': "title",
        'message': "message",
        'time': current_time
    })
    writer.write(data)
