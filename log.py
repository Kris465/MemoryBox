from datetime import datetime as dt

log_file = open('log_file.txt', 'w')
operation_time = dt.now().strftime('%H:%M')


def logwrite(note, message_text):
    log_file.write(operation_time + '\n')
    log_file.write(note + '\n')
    log_file.write(str(message_text) + '\n')
