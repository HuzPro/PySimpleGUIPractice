from asyncore import read
from tkinter import font
import PySimpleGUI as sg

#used https://user-images.githubusercontent.com/46163555/71361827-2a01b880-2562-11ea-9af8-2c264c02c3e8.jpg for themes (It's an image with all the themes)

menu_def =  ["View", ["Theme     ", ["Dark2","DarkGreen3","DarkBlue6","HotDogStand","DarkTeal10","Random"]]]


def window_make(theme):
    sg.theme(theme)
    sg.set_options(font="Franklin 16", button_element_size=(4,3))
    buttonSize = (6,3)
    layout = [
        [sg.Menu([menu_def],font = "Franklin 9", size = (10,None),key = "-MENU BAR-", pad = ((5,0),0), tearoff=False)],
        [sg.InputText("0", readonly=True, enable_events=True, disabled_readonly_text_color='#1B2631', key="-OUTPUT-", s=(10,1), expand_x=True, font="Franklin 28", justification= 'middle', pad = (5,(10,16),5))],
        [sg.Button("Clear",k="-CLEAR-", expand_x=True, size = (4,2)), sg.Button("Enter",k="-ENTER-", bind_return_key=True, expand_x=True, size = (4,2))],
        [sg.Button("7", size = buttonSize),sg.Button("8", size = buttonSize),sg.Button("9", size = buttonSize),sg.Button("/", size = buttonSize)],
        [sg.Button("4", size = buttonSize),sg.Button("5", size = buttonSize),sg.Button("6", size = buttonSize),sg.Button("*", size = buttonSize)],
        [sg.Button("1", size = buttonSize),sg.Button("2", size = buttonSize),sg.Button("3", size = buttonSize),sg.Button("-", size = buttonSize)],
        [sg.Button("0", expand_x=True),sg.Button(".", size = buttonSize),sg.Button("+", size = buttonSize)]
    ]
    return sg.Window("Calculator", layout)


window = window_make('DarkBlue9')
mathExpression = ""

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event in menu_def[1][1]:
        window.close()
        window = window_make(event)
    if event in ['.','1','2','3','4','5','6','7','8','9','0']:
        mathExpression += str(event)
        window["-OUTPUT-"].update(mathExpression)
    if event in ['+','-','*','/']:
        mathExpression += str(event)
        window["-OUTPUT-"].update(mathExpression)
    if event == "-ENTER-":
        window["-OUTPUT-"].update(eval(mathExpression))
        mathExpression = str(eval(mathExpression))
    if event == "-CLEAR-":
        mathExpression = ""
        window["-OUTPUT-"].update(mathExpression)
    if event == "-OUTPUT-" + "_Enter":
        print(event)

window.close()
