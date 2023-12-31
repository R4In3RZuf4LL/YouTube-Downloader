from cgitb import text
import tkinter
from click import command
import customtkinter
from flask.scaffold import F
from pytube import YouTube

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        ytObject.streams
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Heruntergeladen!")
    except:
        finishLabel.configure(text="Download Error!", text_color="red")
    
def on_progress(stream, chunk, bytes_remening):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remening
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube-Downloader")

# Adding Ui Elements
title = customtkinter.CTkLabel(app, text="Kopiere deinen YouTuble Link!")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0.5)
progressBar.pack(padx=10, pady=10)

# Download-Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()