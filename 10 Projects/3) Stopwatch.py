import PySimpleGUI as sg
from time import time
import math

sg.theme("DarkTeal10")
layout = [
    [sg.Push(), sg.Image("Cross.png", k="-CLOSE-", p=0, enable_events=True, tooltip="Close")],
    [sg.VPush()],
    [
        sg.Text("0", font = "Garamond 65", k="-BP TIME-"),
        sg.Text(".", font = "Garamond 65", k="-POINT-", justification='middle'),
        sg.Text("00", font = "Garamond 65", k="-AP TIME-")
    ],
    [
        sg.Button("Start", border_width = 0, k="-START RESUME-"),
        sg.Button("Stop", border_width=0, k="-STOP-"), 
        sg.Button("Lap", border_width = 0, k="-LAP-")

    ],
    [sg.VPush()],
    [sg.VPush()],
    [sg.VPush()],
]

def displayTime(startTime):
    elapsedTime = round(time() - startTime, 2)
    window["-BP TIME-"].update(round(elapsedTime))
    APTime = round(100*(elapsedTime - math.trunc(elapsedTime)))
    window["-AP TIME-"].update(str(APTime).zfill(2))


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
    event, values = window.read(timeout = 1)
    if event == sg.WIN_CLOSED or event == "-CLOSE-":
        break
    if event == "-START RESUME-":
        startTime = time()
        active = True
    if active:
        displayTime(startTime)

window.close()
