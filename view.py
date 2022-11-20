# Здесь интерфейс

import PySimpleGUI as sg

def user_menu():
    sg.theme('DarkAmber')

    layout = [  [sg.Text('Введите, ваше выражение, пожалуйста. \nФормат для целых чисел "2 * 2", формат для комплексных чисел "2 + 3j": ')],
            [sg.Input()],
            [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('0')],
            [sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/'), sg.Button('j')],
            [sg.Button('Узнать ответ')]]


    window = sg.Window('Калькулятор', layout)
    action = []
    flag = True

    while flag == True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Узнать ответ':
            break
        elif event == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '+' or '-' or '/' or '*' or 'j':
            for elem in range(0, 1):
                action.append(event)
            sg.Print(event, end = " ")
        elif event == 'Узнать ответ':
            flag = False
    return action


def output(result):
    sg.theme('DarkAmber')

    sg.popup(f'Результат: {result}')
    