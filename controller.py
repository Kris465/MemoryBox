# Все связующий и управляющий скрипт

import view
import operations
import log

def button_click():
    value_lst = view.get_value()
    log.logwrite("Пользователь ввел", value_lst) 
    result = operations.calc(value_lst)
    view.output(result)
    log_message = log.end_OK(result)
    log.logwrite(log_message)
