
import PySimpleGUI as hp
import os.path

file_list_column = [
    [
        hp.Text("Image Folder"),
        hp.In(size=(40,4), enable_events=True, key="-FOLDER-"),
        hp.FolderBrowse(),
    ],
    [
        hp.Listbox(
            values=[], enable_events=True, size=(70,32),
            key="-FILE LIST-"
        )
    ]
]

image_viewer_column = [
    [hp.Text("Choose an imagine from the list ova dere <--")],
    [hp.Text(size=(55,15), key="-TOUT-")],
    [hp.Image(key="-IMAGE-")],
]

layout = [
    [
        hp.Column(file_list_column),
        hp.VSeperator(),
        hp.Column(image_viewer_column),
    ]
]

window = hp.Window("Image Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == hp.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
window.close()
