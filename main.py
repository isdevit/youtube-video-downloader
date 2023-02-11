#YouTube Video Downloader Project By Ashish Khetal
import tkinter
import customtkinter
from pytube import YouTube

#Download Function
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink,on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        finishLabel.configure(text="")
        video.download()
        #print("Download Complete!")
        finishLabel.configure(text="Download Complete!")
    except:
        #print("Enter A Valid URL")
        finishLabel.configure(text="Invalid URL",text_color="red")

#Progress Function
def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion =bytes_downloaded/total_size*100
    per=str(int(percentage_of_completion))
    pPercentage.configure(text=per+"%")
    pPercentage.update()

    progressBar.set(float(percentage_of_completion)/100)    
   
#System Settings 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

#UI Elements
title = customtkinter.CTkLabel(app,text="Insert The Link Here")
title.pack(padx=10,pady=10)

#Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

#Finished Downloading Optional
finishLabel=customtkinter.CTkLabel(app,text="")
finishLabel.pack()

#Progress  percentage Optional
pPercentage=customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app,width=300)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

#Download button
download = customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(padx=10,pady=10)

#Running the app
app.mainloop()
