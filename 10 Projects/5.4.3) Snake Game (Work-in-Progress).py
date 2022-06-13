from dis import dis
from fileinput import filename
from time import time
from turtle import bgcolor
import PySimpleGUI as sg
from random import randint
import numpy as np
from colormap import rgb2hex, rgb2hls, hls2rgb
import pathlib
import json
from os import path

global  highScore, testHS, appleScore, playerScore, stepcount, snakeBody, direction, snakeSpeed, bgColor, snakeBodyColor, snakeHeadColor
global applePosition
global saveGameData
saveGameData = {}
snakeDirection = {"left":(-1,0),"right":(1,0),"up":(0,1),"down":(0,-1)}
direction = snakeDirection["right"]

def saveGameDataUpdate(saveGameData):
    saveGameData = {
        "snakeSpeed": snakeSpeed,
        "snakeBodyColor": snakeBodyColor,
        "snakeHeadColor": snakeHeadColor,
        "AppleScore": appleScore,
        "PlayerScore": playerScore,
        "StepCount": stepcount,
        "Direction": direction,
        "BackgroundColor":bgColor,
        #"HighScore":highScore
    }
    return saveGameData

def saveGameState():
    saveFileName = "GameData.json"
    filepath = str(pathlib.Path(__file__).parent.resolve())+"\\"+saveFileName
    saveGameData = saveGameDataUpdate(saveGameData)

    if path.isfile(filepath) is True:
        aFile = open(saveFileName, "r")
        jsonobject = json.load(aFile)
        aFile.close()
        if jsonobject["snakeSpeed"] != snakeSpeed: jsonobject["snakeSpeed"] = snakeSpeed
        if jsonobject["snakeBodyColor"] != snakeBodyColor: jsonobject["snakeBodyColor"] = snakeBodyColor
        if jsonobject["snakeHeadColor"] != snakeHeadColor: jsonobject["snakeHeadColor"] = snakeHeadColor
        if jsonobject["AppleScore"] != appleScore: jsonobject["AppleScore"] = appleScore
        if jsonobject["PlayerScore"] != playerScore: jsonobject["PlayerScore"] = playerScore
        if jsonobject["StepCount"] != stepcount: jsonobject["StepCount"] = stepcount
        if jsonobject["Direction"] != direction: jsonobject["Direction"] = direction
        if jsonobject["BackgroundColor"] != bgColor: jsonobject["BackgroundColor"] = bgColor

        aFile = open(filepath,"w")
        json.dump(jsonobject, aFile)
        aFile.close()
        print("first condition "+filepath)
        
    else:
        with open(filepath, "w") as sgd:
            json.dump(saveGameData, sgd)
        print("second condition "+filepath)


testHS = ""
highScore = []


sg.theme("DarkGreen4")
gameCredits = "Creative Director - ME\nProduction Director - ME\nArt Director - ME\nTechnical Director - ME\nSponsor - ME\nSupporters - ME, MYSELF and I"
menuLayout = [
    [sg.VPush()],
    [sg.VPush()],
    [sg.VPush()],
    [sg.pin(sg.Button("Play", k="-PLAY BUTTON-", mouseover_colors=("black", "green"), use_ttk_buttons=True, focus=False, size=(16,1)))],            #Menu
    [sg.pin(sg.Button("Options", k="-OPTIONS BUTTON-", use_ttk_buttons=True, focus=False, size=(16,1)))],
    [sg.pin(sg.Button("Credits", k="-CREDITS BUTTON-", use_ttk_buttons=True, focus=False, size=(16,1)))],
    [sg.pin(sg.Button("High Scores", k="-HIGHSCORES BUTTON-", use_ttk_buttons=True, focus=False, size=(16,1)))],
    [sg.pin(sg.Button("Exit", k="-EXIT BUTTON-", use_ttk_buttons=True, focus=False, size=(16,1)))],
    [sg.pin(sg.Text(text = "", justification="center", visible=False, k="-HIGHSCORES TEXT-"))],
    [sg.pin(sg.Text(gameCredits, justification="center", visible=False, k="-CREDITS TEXT-"))],
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



def makeGameWindow():
    startTime = time()

    #Game constants
    fieldSize = 800
    cellNum = 20
    cellSize = fieldSize/cellNum
    appleScore = 0 
    playerScore = 0
    stepcount = 0

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
        p=((5,5),(0,5)),
    )
    layout1 = [[sg.Text("Score: 0", font= "Courier", k="-SCORE-")],[feild], [sg.Button("Exit", k="-EXIT GAME-", use_ttk_buttons=True, focus=False, s=(10,1))]]
    window1 = sg.Window("Snake", layout1, return_keyboard_events=True, no_titlebar=True,grab_anywhere=True, finalize=True, use_default_focus=False, element_justification="center")
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
            scoreFlag = False
            startTime = time()
            #SnakeEatsApple
            if snakeBody[0] == applePosition:
                applePosition = newApplePosition()
                appleEaten = True
                scoreFlag = True

            #SnakePositionUpdate
            newHead = (snakeBody[0][0]+ direction[0], snakeBody[0][1]+ direction[1])
            snakeBody.insert(0, newHead)
            
            if not appleEaten:
                snakeBody.pop()
            appleEaten = False

            #DeathCheck
            if not 0 <= snakeBody[0][0] <= cellNum-1 or not 0 <= snakeBody[0][1] <= cellNum-1 or snakeBody[0] in snakeBody[1:-1]:
                highScore.append(str(playerScore))
                break

            #DrawDaApple
            tl, br = positionToPixel(applePosition)
            feild.DrawRectangle(tl, br, "#E11916", line_width=0)

            #DrawDaSnake
            for index, part in enumerate(snakeBody):
                tl, br = positionToPixel(part)
                if index == 0:
                    stepcount = stepcount + 1

                    htl=tl
                    if scoreFlag:
                        if stepcount <= 5 and stepcount >= 1:
                            appleScore = 20
                        elif stepcount >= 6 and stepcount <= 10:
                            appleScore = 15
                        elif stepcount >= 11 and stepcount <= 20:
                            appleScore = 10
                        elif stepcount >= 21 and stepcount <= 30:
                            appleScore = 5
                        elif stepcount >= 31:
                            appleScore = 1
                        playerScore += round(appleScore/(snakeSpeed+0.5))
                        window1["-SCORE-"].update("Score: "+str(playerScore))
                        stepcount = 0
                
                if index == len(snakeBody)-1:                               #Tail
                    if htl == tl:
                        color = snakeHeadColor
                    elif htl != tl:
                        color = bgColor
                    feild.DrawRectangle(tl, br, color,line_width=0)

                    #xDelete , yDelete = 0, 0                                        #Comment out this part and uncomment out the line above this to make the code work normally. This is a work in progress alternate.
                    #xDelete , yDelete = tl
                    #xDelete, yDelete = xDelete+(cellSize/2), yDelete-(cellSize/2)
                    #figure = feild.get_figures_at_location((xDelete,yDelete))
                    
                elif index != -1 and index != 0:                            #Body Except Head and Tail
                    color = snakeBodyColor
                    feild.DrawRectangle(tl, br, color, line_width=0)
                    
                elif index == 0:                                            #Head
                    color = snakeHeadColor
                    feild.DrawRectangle(tl, br, color, line_width=0)
                    htl = tl
            
            
    #return snakeBody, direction, applePosition, tl, br, htl
                    
                    
                

    #feild.DrawRectangle((0,0), (fieldSize, fieldSize), "#212F3C")
    feild.draw_text("GAME OVER", color="red", font="Courier 50", location=(fieldSize/2,fieldSize/2))
    
    event, values = window1.read()
    if event == "-EXIT GAME-":
        window1.close()
        if window1:
            window1.close()
        else: pass
        
    return window1

    

window2 = sg.Window("Menu", menuLayout, finalize=True, size=(280,350), use_default_focus=False, element_justification="center",)

#GameVariables
appleScore = 0
playerScore = 0
stepcount = 0
highScore = [15, 17]


#MenuVariables
gameRunning = False
snakeSpeed = 0.35
randomNumber = 0
bgColor = "#212F3C"
snakeBodyColor = "#229954"
snakeHeadColor = "#0B5345"


while True:

    event2, values2 = window2.read()
    if event2 == sg.WIN_CLOSED or event2 == "-EXIT BUTTON-":
        break
    
    if event2 == "-OPTIONS BUTTON-":
        window2["-PLAY BUTTON-"].update(visible=False)
        window2["-OPTIONS BUTTON-"].update(visible=False)
        window2["-CREDITS BUTTON-"].update(visible=False)
        window2["-HIGHSCORES BUTTON-"].update(visible=False)
        window2["-EXIT BUTTON-"].update(visible=False)
        window2["-COLOR TEXT-"].update(visible=True)
        window2["-COLOR PICKER TEXTBOX-"].update(visible=True)
        window2["-COLOR PICKER-"].update(visible=True)
        window2["-SLIDER TEXT-"].update(visible=True)
        window2["-SPEED SLIDER-"].update(visible=True)
        window2["-BACK BUTTON-"].update(visible=True)

        while event2 != "-BACK BUTTON-":
            event2, values2 = window2.read()
            if event2 == "-SPEED SLIDER-":
                snakeSpeed = (100-((values2["-SPEED SLIDER-"])-1))/100
            if event2 == "-COLOR PICKER TEXTBOX-":
                
                factor = 0.75
                snakeBodyColor = values2["-COLOR PICKER TEXTBOX-"]
                rr, gg, bb = hex_to_rgb(values2["-COLOR PICKER TEXTBOX-"])
                h, l, s = rgb2hls(rr / 255.0, gg / 255.0, bb / 255.0)
                l = max(min(l * factor, 1.0), 0.0)
                r, g, b = hls2rgb(h, l, s)
                tempHex = rgb2hex(int(r * 255), int(g * 255), int(b * 255))
                print(str(tempHex))
                snakeHeadColor = tempHex
                window2["-COLOR PICKER-"].update(button_color=snakeBodyColor)

        else: 
            window2["-PLAY BUTTON-"].update(visible=True)
            window2["-OPTIONS BUTTON-"].update(visible=True)
            window2["-CREDITS BUTTON-"].update(visible=True)
            window2["-HIGHSCORES BUTTON-"].update(visible=True)
            window2["-EXIT BUTTON-"].update(visible=True)
            window2["-COLOR TEXT-"].update(visible=False)
            window2["-COLOR PICKER TEXTBOX-"].update(visible=False)
            window2["-COLOR PICKER-"].update(visible=False)
            window2["-SLIDER TEXT-"].update(visible=False)
            window2["-SPEED SLIDER-"].update(visible=False)
            window2["-BACK BUTTON-"].update(visible=False)
        
    if event2 == "-CREDITS BUTTON-":
        window2["-PLAY BUTTON-"].update(visible=False)
        window2["-OPTIONS BUTTON-"].update(visible=False)
        window2["-CREDITS BUTTON-"].update(visible=False)
        window2["-HIGHSCORES BUTTON-"].update(visible=False)
        window2["-EXIT BUTTON-"].update(visible=False)
        window2["-COLOR TEXT-"].update(visible=False)
        window2["-COLOR PICKER TEXTBOX-"].update(visible=False)
        window2["-COLOR PICKER-"].update(visible=False)
        window2["-SLIDER TEXT-"].update(visible=False)
        window2["-SPEED SLIDER-"].update(visible=False)
        window2["-CREDITS TEXT-"].update(visible=True)
        window2["-BACK BUTTON-"].update(visible=True)

        while event2 != "-BACK BUTTON-":
            event2, values2 = window2.read()
        else: 
            window2["-PLAY BUTTON-"].update(visible=True)
            window2["-OPTIONS BUTTON-"].update(visible=True)
            window2["-CREDITS BUTTON-"].update(visible=True)
            window2["-HIGHSCORES BUTTON-"].update(visible=True)
            window2["-EXIT BUTTON-"].update(visible=True)
            window2["-COLOR TEXT-"].update(visible=False)
            window2["-COLOR PICKER TEXTBOX-"].update(visible=False)
            window2["-COLOR PICKER-"].update(visible=False)
            window2["-SLIDER TEXT-"].update(visible=False)
            window2["-SPEED SLIDER-"].update(visible=False)
            window2["-CREDITS TEXT-"].update(visible=False)
            window2["-BACK BUTTON-"].update(visible=False)
            
    if event2 == "-HIGHSCORES BUTTON-":
        window2["-PLAY BUTTON-"].update(visible=False)
        window2["-OPTIONS BUTTON-"].update(visible=False)
        window2["-CREDITS BUTTON-"].update(visible=False)
        window2["-HIGHSCORES BUTTON-"].update(visible=False)
        window2["-EXIT BUTTON-"].update(visible=False)
        window2["-COLOR TEXT-"].update(visible=False)
        window2["-COLOR PICKER TEXTBOX-"].update(visible=False)
        window2["-COLOR PICKER-"].update(visible=False)
        window2["-SLIDER TEXT-"].update(visible=False)
        window2["-SPEED SLIDER-"].update(visible=False)
        window2["-CREDITS TEXT-"].update(visible=False)
        window2["-HIGHSCORES TEXT-"].update(visible=True)
        textHS = ""
        for score in highScore: textHS +=str(score)+"\n"
        window2["-HIGHSCORES TEXT-"].update(testHS)
        window2["-BACK BUTTON-"].update(visible=True)

        while event2 != "-BACK BUTTON-":
            event2, values2 = window2.read()
        else:
            window2["-PLAY BUTTON-"].update(visible=True)
            window2["-OPTIONS BUTTON-"].update(visible=True)
            window2["-CREDITS BUTTON-"].update(visible=True)
            window2["-HIGHSCORES BUTTON-"].update(visible=True)
            window2["-EXIT BUTTON-"].update(visible=True)
            window2["-COLOR TEXT-"].update(visible=False)
            window2["-COLOR PICKER TEXTBOX-"].update(visible=False)
            window2["-COLOR PICKER-"].update(visible=False)
            window2["-SLIDER TEXT-"].update(visible=False)
            window2["-SPEED SLIDER-"].update(visible=False)
            window2["-CREDITS TEXT-"].update(visible=False)
            window2["-HIGHSCORES TEXT-"].update(visible=False)
            window2["-BACK BUTTON-"].update(visible=False)
            
    
    if event2 == "-PLAY BUTTON-" and not gameRunning:
        window2.hide()
        gameRunning = True
        gameWindow = makeGameWindow()
        if gameWindow:
            gameWindow.close()
        window2.un_hide()
        gameRunning = False
        
print()


saveGameState()
window2.close()
