import PySimpleGUI as sg

base_units = [
    "tonne", "Kilogram", "Pound", "Gram", "Miligram", "Microgram", 
    "Mile", "Kilometer", "Meter", "Centimeter", "Milimeter", 
    "Year", "Month", "Week", "Day", "Hour", "Minute", "Second"
]

layout = [
    [
        sg.Text("Unit:", pad=((5,5),0)), 
        sg.Combo(values = base_units, pad=0,  enable_events=True, readonly=True, size=(12,5), key="-UNIT LIST 1-"), 
        sg.Text("To:", pad=((49,5),0)), 
        sg.Combo(values = base_units, pad=0, enable_events=True, readonly=True, size=(12,5), key="-UNIT LIST 2-")
    ],
    [
        sg.Input(key="-INPUT-", pad=(5,(15,4),5))
    ],
    [
        sg.InputText("Output: ", use_readonly_for_disable = True, disabled=True, key="-OUTPUT-")
    ],
    [
        sg.Button("Convert", key="-CONVERT-", pad=((5,5),3))
    ]
]

window = sg.Window("Unit Converter", layout)



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-UNIT LIST 1-":
        #For -UNIT LIST 1- (weight) ("tonne", "Kilogram", "Pound", "Gram", "Miligram", "Microgram")
        if values["-UNIT LIST 1-"] == "tonne":
            window["-UNIT LIST 2-"].update(values = ["Pound", "Kilogram", "Gram", "Miligram", "Microgram"])
        if values["-UNIT LIST 1-"] == "Pound":
            window["-UNIT LIST 2-"].update(values = ["tonne", "Kilogram", "Gram", "Miligram", "Microgram"])
        if values["-UNIT LIST 1-"] == "Kilogram":
            window["-UNIT LIST 2-"].update(values = ["tonne", "Pound", "Gram", "Miligram", "Microgram"])
        if values["-UNIT LIST 1-"] == "Gram":
            window["-UNIT LIST 2-"].update(values = ["tonne", "Kilogram", "Pound", "Miligram", "Microgram"])
        if values["-UNIT LIST 1-"] == "Miligram":
            window["-UNIT LIST 2-"].update(values = ["tonne", "Kilogram", "Pound", "Gram", "Microgram"])
        if values["-UNIT LIST 1-"] == "Microgram":
            window["-UNIT LIST 2-"].update(values = ["tonne", "Kilogram", "Pound", "Gram", "Miligram"])
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
    
    #("tonne", "Kilogram", "Pound", "Gram", "Miligram", "Microgram")
    #("Mile", "Kilometer", "Meter", "Centimeter", "Milimeter")
    #("Year", "Month", "Week", "Day", "Hour", "Minute", "Second")
    if event == "-CONVERT-":
        inputValue = values["-INPUT-"]
        if inputValue.isnumeric():
            #Weight Conversions ("tonne", "Kilogram", "Pound", "Gram", "Miligram", "Microgram")
            #tonne to..
            if values["-UNIT LIST 1-"] == "tonne" and values["-UNIT LIST 2-"] == "Kilogram":
                output = float(inputValue)*1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "tonne" and values["-UNIT LIST 2-"] == "Pound":
                output = float(inputValue)*2204.62
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "tonne" and values["-UNIT LIST 2-"] == "Gram":
                output = float(inputValue)*1000000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "tonne" and values["-UNIT LIST 2-"] == "Miligram":
                output = float(inputValue)*1000000000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "tonne" and values["-UNIT LIST 2-"] == "Microgram":
                output = float(inputValue)*1000000000000
                window["-OUTPUT-"].update("Output: "+str(output))
            #Kilogram to..
            if values["-UNIT LIST 1-"] == "Kilogram" and values["-UNIT LIST 2-"] == "tonne":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Kilogram" and values["-UNIT LIST 2-"] == "Pound":
                output = float(inputValue)*2.20462
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Kilogram" and values["-UNIT LIST 2-"] == "Gram":
                output = float(inputValue)*1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Kilogram" and values["-UNIT LIST 2-"] == "Miligram":
                output = float(inputValue)*1000000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Kilogram" and values["-UNIT LIST 2-"] == "Microgram":
                output = float(inputValue)*1000000000
                window["-OUTPUT-"].update("Output: "+str(output))
            #Pound to..
            if values["-UNIT LIST 1-"] == "Pound" and values["-UNIT LIST 2-"] == "tonne":
                output = float(inputValue)/2204.62
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Pound" and values["-UNIT LIST 2-"] == "Kilogram":
                output = float(inputValue)/2.20462
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Pound" and values["-UNIT LIST 2-"] == "Gram":
                output = float(inputValue)*453.6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Pound" and values["-UNIT LIST 2-"] == "Miligram":
                output = float(inputValue)*453592
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Pound" and values["-UNIT LIST 2-"] == "Microgram":
                output = float(inputValue)*4.536e+8
                window["-OUTPUT-"].update("Output: "+str(output))
            #Gram to..
            if values["-UNIT LIST 1-"] == "Gram" and values["-UNIT LIST 2-"] == "tonne":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Gram" and values["-UNIT LIST 2-"] == "Kilogram":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Gram" and values["-UNIT LIST 2-"] == "Pound":
                output = float(inputValue)/453.6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Gram" and values["-UNIT LIST 2-"] == "Miligram":
                output = float(inputValue)*1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Gram" and values["-UNIT LIST 2-"] == "Microgram":
                output = float(inputValue)*1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            #Miligram to..
            if values["-UNIT LIST 1-"] == "Miligram" and values["-UNIT LIST 2-"] == "tonne":
                output = float(inputValue)/1e-9
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Miligram" and values["-UNIT LIST 2-"] == "Kilogram":
                output = float(inputValue)/1e-6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Miligram" and values["-UNIT LIST 2-"] == "Pound":
                output = float(inputValue)/453592
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Miligram" and values["-UNIT LIST 2-"] == "Gram":
                output = float(inputValue)*1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Miligram" and values["-UNIT LIST 2-"] == "Microgram":
                output = float(inputValue)*1000
                window["-OUTPUT-"].update("Output: "+str(output))
            #Microgram to..
            if values["-UNIT LIST 1-"] == "Microgram" and values["-UNIT LIST 2-"] == "tonne":
                output = float(inputValue)/1e+12
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Microgram" and values["-UNIT LIST 2-"] == "Kilogram":
                output = float(inputValue)/1e-9
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Microgram" and values["-UNIT LIST 2-"] == "Pound":
                output = float(inputValue)/4.536e+8
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Microgram" and values["-UNIT LIST 2-"] == "Gram":
                output = float(inputValue)*1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Microgram" and values["-UNIT LIST 2-"] == "Miligram":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            #Distance Conversion ("Mile", "Kilometer", "Meter", "Centimeter", "Milimeter")
            #Mile to..
            if values["-UNIT LIST 1-"] == "Mile" and values["-UNIT LIST 2-"] == "Kilometer":
                output = float(inputValue)*1.609
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Mile" and values["-UNIT LIST 2-"] == "Meter":
                output = float(inputValue)*1609
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Mile" and values["-UNIT LIST 2-"] == "Centimeter":
                output = float(inputValue)*160934
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Mile" and values["-UNIT LIST 2-"] == "Milimeter":
                output = float(inputValue)*1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            #Kilometer to..
            if values["-UNIT LIST 1-"] == "Kilometer" and values["-UNIT LIST 2-"] == "Mile":
                output = float(inputValue)/1.609
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Kilometer" and values["-UNIT LIST 2-"] == "Meter":
                output = float(inputValue)*1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Kilometer" and values["-UNIT LIST 2-"] == "Centimeter":
                output = float(inputValue)*100000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Kilometer" and values["-UNIT LIST 2-"] == "Milimeter":
                output = float(inputValue)*1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            #Meter to..
            if values["-UNIT LIST 1-"] == "Meter" and values["-UNIT LIST 2-"] == "Mile":
                output = float(inputValue)/1609
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Meter" and values["-UNIT LIST 2-"] == "Kilometer":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Meter" and values["-UNIT LIST 2-"] == "Centimeter":
                output = float(inputValue)*100
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Meter" and values["-UNIT LIST 2-"] == "Milimeter":
                output = float(inputValue)*1000
                window["-OUTPUT-"].update("Output: "+str(output))
            #Centimeter to..
            if values["-UNIT LIST 1-"] == "Centimeter" and values["-UNIT LIST 2-"] == "Mile":
                output = float(inputValue)/160934
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Centimeter" and values["-UNIT LIST 2-"] == "Kilometer":
                output = float(inputValue)/100000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Centimeter" and values["-UNIT LIST 2-"] == "Meter":
                output = float(inputValue)/100
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Centimeter" and values["-UNIT LIST 2-"] == "Milimeter":
                output = float(inputValue)*10
                window["-OUTPUT-"].update("Output: "+str(output))
            #Milimeter to..
            if values["-UNIT LIST 1-"] == "Milimeter" and values["-UNIT LIST 2-"] == "Mile":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Milimeter" and values["-UNIT LIST 2-"] == "Kilometer":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Milimeter" and values["-UNIT LIST 2-"] == "Meter":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Milimeter" and values["-UNIT LIST 2-"] == "Centimeter":
                output = float(inputValue)/10
                window["-OUTPUT-"].update("Output: "+str(output))
            #Time Conversions ("Year", "Month", "Week", "Day", "Hour", "Minute", "Second")
            #Year to..
            if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Month":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Week":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Day":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Hour":
                output = float(inputValue)/10
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Minute":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Year" and values["-UNIT LIST 2-"] == "Second":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            #Month to..
            if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Year":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Week":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Day":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Hour":
                output = float(inputValue)/10
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Minute":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Month" and values["-UNIT LIST 2-"] == "Second":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            #Week to..
            if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Year":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Month":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Day":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Hour":
                output = float(inputValue)/10
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Minute":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Week" and values["-UNIT LIST 2-"] == "Second":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            #Day to..
            if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Year":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Month":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Week":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Hour":
                output = float(inputValue)/10
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Minute":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Day" and values["-UNIT LIST 2-"] == "Second":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            #Hour to..
            if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Year":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Month":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Week":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Day":
                output = float(inputValue)/10
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Minute":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Hour" and values["-UNIT LIST 2-"] == "Second":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            #Minute to..
            if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Year":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Month":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Week":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Day":
                output = float(inputValue)/10
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Hour":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Minute" and values["-UNIT LIST 2-"] == "Second":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            #Second to..
            if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Year":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Month":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Week":
                output = float(inputValue)/1000
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Day":
                output = float(inputValue)/10
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Hour":
                output = float(inputValue)/1.609e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            if values["-UNIT LIST 1-"] == "Second" and values["-UNIT LIST 2-"] == "Minute":
                output = float(inputValue)/1e+6
                window["-OUTPUT-"].update("Output: "+str(output))
            

        else: print("Please enter a number.")
        

window.close()
