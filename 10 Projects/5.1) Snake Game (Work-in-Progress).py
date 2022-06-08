from time import time
from tkinter import Button
import PySimpleGUI as sg
from random import randint

menuLayout = [
    [sg.Button("Play", k="-PLAY BUTTON-", mouseover_colors=("black", "green"))],
    [sg.Button("Options", k="-OPTIONS BUTTON-")],
    [sg.Text("Snake Speed:", visible=False, k="-SLIDER TEXT-")],
    [sg.Slider(k="-SIZE SLIDER-",range=(1,100), default_value=25, orientation="h", enable_events=True, visible=False, )],
    [sg.Button("Back", k="-BACK BUTTON-", visible=False)],
    [sg.Button("Exit", k="-EXIT BUTTON-")]
]

def makeGameWindow():
    startTime = time()

    #Game constants
    fieldSize = 800
    cellNum = 20
    cellSize = fieldSize/cellNum

    #Snake
    snakeBody = [(10,10),(9,10),(8,10), (7,10)]
    snakeDirection = {"left":(-1,0),"right":(1,0),"up":(0,1),"down":(0,-1)}
    direction = snakeDirection["up"]

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

    #Apple
    global applePosition
    applePosition = newApplePosition()
    appleEaten = False

    #GameMap
    feild = sg.Graph(
        canvas_size=(fieldSize,fieldSize),
        graph_bottom_left=(0,0),
        graph_top_right=(fieldSize,fieldSize),
        background_color="#212F3C",
        enable_events=True
    )
    layout1 = [[feild], [sg.Button("Exit", k="-EXIT GAME-")]]
    window1 = sg.Window("Snake", layout1, return_keyboard_events=True, no_titlebar=True)
    while True:
        event, values = window1.read(timeout=0.5)
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
        if timeSinceStart >= 0.25:
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
            if not 0 <= snakeBody[0][0] <= cellNum-1 or not 0 <= snakeBody[0][1] <= cellNum-1 or snakeBody[0] in snakeBody[1:-2]:
                break
             

            #feild.DrawRectangle((0,0), (fieldSize, fieldSize), "#212F3C",) #drawing the background
                
            tl, br = positionToPixel(applePosition)
            feild.DrawRectangle(   tl,         br  ,    "#E11916", line_width=0)
            #DrawDaSnake
            #tail, body, head = 0, 0, 0
            #for index, part in enumerate(snakeBody):
            #    if index == len(snakeBody)-1:
            #        if tail != 0: feild.DeleteFigure(tail)
            #    elif index != -1 and index != 0:
            #        if body != 0: feild.DeleteFigure(body)
            #    elif index == 0:
            #        if head != 0: feild.DeleteFigure(head)
            for index, part in enumerate(snakeBody):
                tl, br = positionToPixel(part)
                if index == len(snakeBody)-1:
                    color = "#212F3C"
                    feild.DrawRectangle(tl, br, color,line_width=0)

                    #color = "#229954"
                    #feild.DrawRectangle(tl, br, color,line_width=0)
                    #xDelete , yDelete = 0, 0                                        #Comment out this part and uncomment out the line above this to make the code work normally. This is a work in progress alternate.
                    #xDelete , yDelete = tl
                    #xDelete, yDelete = xDelete+(cellSize/2), yDelete-(cellSize/2)
                    #figure = feild.get_figures_at_location((xDelete,yDelete))

                elif index != -1 and index != 0:
                    #if body != 0: feild.delete_figure(body)
                    color = "#229954"
                    feild.DrawRectangle(tl, br, color, line_width=0)
                elif index == 0:
                    color = "#0B5345"
                    feild.DrawRectangle(tl, br, color, line_width=0)
                    
                    
                

    feild.DrawRectangle((0,0), (fieldSize, fieldSize), "#212F3C")
    feild.draw_text("GAME OVER", color="red", location=(fieldSize/2,fieldSize/2))
    event, values = window1.read()
    if event == "-EXIT GAME-":
        window1.close()
        

    

window2 = sg.Window("Menu", menuLayout)
gameRunning = False
#window1 = sg.Window("Snake", layout1, return_keyboard_events=True)


while True:

    event2, values2 = window2.read()
    if event2 == sg.WIN_CLOSED or event2 == "-EXIT BUTTON-":
        break

    if event2 == "-OPTIONS BUTTON-":
        window2.find_element("-PLAY BUTTON-").Update(visible=False)
        window2.find_element("-OPTIONS BUTTON-").Update(visible=False)
        window2.find_element("-EXIT BUTTON-").Update(visible=False)
        window2.find_element("-SLIDER TEXT-").Update(visible=True)
        window2.find_element("-SIZE SLIDER-").Update(visible=True)
        window2.find_element("-BACK BUTTON-").Update(visible=True)
    
    if event2 == "-PLAY BUTTON-" and not gameRunning:
        window2.hide()
        gameRunning = True
        makeGameWindow()
        window2.un_hide()
        gameRunning = False
        
        
        


window2.close()
