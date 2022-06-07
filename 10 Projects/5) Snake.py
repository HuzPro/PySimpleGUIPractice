from time import time
import PySimpleGUI as sg
from random import randint

#Game Functions
def positionToPixel(cell):
    tl = cell[0]*cellSize, cell[1]*cellSize
    br = tl[0]+cellSize, tl[1]+cellSize
    return tl, br

def newApplePosition():
    applePosition = randint(0, cellNum-1), randint(0, cellNum-1)
    while applePosition in snakeBody:
        applePosition = randint(0, cellNum-1), randint(0, cellNum-1)
    return applePosition


#Game constants

fieldSize = 800
cellNum = 100
cellSize = fieldSize/cellNum

#Snake
snakeBody = [(10,10),(9,10),(8,10)]
snakeDirection = {"left":(-1,0),"right":(1,0),"up":(0,1),"down":(0,-1)}
direction = snakeDirection["up"]

#Apple

global applePosition
applePosition = newApplePosition()

appleEaten = False

feild = sg.Graph(
    canvas_size=(fieldSize,fieldSize),
    graph_bottom_left=(0,0),
    graph_top_right=(fieldSize,fieldSize),
    background_color="#212F3C",
)

layout1 = [[feild], [sg.Button("Exit", k="-EXIT GAME-")]]
def playGame():
    startTime = time()
    print("Game started")
    window1 = sg.Window("Snake", layout1, return_keyboard_events=True)
    while True:
        event, values = window1.read(timeout=1)
        if event == "-EXIT GAME-":
            break

        if event == "Left:37":
            if direction != snakeDirection["right"]:
                direction = snakeDirection["left"]
        if event == "Up:38":
            if direction != snakeDirection["down"]:
                direction = snakeDirection["up"]
        if event == "Right:39":
            if direction != snakeDirection["left"]:
                direction = snakeDirection["right"]
        if event == "Down:40":
            if direction != snakeDirection["up"]:
                direction = snakeDirection["down"]

        timeSinceStart = time() - startTime
        if timeSinceStart >= 0.1:
            startTime = time()

            #SnakeEatsApple
            if snakeBody[0] == applePosition:
                applePosition = newApplePosition()
                appleEaten = True

            #SnakePositionUpdate
            newHead = (snakeBody[0][0]+ direction[0], snakeBody[0][1]+ direction[1])
            snakeBody.insert(0, newHead)
            if not appleEaten:
                snakeBody.pop()
            appleEaten = False

            #DeathCheck
            if not 0 <= snakeBody[0][0] <= cellNum-1 or not 0 <= snakeBody[0][1] <= cellNum-1 or snakeBody[0] in snakeBody[1:]:
                break
                    


            feild.DrawRectangle((0,0), (fieldSize, fieldSize), "#212F3C")
        
            tl, br = positionToPixel(applePosition)
            feild.DrawRectangle(   tl,         br  ,    "#E11916")
            #DrawDaSnake
            for index, part in enumerate(snakeBody):
                tl, br = positionToPixel(part)
                color = "#0B5345" if index == 0 else "#229954"
                feild.DrawRectangle(tl, br, color)

        feild.DrawRectangle((0,0), (fieldSize, fieldSize), "#212F3C")
        feild.draw_text("GAME OVER", color="red", location=(fieldSize/2,fieldSize/2))
        event, values = window1.read()
        if event == "-EXIT GAME-":
            window1.close()
    
    sg.theme("random")
    
    



layout2 = [
    [sg.Button("Play", k="-PLAY BUTTON-", mouseover_colors=("black", "green"))],
    [sg.Button("Options", k="-OPTIONS BUTTON-")],
    [sg.Button("Exit", k="-EXIT BUTTON-")]
]

window2 = sg.Window("Menu", layout2)

while True:
    event2, values2 = window2.read()
    if event2 == sg.WIN_CLOSED:
        break

    if event2 == "-PLAY BUTTON-":
        playGame()
    
    if event2 == "-OPTIONS BUTTON-":
        print("You have no options >:)")

    if event2 == "-EXIT BUTTON-":
        break

window2.close()
