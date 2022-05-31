from asyncio.windows_events import NULL
from tkinter import Button
import PySimpleGUI as hg
import os.path


#defining layout
layout = [
    [hg.Text("Test text written in the testenv for testing the texts texted in this text place.....")],
    [hg.Button("Okay...")]
]
#creating the actual window
window = hg.Window("Cooler test window",layout)

while True:
    event, values = window.read()
    if event == "Okay..." or event == hg.WIN_CLOSED:
        break

window.close()
