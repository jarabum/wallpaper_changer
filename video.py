import vlc
import ctypes
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from tkinter import *

# Function for playing wallpaper
def playvideo(path, monitor):
    print("Playing" + " " + path + " on monitor" + " " + monitor)
    print()
    window.destroy()
    print("Just close me to end the video wallpaper :)")
    print("Its for resource saving")
    print("If you can, ignore errors if any appear")
    print()
    os.system("python playvideo.py" + " " + path + " " + monitor)

# Paths for wallpapers
wallpaper1 = "videos/wallpapers/video1.mp4"
wallpaper2 = "videos/wallpapers/video2.mp4"
wallpaper3 = "videos/wallpapers/video3.mp4"

# Paths for wallpaper icons
icon1path = os.path.abspath("images/wallpapers/pozadi3.png")
wallpaper1iconpath = os.path.abspath("videos/icons/icon1.png")
wallpaper2iconpath = os.path.abspath("videos/icons/icon2.png")
wallpaper3iconpath = os.path.abspath("videos/icons/icon3.png")

# Main window settings
window = Tk() # Instantiate an instance of a window
# Some window settings
window.geometry("400x430")
window.title("Wallpaper Changer - videos :)")
window.config(background="white")
window.resizable(False, False)

# Set window icon
icon = PhotoImage(file=icon1path) # Convert icon image to PhotoImage
window.iconphoto(True,icon)

# Add text "Wallpaper Changer"
name = Label(window, text="Wallpaper Changer", font=("Arial", 25, "bold"), fg="black", bg="white")
name.pack(padx=20, pady=20)

# Create button for wallpaper 1
wallpaper1icon = PhotoImage(file=wallpaper1iconpath)
wallpaper1b = Button(window, text="wallpaper1", image=wallpaper1icon, command=lambda:playvideo(wallpaper1, 0))
wallpaper1b.place(x=25,y=100)

# Create button for wallpaper 2
wallpaper2icon = PhotoImage(file=wallpaper2iconpath)
wallpaper2b = Button(window, text="wallpaper2", image=wallpaper2icon, command=lambda:playvideo(wallpaper2, 0))
wallpaper2b.place(x=150,y=100)

# Create button for wallpaper 3
wallpaper3icon = PhotoImage(file=wallpaper3iconpath)
wallpaper3b = Button(window, text="wallpaper3", image=wallpaper3icon, command=lambda:playvideo(wallpaper3, 0))
wallpaper3b.place(x=275,y=100)

# Add text "Set custom wallpaper"
customtext = Label(window, text="Set custom wallpaper", font=("Arial", 15, "bold"), fg="black", bg="white")
customtext.place(x=100,y=225)

# Add text "Path to wallpaper"
pathtext = Label(window, text="Path to wallpaper", font=("Arial", 10), fg="black", bg="white")
pathtext.place(x=145,y=260)

# Add text "Path cant have any spaces"
pathtext = Label(window, text="Path cant have any spaces", font=("Arial", 10), fg="black", bg="white")
pathtext.place(x=120,y=280)

# Add input box for path to custom wallpaper
pathtocustomwallpaper = StringVar(window)
wallpaperinput = Entry(window, textvariable=pathtocustomwallpaper, width=50, bd=2.5)
wallpaperinput.place(x=45,y=300)

# Button that sets wallpaper as active
setbutton = Button(window, text="Set", command=lambda:playvideo(os.path.abspath(pathtocustomwallpaper.get()), monitor.get()))
setbutton.place(x=185,y=390)

# Add text "Monitor number (main monitor is 0)"
pathtext = Label(window, text="Monitor number (main monitor is 0)", font=("Arial", 10), fg="black", bg="white")
pathtext.place(x=110,y=325)

# Add input box for selecting monitor
monitor = StringVar(window)
wallpaperinput = Entry(window, textvariable=monitor, width=2, bd=2.5)
wallpaperinput.place(x=190,y=350)

# Add text for my credit :)
credit = Label(window, text="by:jarabum", width=8, height=int(0.5), fg="black", bg="white")
credit.place(x=0,y=410)

window.mainloop() # Create window for GUI