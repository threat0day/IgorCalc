"""
Пример того как ты хочешь сделать

сейчас намеренно допускаю некоторые структурные ошибки, но так понятнее)
"""

import PySimpleGUI as sg  # импортируем библиотеку со всеми утилитами


layout = None
window = None


def init_layout():

    global layout
    layout = [[sg.Input()],
              [sg.Text(size=(10,1), key='-OUTPUT-')],
              [sg.Button('1'), sg.Button('2'),
               sg.Button('+'), [sg.Button('quit')],
               sg.Button('cls'),
               sg.Button('=')
               ]
              ]


def init_window():
    global window
    window = sg.Window('КУЛЬКИШ', layout)  # инициализируем окно с параметрами


def update_output(current_value):
    global window
    # возьмем предыдущее значение и добавим существующее
    old_value = window['-OUTPUT-'].DisplayText

    if current_value == '=':
        try:
            window['-OUTPUT-'].update(eval(str(old_value)))
        except:
            pass

        return

    window['-OUTPUT-'].update(str(old_value) + str(current_value))
    if current_value == 'cls':
        window['-OUTPUT-'] = 0


def entry_point():

    init_layout()
    init_window()

    while True:  # запускаем вечный цикл, чтобы "ловить" нажатия кнопок - события
        event, values = window.read()

        update_output(event)


        if event == 'cls':
            window['-OUTPUT-'] = 0

        if event == sg.WINDOW_CLOSED or event == 'quit':
            break  # выходим из цикла


    window.close()  # закрываем окно безусловно


entry_point()