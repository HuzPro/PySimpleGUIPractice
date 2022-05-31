import PySimpleGUI as sg

layout = [
    [
        sg.Text("Unit:", pad=((5,5),0)), 
        sg.Combo(["Kgs", "Pounds", "Miles", "Kms", "Seconds", "Minutes", "Hours"], pad=0, readonly=True, enable_events=True, size=(8,4), key="-UNIT LIST 1-"), 
        sg.Text("To:", pad=((85,5),0)), 
        sg.Combo([], pad=0, readonly=True, size=(8,4), key="-UNIT LIST 2-")
    ],
    [
        sg.Input(key="-INPUT-", pad=((0,0),5))
    ],
    [
        sg.Button("Convert", key="-CONVERT-", pad=((5,5),3))
    ]
]
window = sg.Window("Unit Converter", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-UNIT LIST 1-":
        if values["-UNIT LIST 1-"] == "Pounds":
            window["-UNIT LIST 2-"].update()

window.close()
