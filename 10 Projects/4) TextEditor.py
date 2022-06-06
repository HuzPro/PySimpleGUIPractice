import PySimpleGUI as sg
from pathlib import Path
import os

savePath = ""
smileys = [
        "happy",[":)",":D","<3"],
        "sad",[":(","D:","T_T","T-T","T.T"],
        "other",[":3"]
    ]
smiley_events = smileys[1] + smileys[3] + smileys[5]
menuLayout = [
        ["File",["Open", "Open New Window","Save As","Save","---","Exit"]],
        ["Tools",["Word Count", "Theme     ", ["Dark2","DarkGreen3","DarkBlue6","HotDogStand","DarkTeal10","Random"]]],
        ["Add",smileys],
]

def makeWindow(theme):
    sg.theme(theme)
    layout = [
        [sg.Menu(menuLayout)],
        [sg.Text("Untitled", k="-DOC NAME-")],
        [sg.Multiline( size=(116,28), k="-TEXT BOX-", expand_x=True,expand_y=True)],
    ]
    return sg.Window("Text Editor", layout, resizable=True)

def saveAs():
    filePath = sg.popup_get_file("Save as", no_window=True, keep_on_top=True, modal=True, save_as=True) + ".txt"
    file = Path(filePath)
    file.write_text(values["-TEXT BOX-"])
    window["-DOC NAME-"].update(Path(filePath).stem)

window = makeWindow("DarkAmber")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == "Open":
        filePath = sg.popup_get_file("Open", no_window=True)
        if filePath:
            savePath = filePath
            file = Path(filePath)
            window["-TEXT BOX-"].update(file.read_text())
            window["-DOC NAME-"].update(Path(filePath).stem)
    
    if event == "Save As":
        saveAs()

    if event == "Save":
        if os.path.exists(savePath):
            file = Path(savePath)
            file.write_text(values["-TEXT BOX-"])
            window["-DOC NAME-"].update(Path(filePath).stem)
        else: 
            saveAs()

    if event == "Exit":
        break
    if event == "Open New Window":
        window = makeWindow("random")
    
    if event == "Word Count":
        fullText = values["-TEXT BOX-"]
        cleanText = fullText.replace("\n"," ").split(" ")
        wordCount = len(cleanText)
        charCount = len("".join(cleanText))
        if charCount == 0:
            wordCount = 0    
        sg.popup(f"Words: {wordCount}.\nCharacters: {charCount}.")
    
    if event in menuLayout[1][1][2]:
        window.close()
        window = makeWindow(event)
    if event in smiley_events:
        fullText = values["-TEXT BOX-"]
        newText = fullText + " " + event
        values["-TEXT BOX-"] = newText
        window["-TEXT BOX-"].update(newText)

window.close()
