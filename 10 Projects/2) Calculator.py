import PySimpleGUI as sg

def window_make(theme):
    sg.theme(theme)
    sg.set_options(font="Franklin 16", button_element_size=(4,3))
    buttonSize = (6,3)
    layout = [
        [sg.Button("Theme", mouseover_colors=())],
        [sg.Text("Output", font="Franklin 28", justification= 'right', expand_x= True, pad = (5,(28,16),5))],
        [sg.Button("Clear", expand_x=True, size = (4,2)), sg.Button("Enter", expand_x=True, size = (4,2))],
        [sg.Button("7", size = buttonSize),sg.Button("8", size = buttonSize),sg.Button("9", size = buttonSize),sg.Button("/", size = buttonSize)],
        [sg.Button("4", size = buttonSize),sg.Button("5", size = buttonSize),sg.Button("6", size = buttonSize),sg.Button("*", size = buttonSize)],
        [sg.Button("1", size = buttonSize),sg.Button("2", size = buttonSize),sg.Button("3", size = buttonSize),sg.Button("-", size = buttonSize)],
        [sg.Button("0", expand_x=True),sg.Button(".", size = buttonSize),sg.Button("+", size = buttonSize)]

    ]
    return sg.Window("Calculator", layout)

menu_theme = ["Menu", "Dark2","DarkGreen3","DarkBlue6","HotDogStand","DarkTeal10","Random"]
window = window_make('DarkBlue9')

while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED():
        break
    if event in ['0','1','2','3','4','5','6','7','8','9','0']:
        print(event)
        sg.theme(new_theme='random')

window.close()
