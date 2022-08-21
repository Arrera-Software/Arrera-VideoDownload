from tkinter import*
import subprocess
import os
from time import*
import webbrowser

def terminal():
    os.popen("gnome-terminal")
def PYPI():
    webbrowser.open("https://pypi.org/")
def HourSup(h1):
    hour = strftime("%H")
    h1 = int(h1)
    hourINT = int(hour)
    if hourINT >= h1:
        return True
    else :
        return False
def HourInf(h1):
    hour = strftime("%H")
    h1 = int(h1)
    hourINT = int(hour)
    if hourINT <= h1:
        return True
    else :
        return False
ResultatHour1 = HourSup(21)
ResultatHour2 = HourInf(6)
if ResultatHour1 == False or ResultatHour2 == False :
    Color = "white"
    TextColor = "black"
if ResultatHour1 == True or ResultatHour2 == True :
    Color = "black"
    TextColor = "white"

screen = Tk()
MenuNavigation = Menu(screen,bg=Color,fg=TextColor)
MenuNavigation.add_command(label="Terminal",command=terminal)
MenuNavigation.add_command(label="Installer de module",command=PYPI)
def Jupyter():
    os.popen("jupyter notebook")
def Spyder():
    os.popen("/usr/bin/spyder")
screen.title("Arrera IA Navigator")
screen.iconphoto(False,PhotoImage(file="image/Icon.png"))
screen.maxsize(700,250)
screen.minsize(700,250)
screen.config(bg=Color)
Label1 = Label(screen,bg=Color,width=20)
Label2 = Label(screen,bg=Color,width=20)
BoutonSpyder = Button(screen,text="S",command=Spyder,bg=Color)
BoutonJypiter = Button(screen,text="J",command=Jupyter,bg=Color)
IconSpyder = PhotoImage(file="image/IconSpyder.png",master=BoutonSpyder)
IconJupyter = PhotoImage(file="image/IconJupyter.png",master=BoutonSpyder)
BoutonSpyder.image_names = IconSpyder
BoutonJypiter.image_names = IconJupyter
BoutonSpyder.config(image=IconSpyder)
BoutonJypiter.config(image=IconJupyter)
Label1.pack(side="left")
BoutonSpyder.pack(side="left")
Label2.pack(side="right")
BoutonJypiter.pack(side="right")
screen.config(menu=MenuNavigation)
screen.mainloop()