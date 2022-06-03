import PySimpleGUI as sg

base_units = [
    "tonne", "Kilogram", "Pound", "Gram", "Milligram", "Microgram", 
    "Mile", "Kilometer", "Meter", "Centimeter", "Milimeter", 
    "Year", "Month", "Week", "Day", "Hour", "Minute", "Second"
]
sg.theme('DarkTeal')
layout = [
    [
        sg.Text("Unit:", pad=((5,5),0)), 
        sg.Combo(values = base_units, pad=0,  enable_events=True, readonly=True, size=(12,5), key="-UNIT LIST 1-"), 
        sg.Text("To:", pad=((49,5),0)), 
        sg.Combo(values = base_units, pad=0, enable_events=True, readonly=True, size=(12,5), key="-UNIT LIST 2-")
    ],
    [
        sg.Text("Input: ", key="-INPUT TEXT-", pad=(5,(15,4),5))
    ],
    [
        sg.Input(key="-INPUT-", pad=(5,(0,4),5))
    ],
    [
        sg.Text("Output: ", key="-OUTPUT TEXT-")
    ],
    [
        sg.InputText("", use_readonly_for_disable = True, disabled_readonly_background_color = '#bc4873', disabled=True, key="-OUTPUT-", pad=(5,(0,4),5))
    ],
    [
        sg.Button("Convert", key="-CONVERT-", pad=((5,5),3))
    ]
]
sg.theme('DarkTeal')
window = sg.Window("Unit Converter", layout)



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-UNIT LIST 1-":
        #For -UNIT LIST 1- (weight) ("tonne", "Kilogram", "Pound", "Gram", "Milligram", "Microgram")
        if values["-UNIT LIST 1-"] == "tonne":
            window["-UNIT LIST 2-"].update(values = ["Pound", "Kilogram", "Gram", "Milligram", "Microgram"])
        if values["-UNIT LIST 1-"] == "Pound":
            window["-UNIT LIST 2-"].update(values = ["tonne", "Kilogram", "Gram", "Milligram", "Microgram"])
        if values["-UNIT LIST 1-"] == "Kilogram":
            window["-UNIT LIST 2-"].update(values = ["tonne", "Pound", "Gram", "Milligram", "Microgram"])
        if values["-UNIT LIST 1-"] == "Gram":
            window["-UNIT LIST 2-"].update(values = ["tonne", "Kilogram", "Pound", "Milligram", "Microgram"])
        if values["-UNIT LIST 1-"] == "Milligram":
            window["-UNIT LIST 2-"].update(values = ["tonne", "Kilogram", "Pound", "Gram", "Microgram"])
        if values["-UNIT LIST 1-"] == "Microgram":
            window["-UNIT LIST 2-"].update(values = ["tonne", "Kilogram", "Pound", "Gram", "Milligram"])
        #For -UNIT LIST 1- (distance) ("Mile", "Kilometer", "Meter", "Centimeter", "Milimeter")
        if values["-UNIT LIST 1-"] == "Mile":
            window["-UNIT LIST 2-"].update(values = ["Kilometer", "Meter", "Centimeter", "Milimeter"])
        if values["-UNIT LIST 1-"] == "Kilometer":
            window["-UNIT LIST 2-"].update(values = ["Mile", "Meter", "Centimeter", "Milimeter"])
        if values["-UNIT LIST 1-"] == "Meter":
            window["-UNIT LIST 2-"].update(values = ["Mile", "Kilometer", "Centimeter", "Milimeter"])
        if values["-UNIT LIST 1-"] == "Centimeter":
            window["-UNIT LIST 2-"].update(values = ["Mile", "Kilometer", "Meter", "Milimeter"])
        if values["-UNIT LIST 1-"] == "Milimeter":
            window["-UNIT LIST 2-"].update(values = ["Mile", "Kilometer", "Meter", "Centimeter"])
        #For -UNIT LIST 1- (time) ("Year", "Month", "Week", "Day", "Hour", "Minute", "Second")
        if values["-UNIT LIST 1-"] == "Year":
            window["-UNIT LIST 2-"].update(values = ["Month", "Week", "Day", "Hour", "Minute", "Second"])
        if values["-UNIT LIST 1-"] == "Month":
            window["-UNIT LIST 2-"].update(values = ["Year", "Week", "Day", "Hour", "Minute", "Second"])
        if values["-UNIT LIST 1-"] == "Week":
            window["-UNIT LIST 2-"].update(values = ["Year", "Month", "Day", "Hour", "Minute", "Second"])
        if values["-UNIT LIST 1-"] == "Day":
            window["-UNIT LIST 2-"].update(values = ["Year", "Month", "Week", "Hour", "Minute", "Second"])
        if values["-UNIT LIST 1-"] == "Hour":
            window["-UNIT LIST 2-"].update(values = ["Year", "Month", "Week", "Day", "Minute", "Second"])
        if values["-UNIT LIST 1-"] == "Minute":
            window["-UNIT LIST 2-"].update(values = ["Year", "Month", "Week", "Day", "Hour", "Second"])
        if values["-UNIT LIST 1-"] == "Second":
            window["-UNIT LIST 2-"].update(values = ["Year", "Month", "Week", "Day", "Hour", "Minute"])
    
    #("tonne", "Kilogram", "Pound", "Gram", "Milligram", "Microgram")
    #("Mile", "Kilometer", "Meter", "Centimeter", "Milimeter")
    #("Year", "Month", "Week", "Day", "Hour", "Minute", "Second")
    if event == "-CONVERT-":
        inputValue = values["-INPUT-"]
        try:
            if float(inputValue):
                #Weight Conversions ("tonne", "Kilogram", "Pound", "Gram", "Milligram", "Microgram")
                #tonne to..
                if values["-UNIT LIST 1-"] == "tonne" and values["-UNIT LIST 2-"] == "Kilogram":
                    output = round(float(inputValue)*1000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "tonne" and values["-UNIT LIST 2-"] == "Pound":
                    output = round(float(inputValue)*2204.62,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "tonne" and values["-UNIT LIST 2-"] == "Gram":
                    output = round(float(inputValue)*1000000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "tonne" and values["-UNIT LIST 2-"] == "Milligram":
                    output = round(float(inputValue)*1000000000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "tonne" and values["-UNIT LIST 2-"] == "Microgram":
                    output = round(float(inputValue)*1000000000000,2)
                    window["-OUTPUT-"].update(str(output))
                #Kilogram to..
                if values["-UNIT LIST 1-"] == "Kilogram" and values["-UNIT LIST 2-"] == "tonne":
                    output = round(float(inputValue)/1000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Kilogram" and values["-UNIT LIST 2-"] == "Pound":
                    output = round(float(inputValue)*2.20462,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Kilogram" and values["-UNIT LIST 2-"] == "Gram":
                    output = round(float(inputValue)*1000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Kilogram" and values["-UNIT LIST 2-"] == "Milligram":
                    output = round(float(inputValue)*1000000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Kilogram" and values["-UNIT LIST 2-"] == "Microgram":
                    output = round(float(inputValue)*1000000000,2)
                    window["-OUTPUT-"].update(str(output))
                #Pound to..
                if values["-UNIT LIST 1-"] == "Pound" and values["-UNIT LIST 2-"] == "tonne":
                    output = round(float(inputValue)/2204.62,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Pound" and values["-UNIT LIST 2-"] == "Kilogram":
                    output = round(float(inputValue)/2.20462,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Pound" and values["-UNIT LIST 2-"] == "Gram":
                    output = round(float(inputValue)*453.6,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Pound" and values["-UNIT LIST 2-"] == "Milligram":
                    output = round(float(inputValue)*453592,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Pound" and values["-UNIT LIST 2-"] == "Microgram":
                    output = round(float(inputValue)*4.536e+8,2)
                    window["-OUTPUT-"].update(str(output))
                #Gram to..
                if values["-UNIT LIST 1-"] == "Gram" and values["-UNIT LIST 2-"] == "tonne":
                    output = round(float(inputValue)/1e+6,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Gram" and values["-UNIT LIST 2-"] == "Kilogram":
                    output = round(float(inputValue)/1000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Gram" and values["-UNIT LIST 2-"] == "Pound":
                    output = round(float(inputValue)/453.6,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Gram" and values["-UNIT LIST 2-"] == "Milligram":
                    output = round(float(inputValue)*1000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Gram" and values["-UNIT LIST 2-"] == "Microgram":
                    output = round(float(inputValue)*1e+6,2)
                    window["-OUTPUT-"].update(str(output))
                #Milligram to..
                if values["-UNIT LIST 1-"] == "Milligram" and values["-UNIT LIST 2-"] == "tonne":
                    output = round(float(inputValue)/1e+9,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Milligram" and values["-UNIT LIST 2-"] == "Kilogram":
                    output = round(float(inputValue)/1e+6,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Milligram" and values["-UNIT LIST 2-"] == "Pound":
                    output = round(float(inputValue)/453592,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Milligram" and values["-UNIT LIST 2-"] == "Gram":
                    output = round(float(inputValue)/1000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Milligram" and values["-UNIT LIST 2-"] == "Microgram":
                    output = round(float(inputValue)*1000,2)
                    window["-OUTPUT-"].update(str(output))
                #Microgram to..
                if values["-UNIT LIST 1-"] == "Microgram" and values["-UNIT LIST 2-"] == "tonne":
                    output = round(float(inputValue)/1e+12,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Microgram" and values["-UNIT LIST 2-"] == "Kilogram":
                    output = round(float(inputValue)/1e+9,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Microgram" and values["-UNIT LIST 2-"] == "Pound":
                    output = round(float(inputValue)/4.536e+8,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Microgram" and values["-UNIT LIST 2-"] == "Gram":
                    output = round(float(inputValue)*1e+6,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Microgram" and values["-UNIT LIST 2-"] == "Milligram":
                    output = round(float(inputValue)/1000,2)
                    window["-OUTPUT-"].update(str(output))
                #Distance Conversion ("Mile", "Kilometer", "Meter", "Centimeter", "Milimeter")
                #Mile to..
                if values["-UNIT LIST 1-"] == "Mile" and values["-UNIT LIST 2-"] == "Kilometer":
                    output = round(float(inputValue)*1.609,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Mile" and values["-UNIT LIST 2-"] == "Meter":
                    output = round(float(inputValue)*1609,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Mile" and values["-UNIT LIST 2-"] == "Centimeter":
                    output = round(float(inputValue)*160934,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Mile" and values["-UNIT LIST 2-"] == "Milimeter":
                    output = round(float(inputValue)*1.609e+6,2)
                    window["-OUTPUT-"].update(str(output))
                #Kilometer to..
                if values["-UNIT LIST 1-"] == "Kilometer" and values["-UNIT LIST 2-"] == "Mile":
                    output = round(float(inputValue)/1.609,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Kilometer" and values["-UNIT LIST 2-"] == "Meter":
                    output = round(float(inputValue)*1000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Kilometer" and values["-UNIT LIST 2-"] == "Centimeter":
                    output = round(float(inputValue)*100000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Kilometer" and values["-UNIT LIST 2-"] == "Milimeter":
                    output = round(float(inputValue)*1e+6,2)
                    window["-OUTPUT-"].update(str(output))
                #Meter to..
                if values["-UNIT LIST 1-"] == "Meter" and values["-UNIT LIST 2-"] == "Mile":
                    output = round(float(inputValue)/1609,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Meter" and values["-UNIT LIST 2-"] == "Kilometer":
                    output = round(float(inputValue)/1000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Meter" and values["-UNIT LIST 2-"] == "Centimeter":
                    output = round(float(inputValue)*100,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Meter" and values["-UNIT LIST 2-"] == "Milimeter":
                    output = round(float(inputValue)*1000,2)
                    window["-OUTPUT-"].update(str(output))
                #Centimeter to..
                if values["-UNIT LIST 1-"] == "Centimeter" and values["-UNIT LIST 2-"] == "Mile":
                    output = round(float(inputValue)/160934,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Centimeter" and values["-UNIT LIST 2-"] == "Kilometer":
                    output = round(float(inputValue)/100000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Centimeter" and values["-UNIT LIST 2-"] == "Meter":
                    output = round(float(inputValue)/100,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Centimeter" and values["-UNIT LIST 2-"] == "Milimeter":
                    output = round(float(inputValue)*10,2)
                    window["-OUTPUT-"].update(str(output))
                #Milimeter to..
                if values["-UNIT LIST 1-"] == "Milimeter" and values["-UNIT LIST 2-"] == "Mile":
                    output = round(float(inputValue)/1.609e+6,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Milimeter" and values["-UNIT LIST 2-"] == "Kilometer":
                    output = round(float(inputValue)/1e+6,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Milimeter" and values["-UNIT LIST 2-"] == "Meter":
                    output = round(float(inputValue)/1000,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Milimeter" and values["-UNIT LIST 2-"] == "Centimeter":
                    output = round(float(inputValue)/10,2)
                    window["-OUTPUT-"].update(str(output))
                #Time Conversions ("Year", "Month", "Week", "Day", "Hour", "Minute", "Second")
                #Year to..
                if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Month":
                    output = round(float(inputValue)*12,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Week":
                    output = round(float(inputValue)*52.1429,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Day":
                    output = round(float(inputValue)*365,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Hour":
                    output = round(float(inputValue)*8760,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Minute":
                    output = round(float(inputValue)*525600,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Second":
                    output = round(float(inputValue)*3.154e+7,2)
                    window["-OUTPUT-"].update(str(output))
                #Month to..
                if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Year":
                    output = round(float(inputValue)/12,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Week":
                    output = round(float(inputValue)*4.345,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Day":
                    output = round(float(inputValue)*30.417,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Hour":
                    output = round(float(inputValue)*730,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Minute":
                    output = round(float(inputValue)*43800,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Second":
                    output = round(float(inputValue)*2.628e+6,2)
                    window["-OUTPUT-"].update(str(output))
                #Week to..
                if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Year":
                    output = round(float(inputValue)/52.143,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Month":
                    output = round(float(inputValue)/4.345,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Day":
                    output = round(float(inputValue)/7,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Hour":
                    output = round(float(inputValue)*168,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Minute":
                    output = round(float(inputValue)*10080,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Second":
                    output = round(float(inputValue)*604800,2)
                    window["-OUTPUT-"].update(str(output))
                #Day to..
                if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Year":
                    output = round(float(inputValue)*365,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Month":
                    output = round(float(inputValue)*30.4167,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Week":
                    output = round(float(inputValue)/7,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Hour":
                    output = round(float(inputValue)*24,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Minute":
                    output = round(float(inputValue)*1440,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Second":
                    output = round(float(inputValue)*86400,2)
                    window["-OUTPUT-"].update(str(output))
                #Hour to..
                if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Year":
                    output = round(float(inputValue)/8760,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Month":
                    output = round(float(inputValue)/730,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Week":
                    output = round(float(inputValue)/168,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Day":
                    output = round(float(inputValue)/24,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Minute":
                    output = round(float(inputValue)*60,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Second":
                    output = round(float(inputValue)*3600,2)
                    window["-OUTPUT-"].update(str(output))
                #Minute to..
                if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Year":
                    output = round(float(inputValue)/525600,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Month":
                    output = round(float(inputValue)/43800,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Week":
                    output = round(float(inputValue)/10080,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Day":
                    output = round(float(inputValue)/1440,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Hour":
                    output = round(float(inputValue)/60,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Second":
                    output = round(float(inputValue)*60,2)
                    window["-OUTPUT-"].update(str(output))
                #Second to..
                if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Year":
                    output = round(float(inputValue)/3.154e+7,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Month":
                    output = round(float(inputValue)/2.628e+6,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Week":
                    output = round(float(inputValue)/604800,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Day":
                    output = round(float(inputValue)/86400,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Hour":
                    output = round(float(inputValue)/3600,2)
                    window["-OUTPUT-"].update(str(output))
                if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Minute":
                    output = round(float(inputValue)/60,2)
                    window["-OUTPUT-"].update(str(output))

        except: window["-OUTPUT-"].update("Please Enter Numbers...")
        

window.close()
