import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import tight_layout


def updateFigure(data):
    axes = fig.axes
    x = [round(int(i[0])) for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x,y,"bo-", linewidth = 1.0)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()

sg.theme("TanBlue")


table_contents = []
layout = [
    [sg.Table(
    headings = ['Observation', 'Result'],
    values=table_contents,
    expand_x=True,
    hide_vertical_scroll=True,
    k="-TABLE-",
    )],
    [sg.Input(k="-INPUT-", expand_x=True),sg.Button("Submit")],
    [sg.Canvas(k="-CANVAS-")]
]



window = sg.Window("Graph Maker", layout, finalize=True)

#matplotlib stuff
fig = matplotlib.figure.Figure(figsize=(8,4), facecolor = "#E5DECE")
fig.add_subplot(111).plot([],[])
figure_canvas_agg = FigureCanvasTkAgg(fig,window["-CANVAS-"].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        newValue = values["-INPUT-"]
        if newValue.isnumeric():
            table_contents.append([len(table_contents) + 1, int(newValue)])
            window["-TABLE-"].update(table_contents)
            window["-INPUT-"].update("")
            updateFigure(table_contents)

window.close()
