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
        sg.Button("Start", border_width = 0, k="-START RESET-"),
        sg.Button("Stop", border_width=0, k="-STOP RESUME-"), 
        sg.Button("Lap", border_width = 0, k="-LAP-")

    ],
    [sg.pin(sg.Column([[]],k="-LAPS-",vertical_scroll_only=True,size_subsample_height=10))],
    [sg.VPush()],
    [sg.VPush()],
    [sg.VPush()],
]

def displayTime(startTime):
    APTime = round(time() - startTime, 2)
    BPTime = math.trunc(APTime)
    window["-BP TIME-"].update(BPTime)
    APTime = round(100*(APTime - math.trunc(APTime)))
    APTime = str(APTime).zfill(2)
    window["-AP TIME-"].update(APTime)
    return APTime, BPTime

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
timeBuffer = 0
active = False
lapCount = 1
apTime, bpTime = 00, 0
while True:
    event, values = window.read(timeout = 10)
    if event == sg.WIN_CLOSED or event == "-CLOSE-":
        break

    if event == "-START RESET-":
        if startTime > 0:#Reset
            active = False
            window["-AP TIME-"].update("00")
            window["-BP TIME-"].update("0")
            window["-START RESET-"].update("Start")
            window["-STOP RESUME-"].update("Stop")
            window["-LAPS-"].update(visible=False)
            apTime, bpTime = 00, 0
            startTime = 0
            lapCount = 1
        else:#Start
            window["-LAPS-"].update(visible=True)
            startTime = time()
            active = True
            window["-START RESET-"].update("Reset")

    if event == "-STOP RESUME-":
        if startTime > 0:
            if active == True:#Stop
                active = False
                window["-STOP RESUME-"].update("Resume")
                window["-START RESET-"].update("Reset")
                timeBuffer = time()
            elif active == False:#Resume
                timeBuffer = timeBuffer-startTime
                startTime = time() - timeBuffer
                active = True
                window["-STOP RESUME-"].update("Stop")

    if active:
            apTime, bpTime = displayTime(startTime)
    if event == "-LAP-":
        window.extend_layout(window["-LAPS-"],
        [[sg.Text(lapCount),sg.VSeparator(),sg.Text(str(bpTime)+":"+str(apTime))]])
        lapCount+=1

window.close()
