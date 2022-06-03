import PySimpleGUI as sg
from time import time

sg.theme("DarkTeal10")
layout = [
    [sg.Push(), sg.Image("cross.png", k="-CLOSE-", p=0, enable_events=True, tooltip="Close")],
    [sg.VPush()],
    [sg.Text("123.", font = "Garamond 65", k="-TIME-")],
    [
        sg.Button("Start", border_width = 0, k="-START RESUME-"),
        sg.Button("Stop", border_width=0, k="-STOP-"), 
        sg.Button("Lap", border_width = 0, k="-LAP-")

    ],
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
    no_titlebar=True,
    grab_anywhere=True,
    use_default_focus=False)
startTime = 0
active = False

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "-CLOSE-":
        break
    if event == "-START RESUME-":
        startTime = time()
        active = True
    if active:
        elapsedTime = time()
