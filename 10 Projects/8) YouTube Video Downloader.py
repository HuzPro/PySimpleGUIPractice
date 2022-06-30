from pathlib import Path
import PySimpleGUI as sg
from pytube import YouTube
import os
import ffmpeg
import subprocess

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
    [sg.Frame("Highest Quality (.mp4)", [[sg.Button("Download", k="-HIGHEST-"), sg.Text("", k="-HIGHESTRES-"), sg.Text("", k="-HIGHESTSIZE-"), sg.Text("", k="-HIGHESTFPS-")]])],
    [sg.Frame("High Quality (.mp4)", [[sg.Button("Download", k="-HIGH-"), sg.Text("", k="-HIGHRES-"), sg.Text("", k="-HIGHSIZE-"), sg.Text("", k="-HIGHFPS-")]])],
    [sg.Frame("Medium Quality (.mp4)", [[sg.Button("Download", k="-MED-"), sg.Text("", k="-MEDRES-"), sg.Text("", k="-MEDSIZE-"), sg.Text("", k="-MEDFPS-")]])],
    [sg.Frame("Low Quality (.mp4)", [[sg.Button("Download", k="-LOW-"), sg.Text("", k="-LOWRES-"), sg.Text("", k="-LOWSIZE-"), sg.Text("", k="-LOWFPS-")]])],
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
        #Highest Quality
        window["-HIGHESTSIZE-"].update(f'Size: {round(video_object.streams.filter(adaptive=True)[0].filesize / 1048576, 1)} MBs')
        window["-HIGHESTRES-"].update(f'Resolution: {video_object.streams.filter(adaptive=True)[0].resolution}')
        window["-HIGHESTFPS-"].update(f'Fps: {video_object.streams.filter(adaptive=True)[0].fps}')
        #High Quality
        try:
            vidfilesize = round(video_object.streams.filter(adaptive=True, resolution="1080p")[0].filesize / 1048576, 1)
            vidrez = video_object.streams.filter(adaptive=True, resolution="1080p")[0].resolution
            vidfps = video_object.streams.filter(adaptive=True, resolution="1080p")[0].fps
            window["-HIGHSIZE-"].update(f'Size: {vidfilesize} MBs')
            window["-HIGHRES-"].update(f'Resolution: {vidrez}')
            window["-HIGHFPS-"].update(f'Fps: {vidfps}')
        except IndexError as ie:
            window["-HIGHSIZE-"].update(f'Size: NA')
            window["-HIGHRES-"].update(f'Resolution: NA')
            window["-HIGHFPS-"].update(f'Fps: NA')
            window["-HIGH-"].update(disabled=True)

        #Medium Quality
        try:
            vidfilesize = round(video_object.streams.get_by_resolution("720p").filesize / 1048576, 1)
            vidrez = video_object.streams.get_by_resolution("720p").resolution
            vidfps = video_object.streams.get_by_resolution("720p").fps
            window["-MEDSIZE-"].update(f'Size: {vidfilesize} MBs')
            window["-MEDRES-"].update(f'Resolution: {vidrez}')
            window["-MEDFPS-"].update(f'Fps: {vidfps}')
        except AttributeError as ae:
            window["-MEDSIZE-"].update(f'Size: NA')
            window["-MEDRES-"].update(f'Resolution: NA')
            window["-MEDFPS-"].update(f'Fps: NA')
            window["-MED-"].update(disabled=True)

        #Low Quality
        if video_object.streams.get_by_resolution("360p").resolution:
            vidfilesize = round(video_object.streams.get_by_resolution("360p").filesize / 1048576, 1)
            vidrez = video_object.streams.get_by_resolution("360p").resolution
            vidfps = video_object.streams.get_by_resolution("360p").fps
        elif video_object.streams.get_by_resolution("240p").resolution:
            vidfilesize = round(video_object.streams.get_by_resolution("240p").filesize / 1048576, 1)
            vidrez = video_object.streams.get_by_resolution("240p").resolution
            vidfps = video_object.streams.get_by_resolution("240p").fps
        elif video_object.streams.get_by_resolution("144p").resolution:
            vidfilesize = round(video_object.streams.get_by_resolution("144p").filesize / 1048576, 1)
            vidrez = video_object.streams.get_by_resolution("144p").resolution
            vidfps = video_object.streams.get_by_resolution("144p").fps
        window["-LOWSIZE-"].update(f'Size: {vidfilesize} MBs')
        window["-LOWRES-"].update(f'Resolution: {vidrez}')
        window["-LOWFPS-"].update(f'Fps: {vidfps}')
        #Audio Only
        window["-AUDIOSIZE-"].update(f'Size: {round(video_object.streams.get_audio_only().filesize / 1048576, 1)} MBs')

    if event == "-HIGHEST-":
        sg.popup_ok("Type 'default' as file name to save the video with it's original file name")
        temppath = sg.popup_get_file("Select File Path", no_window=True, title="Save As", save_as=True, file_types=(("MP4", "*.mp4"),))
        saveFilePathAndFile = Path(temppath)
        saveFilePath = os.path.dirname(saveFilePathAndFile)
        saveFileName = os.path.basename(saveFilePathAndFile)
        
        if saveFileName == ".mp4": pass
        elif saveFileName == "default.mp4":
            videoFile = saveFilePath+"\\"+str(video_object.title)+"1.mp4"
            audioFile = saveFilePath+"\\"+str(video_object.title)+"1.mp3"
            outputFile = saveFilePath+"\\"+str(video_object.title)+".mp4"

            for i, video_stream in enumerate(video_object.streams.filter(adaptive=True)):
                if i == 0 and video_stream:
                    highestQualityVideo = video_stream
                    break
            highestQualityVideo.download(output_path=saveFilePath, filename=video_object.title+"1.mp4")

            for i, audio_stream in enumerate(video_object.streams.filter(adaptive=True, only_audio=True)):
                if i == 1 and audio_stream:
                    highestQualityAudio = audio_stream
            highestQualityAudio.download(output_path=saveFilePath, filename=video_object.title+"1.mp3")

            subprocess.run(f'ffmpeg -i "{videoFile}" -i "{audioFile}" -c copy -y "{outputFile}"')
            os.remove(f"{videoFile}")
            os.remove(f"{audioFile}")

        else:
            videoFile = saveFilePath+"\\"+str(saveFileName)+"1.mp4"
            audioFile = saveFilePath+"\\"+str(saveFileName)+"1.mp3"
            outputFile = saveFilePath+"\\"+str(saveFileName)

            for i, video_stream in enumerate(video_object.streams.filter(adaptive=True)):
                if i == 0 and video_stream:
                    highestQualityVideo = video_stream
                    break
            highestQualityVideo.download(output_path=saveFilePath, filename=saveFileName+"1.mp4")

            for i, audio_stream in enumerate(video_object.streams.filter(adaptive=True, only_audio=True)):
                if i == 1 and audio_stream:
                    highestQualityAudio = audio_stream
            highestQualityAudio.download(output_path=saveFilePath, filename=saveFileName+"1.mp3")

            subprocess.run(f'ffmpeg -i "{videoFile}" -i "{audioFile}" -c copy -y "{outputFile}"')
            os.remove(f"{videoFile}")
            os.remove(f"{audioFile}")

    if event == "-HIGH-":
        sg.popup_ok("Type 'default' as file name to save the video with it's original file name")
        temppath = sg.popup_get_file("Select File Path", no_window=True, title="Save As", save_as=True, file_types=(("MP4", "*.mp4"),))
        saveFilePathAndFile = Path(temppath)
        saveFilePath = os.path.dirname(saveFilePathAndFile)
        saveFileName = os.path.basename(saveFilePathAndFile)
        
        if saveFileName == ".mp4": pass
        elif saveFileName == "default.mp4":
            videoFile = saveFilePath+"\\"+str(video_object.title)+"1.mp4"
            audioFile = saveFilePath+"\\"+str(video_object.title)+"1.mp3"
            outputFile = saveFilePath+"\\"+str(video_object.title)+".mp4"

            for i, video_stream in enumerate(video_object.streams.filter(adaptive=True, resolution="1080p", video_codec="vp9")):
                if i == 0 and video_stream:
                    highQualityVideo = video_stream
                    break
            highQualityVideo.download(output_path=saveFilePath, filename=video_object.title+"1.mp4")

            for i, audio_stream in enumerate(video_object.streams.filter(adaptive=True, only_audio=True)):
                if i == 1 and audio_stream:
                    highQualityAudio = audio_stream
            highQualityAudio.download(output_path=saveFilePath, filename=video_object.title+"1.mp3")

            subprocess.run(f'ffmpeg -i "{videoFile}" -i "{audioFile}" -c copy "{outputFile}"')
            os.remove(f"{videoFile}")
            os.remove(f"{audioFile}")

        else:
            videoFile = saveFilePath+"\\"+str(saveFileName)+"1.mp4"
            audioFile = saveFilePath+"\\"+str(saveFileName)+"1.mp3"
            outputFile = saveFilePath+"\\"+str(saveFileName)

            for i, video_stream in enumerate(video_object.streams.filter(adaptive=True)):
                if i == 0 and video_stream:
                    highQualityVideo = video_stream
                    break
            highQualityVideo.download(output_path=saveFilePath, filename=saveFileName+"1.mp4")

            for i, audio_stream in enumerate(video_object.streams.filter(adaptive=True, only_audio=True)):
                if i == 1 and audio_stream:
                    highQualityAudio = audio_stream
            highQualityAudio.download(output_path=saveFilePath, filename=saveFileName+"1.mp3")

            subprocess.run(f'ffmpeg -i "{videoFile}" -i "{audioFile}" -c copy "{outputFile}"')
            os.remove(f"{videoFile}")
            os.remove(f"{audioFile}")


    if event == "-MED-":
        sg.popup_ok("Type 'default' as file name to save the video with it's original file name")
        temppath = sg.popup_get_file("Select File Path", no_window=True, title="Save As", save_as=True, file_types=(("MP4", "*.mp4"),))
        saveFilePathAndFile = Path(temppath)
        saveFilePath = os.path.dirname(saveFilePathAndFile)
        saveFileName = os.path.basename(saveFilePathAndFile)
        if saveFileName == ".mp4": pass
        elif saveFileName == "default.mp4": video_object.streams.get_by_resolution("720p").download(output_path=saveFilePath)
        else: video_object.streams.get_by_resolution("720p").download(output_path=saveFilePath, filename=saveFileName)

    if event == "-LOW-":
        sg.popup_ok("Type 'default' as file name to save the video with it's original file name")
        temppath = sg.popup_get_file("Select File Path", no_window=True, title="Save As", save_as=True, file_types=(("MP4", "*.mp4"),))
        saveFilePathAndFile = Path(temppath)
        saveFilePath = os.path.dirname(saveFilePathAndFile)
        saveFileName = os.path.basename(saveFilePathAndFile)
        if saveFileName == ".mp4": pass
        elif saveFileName == "default.mp4": video_object.streams.get_by_resolution("360p").download(output_path=saveFilePath)
        else: video_object.streams.get_by_resolution("360p").download(output_path=saveFilePath, filename=saveFileName)
        
    if event == "-AUDIO-":
        sg.popup_ok("Type 'default' as file name to save the video with it's original file name")
        temppath = sg.popup_get_file("Select File Path", no_window=True, title="Save As", save_as=True, file_types=(("MP3", "*.mp3"),))
        saveFilePathAndFile = Path(temppath)
        saveFilePath = os.path.dirname(saveFilePathAndFile)
        saveFileName = os.path.basename(saveFilePathAndFile)
        if saveFileName == ".mp3": pass
        elif saveFileName == "default.mp3": video_object.streams.get_audio_only().download(output_path=saveFilePath)
        else: video_object.streams.get_audio_only().download(output_path=saveFilePath, filename=saveFileName)

window.close()
