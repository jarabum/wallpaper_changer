import ctypes
import os
from tkinter import *

wallpaper1 = os.path.abspath("images/wallpapers/testpozadi.jpg")
wallpaper2 = os.path.abspath("images/wallpapers/testpozadi2.jpg")
wallpaper3 = os.path.abspath("images/wallpapers/pozadi3.png")

wallpaper1iconpath = os.path.abspath("images/icons/wallpaper1icon.png")
wallpaper2iconpath = os.path.abspath("images/icons/wallpaper2icon.png")
wallpaper3iconpath = os.path.abspath("images/icons/wallpaper3icon.png")

pathtocustomwallpaper = "images/wallpapers/testpozadi2.jpg"
customwallpaper = os.path.abspath(pathtocustomwallpaper)

def change_wallpaper(image_path):
    # Constants for setting the wallpaper
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02

    try:
        # Call Windows API to change wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path,
                                                   SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
        return True
    except Exception as e:
        # Print error message if wallpaper change fails
        print(f"Error changing wallpaper: {e}")
        return False
    
window = Tk() # Instantiate an instance of a window
window.geometry("400x400")
window.title("Wallpaper Changer :)")
window.config(background="white")
window.resizable(False, False)

icon = PhotoImage(file=wallpaper3) # Convert icon image to PhotoImage
window.iconphoto(True,icon) # Set window icon

name = Label(window, text="Wallpaper Changer", font=("Arial", 25, "bold"), fg="black", bg="white")
name.pack(padx=20, pady=20) # Add text "Wallpaper Changer to window"

wallpaper1icon = PhotoImage(file=wallpaper1iconpath)
wallpaper1b = Button(window, text="wallpaper1", image=wallpaper1icon, command=lambda:change_wallpaper(wallpaper1))
wallpaper1b.place(x=25,y=100) # Create button for wallpaper 1

wallpaper2icon = PhotoImage(file=wallpaper2iconpath)
wallpaper2b = Button(window, text="wallpaper2", image=wallpaper2icon, command=lambda:change_wallpaper(wallpaper2))
wallpaper2b.place(x=150,y=100) # Create button for wallpaper 2

wallpaper3icon = PhotoImage(file=wallpaper3iconpath)
wallpaper3b = Button(window, text="wallpaper3", image=wallpaper3icon, command=lambda:change_wallpaper(wallpaper3))
wallpaper3b.place(x=275,y=100) # Create button for wallpaper 3

customtext = Label(window, text="Set custom wallpaper", font=("Arial", 15, "bold"), fg="black", bg="white")
customtext.place(x=100,y=225) # Add text "Set custom wallpaper"

pathtext = Label(window, text="Path to wallpaper", font=("Arial", 10), fg="black", bg="white")
pathtext.place(x=130,y=260)

wallpaperinput = Entry(window, textvariable=pathtocustomwallpaper)
wallpaperinput.place(x=130,y=280)

credit = Label(window, text="by:jarabum", width=8, height=int(0.5), fg="black", bg="white")
credit.place(x=0,y=380) # Add text for my credit :)

window.mainloop() # Create window for GUI