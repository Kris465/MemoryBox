from datetime import datetime as dt

log_file = open('log_file.txt', 'w')
operation_time = dt.now().strftime('%H:%M')


def end_OK(message_text):  # Функция, формирующий красивую запись в файл
    total_string_OK_length = 70
    result = ''
    for i in range(1, total_string_OK_length - len(message_text)-2):
        result += '.'
    result += 'OK'


def logwrite(arg, message_text=''):  # Основная функция лога
    if arg == 'step_begin' or arg == 'exception':
        log_file.write(operation_time + ' ' + message_text)
    elif arg == 'step_OK':
        log_file.write(end_OK(message_text) + '\n')


"""Пример:
def check_input(input):    
    message_text = f'Проверяю ввод пользователя'     
    logwrite('step_begin', message_text)                              # <--------- Запись в лог об обЪявлении начала операции

    for s in expression:
        if s.isalpha == False:
            pass
            logwrite('step_OK', message_text)                         # <----------------- Запись в лог о том, что шаг выполнен (функция отработала), при условии, что проверка пройдена удачно
        else:
            message_text = f'Ошибка ввода. Проверьте входные данные'            
            logwrite('exception', message_text)                       # <-------------- Запись в лог и вывод пользователю отчёт об ошибке
            print('message_text)                                      
"""

"""Пример записи:
Если проверка прошла успешно:
14:06 Проверяю ввод пользователя........................................OK

Если проверка прошла неудачно:
14:06 Проверяю ввод пользователя
Ошибка ввода. Проверьте входные данные
"""


                                                                                                                                    # Новикова Д.
