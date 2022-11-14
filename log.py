from datetime import datetime as dt

log_file = open('log_file.txt', 'w')
operation_time = dt.now().strftime('%H:%M')


def logwrite(note, message_text):
    log_file.write(operation_time, note, message_text, '\n')
