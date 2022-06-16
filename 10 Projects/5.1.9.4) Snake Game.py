from time import time
import PySimpleGUI as sg
from random import randint
from colormap import rgb2hex, rgb2hls, hls2rgb
import pathlib
import json
import os
from os import path


global  highScore, testHS, appleScore, playerScore, stepcount, snakeBody, direction, snakeSpeed, bgColor, snakeBodyColor, snakeHeadColor, sliderValue, applePosition, saveGameData


saveGameData = {}
snakeDirection = {"left":(-1,0),"right":(1,0),"up":(0,1),"down":(0,-1)}
direction = snakeDirection["right"]

saveCheck = False

def readGameState():
    global saveGameData
    global snakeSpeed, snakeBodyColor, snakeHeadColor, appleScore, playerScore, stepcount, direction, bgColor, highScore, sliderValue
    saveFileName = "GameData.json"
    filepath = str(pathlib.Path(__file__).parent.resolve())+"\\"+saveFileName
    if path.isfile(filepath) is True and os.stat(filepath).st_size >= 3:
        aFile = open(saveFileName, "r")
        saveGameData = json.load(aFile)
        aFile.close()
        snakeSpeed = saveGameData["snakeSpeed"]
        snakeBodyColor = saveGameData["snakeBodyColor"]
        snakeHeadColor = saveGameData["snakeHeadColor"]
        appleScore = saveGameData["AppleScore"]
        playerScore = saveGameData["PlayerScore"]
        stepcount = saveGameData["StepCount"]
        direction = saveGameData["Direction"]
        bgColor = saveGameData["BackgroundColor"]
        highScore = []
        if saveGameData["HighScore"] != []:
            for score in saveGameData["HighScore"]:
                highScore.append(score)
        sliderValue = saveGameData["sliderValue"]
        saveCheck = True
    return  saveCheck
saveCheck = readGameState()


def saveGameDataUpdate(saveGameData):
    saveGameData = {
        "snakeSpeed": snakeSpeed,
        "snakeBodyColor": snakeBodyColor,
        "snakeHeadColor": snakeHeadColor,
        "AppleScore": appleScore,
        "PlayerScore": playerScore,
        "StepCount": stepcount,
        "Direction": direction,
        "BackgroundColor": bgColor,
        "HighScore": highScore,
        "sliderValue": sliderValue
    }
    return saveGameData




def saveGameState():
    global saveGameData
    saveFileName = "GameData.json"
    filepath = str(pathlib.Path(__file__).parent.resolve())+"\\"+saveFileName
    saveGameData = saveGameDataUpdate(saveGameData)

    if path.isfile(filepath) is True and os.stat(filepath).st_size >= 3:
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
        if jsonobject["HighScore"] != highScore: jsonobject["HighScore"] = highScore
        if jsonobject["sliderValue"] != sliderValue: jsonobject["sliderValue"] = sliderValue
        aFile = open(filepath,"w")
        json.dump(jsonobject, aFile)
        aFile.close()
        
    else:
        with open(filepath, "w") as sgd:
            json.dump(saveGameData, sgd)





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
    [sg.pin(sg.Listbox([highScore], default_values=["No HighScores Yet :("], select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, highlight_text_color=None, highlight_background_color=None, no_scrollbar=True, s=(16,10), k="-HIGHSCORES TEXT-", visible=False))],
    [sg.pin(sg.Text(gameCredits, justification="center", visible=False, k="-CREDITS TEXT-"))],
    [sg.pin(sg.Text("Snake Speed:", visible=False, k="-SLIDER TEXT-"))],                                                                            #Snake Speed
    [sg.pin(sg.Slider(k="-SPEED SLIDER-",range=(1,100), default_value=sliderValue, orientation="h", enable_events=True, visible=False, size=(128,16)))],

    [sg.pin(sg.Text("Snake Color:", visible=False, k="-COLOR TEXT-"))]+                                                                             #Snake Color
    [sg.pin(sg.Input(default_text=str(snakeBodyColor), size=(8,1),visible=False, enable_events=True,k="-COLOR PICKER TEXTBOX-",))]+
    [sg.pin(sg.ColorChooserButton("",s=(4,1),button_color=snakeBodyColor, visible = False, k="-COLOR PICKER-", target=("-COLOR PICKER TEXTBOX-"),))],

    [sg.VPush()],
    [sg.pin(sg.Button("Clear", k="-CLEAR HIGHSCORES BUTTON-", visible=False, use_ttk_buttons=True, focus=False, size=(16,1)))],
    [sg.pin(sg.Button("Back", k="-BACK BUTTON-", visible=False, use_ttk_buttons=True, focus=False, size=(16,1)))],
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

    

window2 = sg.Window("Menu", menuLayout, finalize=True, size=(280,350), use_default_focus=False, element_justification="center",)

randomNumber = 0
gameRunning = False
#GameVariables
if not saveCheck:
    stepcount = 0
    highScore = []


    #MenuVariables
    
    snakeSpeed = 0.35
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
        values2["-SPEED SLIDER-"]=sliderValue
        window2["-BACK BUTTON-"].update(visible=True)
        while event2 != "-BACK BUTTON-":
            event2, values2 = window2.read()
            if event2 == "-SPEED SLIDER-":
                sliderValue = values2["-SPEED SLIDER-"]
                snakeSpeed = (100-((values2["-SPEED SLIDER-"])-1))/100
            if event2 == "-COLOR PICKER TEXTBOX-":
                
                factor = 0.75
                snakeBodyColor = values2["-COLOR PICKER TEXTBOX-"]
                rr, gg, bb = hex_to_rgb(values2["-COLOR PICKER TEXTBOX-"])
                h, l, s = rgb2hls(rr / 255.0, gg / 255.0, bb / 255.0)
                l = max(min(l * factor, 1.0), 0.0)
                r, g, b = hls2rgb(h, l, s)
                tempHex = rgb2hex(int(r * 255), int(g * 255), int(b * 255))
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
        highscores = []
        highScore.sort(reverse=True)
        if highScore:
            for num, score in enumerate(highScore):
                highscores.append(str(str(num+1)+") "+str(score))+'\n')
                num+=1
        window2["-HIGHSCORES TEXT-"].update(highscores)
        window2["-CLEAR HIGHSCORES BUTTON-"].update(visible=True)
        window2["-BACK BUTTON-"].update(visible=True)

        while event2 != "-BACK BUTTON-":
            event2, values2 = window2.read()
            if event2 == "-CLEAR HIGHSCORES BUTTON-":
                sg.popup_auto_close("All the highscores have been cleared!", auto_close_duration=3, no_titlebar=True, keep_on_top=True, grab_anywhere=True, button_type=0)
                highScore = []
                highscores = []
                highScore.sort(reverse=True)
                if highScore:
                    for num, score in enumerate(highScore):
                        highscores.append(str(str(num+1)+") "+str(score))+'\n')
                        num+=1
                window2["-HIGHSCORES TEXT-"].update(highscores)
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
            window2["-CLEAR HIGHSCORES BUTTON-"].update(visible=False)
            window2["-BACK BUTTON-"].update(visible=False)
    
    if event2 == "-PLAY BUTTON-" and not gameRunning:
        prevApple=0
        delBody=[0,0,0,0]
        appleScore = 0
        playerScore = 0
        window2.hide()
        gameRunning = True
        startTime = time()

        #Game constants
        fieldSize = 800
        cellNum = 60
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
        applePosition = newApplePosition()
        appleEaten = False

        #GameMap
        feild = sg.Graph(
            canvas_size=(fieldSize,fieldSize),
            graph_bottom_left=(0,0),
            graph_top_right=(fieldSize,fieldSize),
            background_color=bgColor,
            p=((5,5),(0,5)),
            enable_events=True,
        )
        layout1 = [[sg.Text("Score: 0", font= "Courier", k="-SCORE-")],[feild], [sg.Button("Exit", k="-EXIT GAME-", use_ttk_buttons=True, focus=False, s=(10,1))]]
        window1 = sg.Window("Snake", layout1, return_keyboard_events=True, no_titlebar=True,grab_anywhere=True, finalize=True, use_default_focus=False, element_justification="center")
        while True:
            event, values = window1.read(timeout=snakeSpeed)
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
                    delBody.append(0)
                    appleEaten = True
                    scoreFlag = True

                #SnakePositionUpdate
                newHead = (snakeBody[0][0]+ direction[0], snakeBody[0][1]+ direction[1])
                snakeBody.insert(0, newHead)

                if not appleEaten:
                    snakeBody.pop()
                appleEaten = False

                #DeathCheck
                if not 0 <= snakeBody[0][0] <= cellNum-1 or not 0 <= snakeBody[0][1] <= cellNum-1 or snakeBody[0] in snakeBody[1:]:
                    break

                #DrawDaApple
                tl, br = positionToPixel(applePosition)
                if prevApple != 0: feild.delete_figure(prevApple)
                prevApple = feild.DrawRectangle(tl, br, "#E11916", line_width=0)
                #DrawDaSnake
                for index, part in enumerate(snakeBody):
                    tl, br = positionToPixel(part)
                    if index == 0:
                        stepcount = stepcount + 1

                        htl=tl
                        if scoreFlag:
                            if stepcount <= cellNum/8 and stepcount >= 1:
                                appleScore = 200
                            elif stepcount >= (cellNum/8)+1 and stepcount <= cellNum/5:
                                appleScore = 150
                            elif stepcount >= (cellNum/5)+1 and stepcount <= cellNum/3:
                                appleScore = 100
                            elif stepcount >= (cellNum/3)+1 and stepcount <= cellNum/3:
                                appleScore = 50
                            elif stepcount >= (cellNum)+1:
                                appleScore = 10
                            playerScore += round(appleScore/(snakeSpeed+0.5))
                            window1["-SCORE-"].update("Score: "+str(playerScore))
                            stepcount = 0

                    if index == len(snakeBody)-1:                               #Tail
                        if delBody[index] != 0:feild.delete_figure(delBody[index])
                        delBody[index] = 0
                        if htl == tl: color = snakeHeadColor
                        
                        else: color = snakeBodyColor
                        delBody[index] = feild.DrawRectangle(tl, br, color,line_width=0)
                    elif index != -1 and index != 0:                            #Body Except Head and Tail
                        color = snakeBodyColor
                        if delBody[index] != 0: feild.delete_figure(delBody[index])
                        delBody[index]=0
                        delBody[index] = feild.DrawRectangle(tl, br, color, line_width=0)

                    elif index == 0:                                            #Head
                        if delBody[index] != 0: feild.delete_figure(delBody[index])
                        delBody[index]=0
                        color = snakeHeadColor
                        delBody[index] = feild.DrawRectangle(tl, br, color, line_width=0)
                        htl = tl

        
        #return snakeBody, direction, applePosition, tl, br, htl




        #feild.DrawRectangle((0,0), (fieldSize, fieldSize), "#212F3C")
        feild.draw_text("GAME OVER", color="red", font="Courier 50", location=(fieldSize/2,fieldSize/2))

        event, values = window1.read()
        if event == "-EXIT GAME-":
            highScore.append(playerScore)
            playerScore = 0
            window1.close()
            if window1:
                window1.close()
            else: pass

        window2.un_hide()
        gameRunning = False
        


saveGameState()
window2.close()
