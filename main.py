# YouTube Video Downloader Project By Ashish Khetal
import os
import tkinter
import customtkinter
from pytube import YouTube
from moviepy.editor import *
import vlc
import tkinter.messagebox

# Save Directory
SAVE_DIR = "Yours Save Directory Folder's Path e.g C:/Users/...."

# Global variable for video
video = None

# Global variable for player
player =None

# Download Function
def startDownload():
    global video
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        finishLabel.configure(text="")
        video.download(output_path=SAVE_DIR)
        # print("Download Complete!")
        finishLabel.configure(text="Download Complete!")
        convertVid.configure(state=tkinter.NORMAL)
        playButton.configure(state=tkinter.NORMAL)
    except:
        # print("Enter A Valid URL")
        finishLabel.configure(text="Invalid URL", text_color="red")


# Conversion to Audio
def convertAudio():
    global video
    try:
        video_path = os.path.join(SAVE_DIR, video.title + '.mp4')
        audio_path = os.path.join(SAVE_DIR, video.title + '.mp3')
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        finishLabel.configure(text="Conversion Complete!")
        playAudioButton.configure(state=tkinter.NORMAL)
    except:
        finishLabel.configure(text="Conversion Failed", text_color="red")

# Progress Function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    progressBar.set(float(percentage_of_completion) / 100)

# Play Video Function
def playVideo():
    global video, player, video_window
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video_path = os.path.join(SAVE_DIR, str(ytObject.title) + '.mp4')
        player = vlc.MediaPlayer(video_path)
        player.play()
        player.video_set_mouse_input(False)  # Disable mouse input for the video player
        player.video_set_key_input(False)  # Disable key input for the video player
        player.set_fullscreen(False)  # Enable fullscreen mode for the video player
        player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached,stopPlayer)  # Attach event listener for player end reached

        # Create a window to hold the video player
        video_window = tkinter.Toplevel(app)
        video_window.title("Video Player")
        video_window.geometry("800x600")
        video_window.protocol("WM_DELETE_WINDOW", closeVideoPlayer)  # Attach event listener for window close

        # Embed the video player in the window
        player.set_hwnd(video_window.winfo_id())
    except:
        finishLabel.configure(text="Video Playback Failed", text_color="red")

# Play Audio Function
def playAudio():
    global video, player, audio_window
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        audio_path = os.path.join(SAVE_DIR, str(ytObject.title) + '.mp3')
        player = vlc.MediaPlayer(audio_path)
        player.play()
        player.audio_set_volume(40)  # Set volume to maximum (0-100)
        player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached,stopPlayer)  # Attach event listener for player end reached

        # Create a window to hold the audio player
        audio_window = tkinter.Toplevel(app)
        audio_window.title("Audio Player")
        audio_window.geometry("400x200")
        audio_window.protocol("WM_DELETE_WINDOW", closeAudioPlayer)  # Attach event listener for window close

        # Embed the audio player in the window
        player.set_hwnd(audio_window.winfo_id())

    except:
        finishLabel.configure(text="Audio Playback Failed", text_color="red")

def stopPlayer(event):
    global player
    player.stop()
    player.release()
    player = None

def closeVideoPlayer():
    global video_window,player
    result = tkinter.messagebox.askquestion("Close Video Player", "Are you sure you want to close the video player?")
    if result == "yes":
        player.stop()
        player.release()
        player = None
        video_window.destroy()

def closeAudioPlayer():
    global audio_window, player
    result = tkinter.messagebox.askquestion("Close Audio Player", "Are you sure you want to close the audio player?")
    if result == "yes":
        player.stop()
        player.release()
        player = None
        audio_window.destroy()

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text="Insert The Link Here")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading Optional
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress  percentage Optional
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=300)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Conversion button
convertVid = customtkinter.CTkButton(app, text="Convert to Audio", command=convertAudio, state=tkinter.DISABLED)
convertVid.pack(padx=10, pady=10)

# Play Video button
playButton = customtkinter.CTkButton(app, text="Play Video", command=playVideo, state=tkinter.DISABLED)
playButton.pack(padx=10, pady=10)

# Play Audio button
playAudioButton = customtkinter.CTkButton(app, text="Play Audio", command=playAudio, state=tkinter.DISABLED)
playAudioButton.pack(padx=10, pady=10)

# Running the app
app.mainloop()
