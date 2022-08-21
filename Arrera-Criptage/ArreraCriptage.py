from tkinter import*
import os
from time import*
def ArreraCriptage(para,phrase):
    if para == "Criptage":
        phrase = phrase.replace("a","&")
        phrase = phrase.replace("b","2")
        phrase = phrase.replace("c","{")
        phrase = phrase.replace("d","0")
        phrase = phrase.replace("e","6")
        phrase = phrase.replace("f","1")
        phrase = phrase.replace("g","@")
        phrase = phrase.replace("h","°")
        phrase = phrase.replace("i","'")
        phrase = phrase.replace("j","ç")
        phrase = phrase.replace("k","€")
        phrase = phrase.replace("l","§")
        phrase = phrase.replace("m","<")
        phrase = phrase.replace("n",",")
        phrase = phrase.replace("o","~")
        phrase = phrase.replace("p","=")
        phrase = phrase.replace("q","|")
        phrase = phrase.replace("r","}")
        phrase = phrase.replace("s","%")
        phrase = phrase.replace("t","$")
        phrase = phrase.replace("u","[")
        phrase = phrase.replace("v","ø")
        phrase = phrase.replace("w","£")
        phrase = phrase.replace("x","-")
        phrase = phrase.replace("y","#")
        phrase = phrase.replace("z","?")
        phrase = phrase.replace("A","&")
        phrase = phrase.replace("B","2")
        phrase = phrase.replace("C","{")
        phrase = phrase.replace("D","0")
        phrase = phrase.replace("E","6")
        phrase = phrase.replace("F","1")
        phrase = phrase.replace("G","@")
        phrase = phrase.replace("H","°")
        phrase = phrase.replace("I","'")
        phrase = phrase.replace("J","ç")
        phrase = phrase.replace("K","€")
        phrase = phrase.replace("L","§")
        phrase = phrase.replace("M","<")
        phrase = phrase.replace("N",",")
        phrase = phrase.replace("O","~")
        phrase = phrase.replace("P","=")
        phrase = phrase.replace("Q","|")
        phrase = phrase.replace("R","}")
        phrase = phrase.replace("S","%")
        phrase = phrase.replace("T","$")
        phrase = phrase.replace("U","[")
        phrase = phrase.replace("V","ø")
        phrase = phrase.replace("W","£")
        phrase = phrase.replace("X","-")
        phrase = phrase.replace("Y","#")
        phrase = phrase.replace("Z","?")
        return phrase
    if para == "decriptage":
        phrase = phrase.replace("&","a")
        phrase = phrase.replace("2","b")
        phrase = phrase.replace("{","c")
        phrase = phrase.replace("0","d")
        phrase = phrase.replace("6","e")
        phrase = phrase.replace("1","f")
        phrase = phrase.replace("@","g")
        phrase = phrase.replace("°","h")
        phrase = phrase.replace("'","i")
        phrase = phrase.replace("ç","j")
        phrase = phrase.replace("€","k")
        phrase = phrase.replace("§","l")
        phrase = phrase.replace("<","m")
        phrase = phrase.replace(",","n")
        phrase = phrase.replace("~","o")
        phrase = phrase.replace("=","p")
        phrase = phrase.replace("|","q")
        phrase = phrase.replace("}","r")
        phrase = phrase.replace("%","s")
        phrase = phrase.replace("$","t")
        phrase = phrase.replace("[","u")
        phrase = phrase.replace("ø","v")
        phrase = phrase.replace("£","w")
        phrase = phrase.replace("-","x")
        phrase = phrase.replace("#","y")
        phrase = phrase.replace("?","z")
        return phrase

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
screen.title("Arrera Criptage")
screen.minsize(500,200)
screen.maxsize(500,200)
screen.config(bg=Color)
LabelIndication = Label(screen,text="Arrera Criptage",bg = Color ,fg=TextColor,font=("arial","20"))
LabelEcart= Label(screen,bg="grey",width=1000,height=1)
WidgEntry = Entry(width=250)
def Cript():
    requette = WidgEntry.get()
    def Copie():
        cp = screen2.clipboard_get()
        cp
        screen2.clipboard_clear()
        screen2.clipboard_append(Phrase)
    Phrase = ArreraCriptage("Criptage",requette)
    screen2 = Toplevel()
    screen2.title("Arrera Criptage")
    screen2.minsize(500,200)
    screen2.maxsize(500,200)
    screen2.config(bg=Color)
    Label1 = Label(screen2,text=Phrase,bg=Color,fg=TextColor).place(relx=.5, rely=.5, anchor="center")
    BoutonCopier = Button(screen2,text="Copier",bg=Color,fg=TextColor,command=Copie).pack(side="bottom")
def Decript():
    requette = WidgEntry.get()
    def Copie():
        cp = screen2.clipboard_get()
        cp
        screen2.clipboard_clear()
        screen2.clipboard_append(Phrase)
    Phrase = ArreraCriptage("decriptage",requette)
    screen2 = Toplevel()
    screen2.title("Arrera Criptage")
    screen2.minsize(500,200)
    screen2.maxsize(500,200)
    screen2.config(bg=Color)
    Label1 = Label(screen2,text=Phrase,bg=Color,fg=TextColor).place(relx=.5, rely=.5, anchor="center")
    BoutonCopier = Button(screen2,text="Copier",bg=Color,fg=TextColor,command=Copie).pack(side="bottom")
BoutonCrip = Button(screen,text="Cripter",bg=Color,fg=TextColor,command=Cript)
BoutonDeCrip = Button(screen,text="Decripter",bg=Color,fg=TextColor,command=Decript)
LabelIndication.pack()
LabelEcart.pack()
WidgEntry.pack()
BoutonCrip.pack(side="left")
BoutonDeCrip.pack(side="right")

screen.mainloop()