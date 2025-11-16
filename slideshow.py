import os
import ctypes
from tkinter import *

icon = os.path.abspath("images/wallpapers/pozadi3.png")

slideshow = []
slideshowwin = None
currentwallpaper = 0
wallpapertime = 5

# Function for changing wallpaper    
def change_wallpaper(image_path):
    # Constants for setting the wallpaper
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02
    print(image_path)

    try:
        # Call Windows API to change wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path,
                                                   SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
        return True
    except Exception as e:
        # Print error message if wallpaper change fails
        print(f"Error changing wallpaper: {e}")
        return False


# Function for appending path of wallpaper to slideshowappend variable
def slideshowappend():
    appendtext = pathtoslideshowwallpaper.get()
    if appendtext.strip():
        slideshow.append(appendtext)
        print(slideshow)

# Function for setting time for slideshow
def settime():
    global wallpapertime
    try:
        wallpapertime = int(wallpapertimeinput.get())
        print(wallpapertime)
    except ValueError:
        print("Invalid time")

# Function for running slideshow
def runslideshow():
    global currentwallpaper

    if slideshowwin is None:
        return
    if not slideshowwin.winfo_exists():
        return
    if len(slideshow) == 0:
        return
    
    change_wallpaper(os.path.abspath(slideshow[currentwallpaper]))
    currentwallpaper = (currentwallpaper + 1) % len(slideshow)
    slideshowwin.after(wallpapertime * 1000, runslideshow)


# Function for starting slideshow
def start():
    print("Starting slideshow")
    change_wallpaper(os.path.abspath(slideshow[0]))
    global slideshowwin
    window.destroy()

    # Window for slideshow
    slideshowwin = Tk() # Instantiate an instance of a window for slideshow
    slideshowwin.geometry("250x25")
    slideshowwin.title("Wallpaper Changer - slideshow :)")
    slideshowwin.config(background="white")
    slideshowwin.resizable(False, False)

    # Add text "Leave me open for slideshow"
    slideshowtext = Label(slideshowwin, text="Leave me open for slideshow", font=("Arial", 10, "bold"), fg="black", bg="white")
    slideshowtext.pack()

    # Run slideshow
    slideshowwin.after(1000, runslideshow)

    slideshowwin.mainloop()
        

# Main window 
window = Tk() # Instantiate an instance of a window
# Some window settings
window.geometry("400x380")
window.title("Wallpaper Changer - slideshow :)")
window.config(background="white")
window.resizable(False, False)

# Set window icon
icon = PhotoImage(file=icon) # Convert icon image to PhotoImage
window.iconphoto(True,icon)

# Add text "Wallpaper Slideshow"
name = Label(window, text="Wallpaper Slideshow", font=("Arial", 25, "bold"), fg="black", bg="white")
name.pack(padx=20, pady=20)

# Add text "Path to wallpaper for slideshow"
pathtext = Label(window, text="Path to wallpaper for slideshow", font=("Arial", 10), fg="black", bg="white")
pathtext.place(x=110,y=75)

# Add input box for path to slideshow wallpaper
pathtoslideshowwallpaper = StringVar(window)
wallpaperinput = Entry(window, textvariable=pathtoslideshowwallpaper, width=50, bd=2.5)
wallpaperinput.place(x=45,y=100)

# Button that adds wallpaper to slideshow
addbutton = Button(window, text="Add to slideshow", command=lambda:slideshowappend())
addbutton.place(x=150,y=125)

# Add text "Time between wallpapers"
timetext = Label(window, text="Time between wallpapers (seconds)", font=("Arial", 10), fg="black", bg="white")
timetext.place(x=95,y=175)

# Add input box for time between wallpapers
wallpapertimeinput = StringVar(window)
wallpaperinputtime = Entry(window, textvariable=wallpapertimeinput, width=10, bd=2.5)
wallpaperinputtime.place(x=165,y=200)

# Button that sets time between wallpapers
setbutton = Button(window, text="Set", command=lambda:settime())
setbutton.place(x=185,y=225)

# Button that starts slideshow
startbutton = Button(window, text="Start slideshow", width=15, height=3, command=lambda:start())
startbutton.place(x=143,y=275)

# Add text for my credit :)
credit = Label(window, text="by:jarabum", width=8, height=int(0.5), fg="black", bg="white")
credit.place(x=0,y=360)

window.mainloop() # Create window for GUI
