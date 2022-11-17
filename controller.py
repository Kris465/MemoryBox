# Все связующий и управляющий скрипт

import view
import operations
import log

def button_click():
    value_lst = view.get_value()
    log.logwrite("User input: ", value_lst) 
    result = operations.calc(value_lst)
    log.logwrite("Result of calculations is: ", result)
    view.output(result)
