from shutil import which
from tkinter import*
import webbrowser

Color = "grey"
ColorBTN = "white"

screen = Tk()
def Python():
    webbrowser.open("https://docs.python.org/fr/3")
def C():
    webbrowser.open("https://devdocs.io/c/")
def Cpp():
    webbrowser.open("https://docs.microsoft.com/fr-fr/cpp/cpp/?view=msvc-170")
def bash():
    webbrowser.open("https://www.gnu.org/software/bash/manual/bash.html")
screen.config(bg=Color)
screen.title("Arrera Tout Savoir")
screen.minsize(600,300)
screen.iconphoto(False,PhotoImage(file="image/Icon.png"))
cadreLanguage = Frame(screen,bg=Color,width=500,height=200)

BoutonPython = Button(cadreLanguage,text=" Python  \n  ",command=Python,bg=ColorBTN)
BoutonC = Button(cadreLanguage,     text="Language \n C",command=C,bg=ColorBTN)
BoutonBash = Button(cadreLanguage,  text="  Bash   \n  ",command = bash,bg=ColorBTN)
BoutonCpp = Button(cadreLanguage,   text="Language \n C++",command=Cpp,bg=ColorBTN)

LabelEcrat1 = Label(cadreLanguage,bg=Color,width=5)
LabelEcrat2 = Label(cadreLanguage,bg=Color,width=5)

cadreLanguage.place(relx=.5, rely=.5, anchor="center")
BoutonPython.place(x="0",y="100")
BoutonBash.place(x="100",y="100")
BoutonC.place(x="250",y="100")
BoutonCpp.place(x="380",y="100")
screen.mainloop()