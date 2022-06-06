import PySimpleGUI as sg
from pathlib import Path

smileys = [
        "happy",[":)",":D","<3"],
        "sad",[":(","D:","T_T","T-T","T.T"],
        "other",[":3"]
    ]
smiley_events = smileys[1] + smileys[3] + smileys[5]

def makeWindow():
    sg.theme("DarkGreen4")
    menuLayout = [
        ["File",["Open", "Open New Window","Save","---","Exit"]],
        ["Tools",["Word Count"]],
        ["Add",smileys],
    ]

    layout = [
        [sg.Menu(menuLayout)],
        [sg.Text("Untitled", k="-DOC NAME-")],
        [sg.Multiline( size=(160,35), k="-TEXT BOX-")],
    ]
    return sg.Window("Text Editor", layout)

window = makeWindow()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == "Open":
        filePath = sg.popup_get_file("open", no_window=True)
        if filePath:
            file = Path(filePath)
            window["-TEXT BOX-"].update(file.read_text())
            window["-DOC NAME-"].update(filePath.split("/")[-1])
    if event == "Save":
        filePath = sg.popup_get_file("Save as", no_window=True, save_as=True) + ".txt"
        file = Path(filePath)
        file.write_text(values["-TEXT BOX-"])
        window["-DOC NAME-"].update(filePath.split("/")[-1])
    if event == "Exit":
        break
    if event == "Open New Window":
        window = makeWindow()
    
    if event == "Word Count":
        fullText = values["-TEXT BOX-"]
        cleanText = fullText.replace("\n"," ").split(" ")
        wordCount = len(cleanText)
        charCount = len("".join(cleanText))
        if charCount == 0:
            wordCount = 0    
        sg.popup(f"Words: {wordCount}.\nCharacters: {charCount}.")

    if event in smiley_events:
        fullText = values["-TEXT BOX-"]
        newText = fullText + " " + event
        values["-TEXT BOX-"] = newText
        window["-TEXT BOX-"].update(newText)
window.close()
