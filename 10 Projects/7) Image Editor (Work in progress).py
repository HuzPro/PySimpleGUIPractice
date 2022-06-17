import PySimpleGUI as sg
from PIL import Image, ImageTk

filePath = ""

settingsColumn = [sg.Column([
    [sg.Button("Test")],
    [sg.Button("Test")],
    [sg.Button("Test")]
])]
imgColumn = [sg.Column([[sg.InputText("", expand_x=True, disabled=True,k="-FILE PATH-"),sg.FileBrowse(k="-FILE SELECT-", target="-FILE PATH-")],[sg.Image(k="-IMAGE-", size=(800,800))]])]



layout = [[settingsColumn, imgColumn]]

window = sg.Window("Image Editor", layout)

#img = Image.open(filePath)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    if event == "-FILE SELECT-":
        #window["-IMAGE-"].update(filePath=filePath)
        print(filePath)

window.close()
