from time import time
import PySimpleGUI as sg
from random import randint
import numpy as np
from colormap import rgb2hex, rgb2hls, hls2rgb

sg.theme("DarkGreen4")
gameCredits = "Creative Director - ME HAHAHAHAHAHA\nProduction Director - ME HAHAHAHAHAHA\nArt Director - ME HAHAHAHAHAHA\nTechnical Director - ME HAHAHAHAHAHA\nSponsor - ME HAHAHAHAHAHA"
menuLayout = [
    [sg.VPush()],
    [sg.VPush()],
    [sg.VPush()],
    [sg.pin(sg.Button("Play", k="-PLAY BUTTON-", mouseover_colors=("black", "green"), use_ttk_buttons=True, focus=False, size=(16,1)))],            #Menu
    [sg.pin(sg.Button("Options", k="-OPTIONS BUTTON-", use_ttk_buttons=True, focus=False, size=(16,1)))],
    [sg.pin(sg.Button("Credits", k="-CREDITS BUTTON-", use_ttk_buttons=True, focus=False, size=(16,1)))],
    [sg.pin(sg.Button("Exit", k="-EXIT BUTTON-", use_ttk_buttons=True, focus=False, size=(16,1)))],
    [sg.pin(sg.Text(gameCredits, visible=False, k="-CREDITS TEXT-"))],
    [sg.pin(sg.Text("Snake Speed:", visible=False, k="-SLIDER TEXT-"))],                                                                            #Snake Speed
    [sg.pin(sg.Slider(k="-SPEED SLIDER-",range=(1,100), default_value=35, orientation="h", enable_events=True, visible=False, size=(128,16)))],

    [sg.pin(sg.Text("Snake Color:", visible=False, k="-COLOR TEXT-"))]+                                                                             #Snake Color
    [sg.pin(sg.Input(default_text="#229954", size=(8,1),visible=False, enable_events=True,k="-COLOR PICKER TEXTBOX-",))]+
    [sg.pin(sg.ColorChooserButton("",s=(4,1),button_color="#229954", visible = False, k="-COLOR PICKER-", target=("-COLOR PICKER TEXTBOX-"),))],

    [sg.VPush()],
    [sg.pin(sg.Button("Back", k="-BACK BUTTON-", visible=False, use_ttk_buttons=True, focus=False, size=(16,1)))],
    [sg.VPush()],
    [sg.VPush()],
    [sg.VPush()],
    [sg.VPush()],
    [sg.VPush()],
]

def hex_to_rgb(hex):
     hex = hex.lstrip('#')
     hlen = len(hex)
     return tuple(int(hex[i:i+hlen//3], 16) for i in range(0, hlen, hlen//3))

def adjust_color_lightness(r, g, b, factor=0.3):
    h, l, s = rgb2hls(r / 255.0, g / 255.0, b / 255.0)
    l = max(min(l * factor, 1.0), 0.0)
    r, g, b = hls2rgb(h, l, s)
    return rgb2hex(int(r * 255), int(g * 255), int(b * 255))

def darken_color(r, g, b, factor=0.3):
    return adjust_color_lightness(r, g, b, 1 - factor)



def makeGameWindow(snakeSpeed, bgColor, snakeBodyColor,snakeHeadColor):
    startTime = time()

    #Game constants
    fieldSize = 800
    cellNum = 20
    cellSize = fieldSize/cellNum

    #Snake
    snakeBody = [(10,10),(9,10),(8,10), (7,10)]
    snakeDirection = {"left":(-1,0),"right":(1,0),"up":(0,1),"down":(0,-1)}
    direction = snakeDirection["right"]

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
        background_color=bgColor,
        p=((5,5),(12,5)),
    )
    layout1 = [[feild], [sg.Button("Exit", k="-EXIT GAME-", use_ttk_buttons=True, focus=False, s=(10,1))]]
    window1 = sg.Window("Snake", layout1, return_keyboard_events=True, no_titlebar=True,grab_anywhere=True, finalize=True, use_default_focus=False)
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
        if timeSinceStart >= snakeSpeed:
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
            if not 0 <= snakeBody[0][0] <= cellNum-1 or not 0 <= snakeBody[0][1] <= cellNum-1 or snakeBody[0] in snakeBody[1:-1]:
                break
             

            #feild.DrawRectangle((0,0), (fieldSize, fieldSize), "#212F3C",) #drawing the background
                
            tl, br = positionToPixel(applePosition)
            feild.DrawRectangle(   tl,         br  ,    "#E11916", line_width=0)
            #DrawDaSnake
            #tail, body, head = 0, 0, 0
            for index, part in enumerate(snakeBody):
                #if tail != 0: feild.delete_figure(tail)
                #if body != 0: feild.delete_figure(body)
                #if head != 0: feild.delete_figure(head)
                tl, br = positionToPixel(part)
                if index == 0:htl=tl
                if index == len(snakeBody)-1:                               #Tail
                    if htl == tl:
                        color = snakeHeadColor
                    elif htl != tl:
                        color = bgColor
                    tail = feild.DrawRectangle(tl, br, color,line_width=0)

                    #xDelete , yDelete = 0, 0                                        #Comment out this part and uncomment out the line above this to make the code work normally. This is a work in progress alternate.
                    #xDelete , yDelete = tl
                    #xDelete, yDelete = xDelete+(cellSize/2), yDelete-(cellSize/2)
                    #figure = feild.get_figures_at_location((xDelete,yDelete))
                    
                elif index != -1 and index != 0:                            #Body Except Head and Tail
                    color = snakeBodyColor
                    body = feild.DrawRectangle(tl, br, color, line_width=0)
                    
                elif index == 0:                                            #Head
                    color = snakeHeadColor
                    head = feild.DrawRectangle(tl, br, color, line_width=0)
                    htl = tl
                    
                    
                

    #feild.DrawRectangle((0,0), (fieldSize, fieldSize), "#212F3C")
    feild.draw_text("GAME OVER", color="red", font="Courier 50", location=(fieldSize/2,fieldSize/2))
    
    event, values = window1.read()
    if event == "-EXIT GAME-":
        window1.close()
        if window1:
            window1.close()
        else: pass
        
    return window1

    

window2 = sg.Window("Menu", menuLayout, finalize=True, size=(280,400), use_default_focus=False, element_justification="center",)

#MenuVariables
gameRunning = False
snakeSpeed = 0.35
randomNumber=0
backgroundColor = "#212F3C"
snkBColor = "#229954"
snkHColor = "#0B5345"

while True:

    event2, values2 = window2.read()
    if event2 == sg.WIN_CLOSED or event2 == "-EXIT BUTTON-":
        break
    
    if event2 == "-OPTIONS BUTTON-":
        window2["-PLAY BUTTON-"].update(visible=False)
        window2.find_element("-OPTIONS BUTTON-").Update(visible=False)
        window2.find_element("-CREDITS BUTTON-").Update(visible=False)
        window2.find_element("-EXIT BUTTON-").Update(visible=False)
        window2.find_element("-COLOR TEXT-").Update(visible=True)
        window2.find_element("-COLOR PICKER TEXTBOX-").Update(visible=True)
        window2.find_element("-COLOR PICKER-").Update(visible=True)
        window2.find_element("-SLIDER TEXT-").Update(visible=True)
        window2.find_element("-SPEED SLIDER-").Update(visible=True)
        window2.find_element("-BACK BUTTON-").Update(visible=True)

        while event2 != "-BACK BUTTON-":
            event2, values2 = window2.read()
            if event2 == "-SPEED SLIDER-":
                snakeSpeed = (100-((values2["-SPEED SLIDER-"])-1))/100
            if event2 == "-COLOR PICKER TEXTBOX-":
                
                factor = 0.75
                snkBColor = values2["-COLOR PICKER TEXTBOX-"]
                rr, gg, bb = hex_to_rgb(values2["-COLOR PICKER TEXTBOX-"])
                h, l, s = rgb2hls(rr / 255.0, gg / 255.0, bb / 255.0)
                l = max(min(l * factor, 1.0), 0.0)
                r, g, b = hls2rgb(h, l, s)
                tempHex = rgb2hex(int(r * 255), int(g * 255), int(b * 255))
                print(str(tempHex))
                snkHColor = tempHex
                window2["-COLOR PICKER-"].update(button_color=snkBColor)

        else: 
            window2.find_element("-PLAY BUTTON-").Update(visible=True)
            window2.find_element("-OPTIONS BUTTON-").Update(visible=True)
            window2.find_element("-CREDITS BUTTON-").Update(visible=True)
            window2.find_element("-EXIT BUTTON-").Update(visible=True)
            window2.find_element("-COLOR TEXT-").Update(visible=False)
            window2.find_element("-COLOR PICKER TEXTBOX-").Update(visible=False)
            window2.find_element("-COLOR PICKER-").Update(visible=False)
            window2.find_element("-SLIDER TEXT-").Update(visible=False)
            window2.find_element("-SPEED SLIDER-").Update(visible=False)
            window2.find_element("-BACK BUTTON-").Update(visible=False)
            
    
    if event2 == "-PLAY BUTTON-" and not gameRunning:
        window2.hide()
        gameRunning = True
        gameWindow = makeGameWindow(snakeSpeed, backgroundColor,snkBColor,snkHColor)
        if gameWindow:
            gameWindow.close()
        window2.un_hide()
        gameRunning = False
        
        
        


window2.close()
