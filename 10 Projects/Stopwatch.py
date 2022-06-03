import PySimpleGUI as sg
sg.theme("DarkTeal10")
layout = [
    [sg.Push(), sg.Image("cross.png", k="-CLOSE-", p=0, enable_events=True, tooltip="Close")],
    [sg.VPush()],
    [sg.Text("Time")],
    [sg.Button("Start"), sg.Button("Lap")],
    [sg.VPush()],
    [sg.VPush()],
    [sg.VPush()],
]

window = sg.Window(
    "Stopwatch", 
    layout,
    size = (400, 500),
    resizable=True,
    element_justification="center",
    no_titlebar=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "-CLOSE-":
        break
