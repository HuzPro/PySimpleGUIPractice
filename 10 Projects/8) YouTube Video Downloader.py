from pathlib import Path
import PySimpleGUI as sg
from pytube import YouTube
import os

######################## NEED TO ADD HQ(1080p VIDEOS AND MERGE THEM WITH AUDIO USING PFFMPEG ########################

def progressCheck(stream, chunk, bytesRemaining):
    progressAmount = 100 - round(bytesRemaining / stream.filesize * 100)
    window["-DOWNLOADPROGBAR-"].update(bar_color = "red")
    window["-DOWNLOADPROGBAR-"].update(progressAmount)


def onCompleteCheck(stream, filePath):
    window["-DOWNLOADPROGBAR-"].update(0)
    window["-DOWNLOADPROGBAR-"].update(bar_color = "green")
    sg.popup("\n The video has been successfully downloaded! \n", title ="Download Successful!", auto_close=True, auto_close_duration=5)


sg.theme("DarkRed1")

infoSection = [
    [sg.Text("Title:\t  "), sg.Text("", k="-TITLE-")],
    [sg.Text("Length:\t  "), sg.Text("", k="-LENGTH-")],
    [sg.Text("Views:\t  "), sg.Text("", k="-VIEWS-")],
    [sg.Text("Creator:\t  "), sg.Text("", k="-CREATOR-")],
    [sg.Text("Description:"), ],
    [sg.Multiline("", k="-DESCRIPTION-", p=((2,5),5), s=(75,25), no_scrollbar=True, disabled=True,)]
]

downloadSection = [
    [sg.Frame("High Quality (.mp4)", [[sg.Button("Download", k="-HIGH-"), sg.Text("", k="-HIGHRES-"), sg.Text("", k="-HIGHSIZE-")]])],
    [sg.Frame("Low Quality (.mp4)", [[sg.Button("Download", k="-LOW-"), sg.Text("", k="-LOWRES-"), sg.Text("", k="-LOWSIZE-")]])],
    [sg.Frame("Audio (.mp3)", [[sg.Button("Download", k="-AUDIO-"), sg.Text("", k="-AUDIOSIZE-")]])],
    [sg.VPush()],
    [sg.Progress(100, orientation="h", bar_color="red", s=(10, 30), p=((10,10),(0,10)), k="-DOWNLOADPROGBAR-", expand_x=True)],
]

main_layout = [
    [sg.TabGroup([
        [sg.Tab("Info", infoSection), sg.Tab("Download", downloadSection)]
    ])
]
]

firstLayout = [[sg.Input("", s=(50,1), p=((10,10),(10,10)), k="-INPUT-", ), sg.Button("Submit", bind_return_key=True, k="-SUBMIT-")]]


window = sg.Window("Youtube Video Downloader", firstLayout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-SUBMIT-":
        #Closing previous window and opening the main info/download window
        video_object = YouTube(values["-INPUT-"], on_progress_callback = progressCheck, on_complete_callback = onCompleteCheck)
        window.close()
        
        #Updating the video info
        window = sg.Window("Youtube Video Downloader", main_layout, finalize=True)
        window["-TITLE-"].update(video_object.title)
        window["-LENGTH-"].update(f'{round(video_object.length / 60, 2)} minutes')
        window["-VIEWS-"].update(video_object.views)
        window["-CREATOR-"].update(video_object.author)
        window["-DESCRIPTION-"].update(video_object.description)

        #Download
        window["-HIGHSIZE-"].update(f'Size: {round(video_object.streams.get_by_resolution("720p").filesize / 1048576, 1)} MBs')
        window["-HIGHRES-"].update(f'Resolution: {video_object.streams.get_by_resolution("720p").resolution}')
        window["-LOWSIZE-"].update(f'Size: {round(video_object.streams.get_by_resolution("360p").filesize / 1048576, 1)} MBs')
        window["-LOWRES-"].update(f'Resolution: {video_object.streams.get_by_resolution("360p").resolution}')
        window["-AUDIOSIZE-"].update(f'Size: {round(video_object.streams.get_audio_only().filesize / 1048576, 1)} MBs')

    if event == "-HIGH-":
        sg.popup_ok("Type 'default' as file name to save the video with it's original file name")
        temppath = sg.popup_get_file("Select File Path", no_window=True, title="Save As", save_as=True, file_types=(("MP4", "*.mp4"),))
        saveFilePathAndFile = Path(temppath)
        saveFilePath = os.path.dirname(saveFilePathAndFile)
        saveFileName = os.path.basename(saveFilePathAndFile) + ".mp4"
        if saveFileName == "..mp4":
            pass
        elif saveFileName == "default.mp4.mp4":
            video_object.streams.get_by_resolution("720p").download(output_path=saveFilePath)
        else:
            print(saveFileName)
            video_object.streams.get_by_resolution("720p").download(output_path=saveFilePath, filename=saveFileName)

    if event == "-LOW-":
        sg.popup_ok("Type 'default' as file name to save the video with it's original file name")
        temppath = sg.popup_get_file("Select File Path", no_window=True, title="Save As", save_as=True, file_types=(("MP4", "*.mp4"),))
        saveFilePathAndFile = Path(temppath)
        saveFilePath = os.path.dirname(saveFilePathAndFile)
        saveFileName = os.path.basename(saveFilePathAndFile) + ".mp4"
        if saveFileName == "..mp4":
            pass
        elif saveFileName == "default.mp4.mp4":
            video_object.streams.get_by_resolution("360p").download(output_path=saveFilePath)
        else:
            print(saveFileName)
            video_object.streams.get_by_resolution("360p").download(output_path=saveFilePath, filename=saveFileName)
        
    if event == "-AUDIO-":
        sg.popup_ok("Type 'default' as file name to save the video with it's original file name")
        temppath = sg.popup_get_file("Select File Path", no_window=True, title="Save As", save_as=True, file_types=(("MP3", "*.mp3"),))
        saveFilePathAndFile = Path(temppath)
        saveFilePath = os.path.dirname(saveFilePathAndFile)
        saveFileName = os.path.basename(saveFilePathAndFile) + ".mp3"
        if saveFileName == "..mp4":
            pass
        elif saveFileName == "default.mp3.mp3":
            video_object.streams.get_audio_only().download(output_path=saveFilePath)
        else:
            print(saveFileName)
            video_object.streams.get_audio_only().download(output_path=saveFilePath, filename=saveFileName)


window.close()
