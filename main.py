import PySimpleGUI as sg

layout = [[sg.Input()],
          [sg.Text(size=(10,1), key='-OUTPUT-')],
          [sg.Button('1'), sg.Button('2'),
           sg.Button('+'), [sg.Button('quit')]
           ]
          ]

window = sg.Window('КУЛЬКИШ', layout)
while True:
    event, values = window.read()

    if event == '1':
        window['-OUTPUT-'].update(1)
    if event == '2':
        window['-OUTPUT-'].update(2)

    if event == sg.WINDOW_CLOSED or event == 'quit':
        break


window.close()