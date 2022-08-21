from tkinter import*
import webbrowser
Navigateur = "firefox"
from time import*

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
    color = "white"
if ResultatHour1 == True or ResultatHour2 == True :
    color = "black"

def LeMonde():
    webbrowser.get(Navigateur).open("https://www.lemonde.fr/")
def VoixDuNord():
    webbrowser.get(Navigateur).open("https://www.lavoixdunord.fr/")
def ONU():
    webbrowser.get(Navigateur).open("https://news.un.org/fr/")
def Frandroid():
    webbrowser.get(Navigateur).open("https://www.frandroid.com/")
def Liberation():
    webbrowser.get(Navigateur).open("https://www.liberation.fr/")
def Mcarte():
    webbrowser.get(Navigateur).open("https://meteofrance.com/previsions-meteo-france/pas-de-calais/62")
def Mvigilance():
    webbrowser.get(Navigateur).open("https://vigilance.meteofrance.fr/fr")
def FlipBoard():
    webbrowser.get(Navigateur).open("https://flipboard.com/")
def ArreraNews():
    screen1=Tk()
    screen1.title("Arrera News")
    screen1.minsize(300,400)
    screen1.maxsize(300,400)
    screen1.config(bg=color)
    CadreRight = Frame(screen1,width=500,height=250,bg=color)
    CadreLeft = Frame(screen1,width=500,height=250,bg=color)
    #boutton

    BoutonLeMonde=Button(CadreRight,bg=color)
    IconLeMonde=PhotoImage(master=BoutonLeMonde,file="image/IconLeMonde.png")
    BoutonLeMonde.image_names = IconLeMonde
    BoutonLeMonde.config(command=LeMonde,image=IconLeMonde)

    BoutonVoixDuNOrd=Button(CadreRight,bg=color)
    IconVoixDuNord=PhotoImage(master=BoutonVoixDuNOrd,file="image/LogoVoixNord.png")
    BoutonVoixDuNOrd.image_names = IconVoixDuNord
    BoutonVoixDuNOrd.config(command=VoixDuNord,image=IconVoixDuNord)

    BoutonONU=Button(CadreRight,bg=color)
    IconONU=PhotoImage(master=BoutonONU,file="image/IconONU.png")
    BoutonONU.image_names = IconONU
    BoutonONU.config(command=ONU,image=IconONU)

    BoutonFrandoid=Button(CadreRight,bg=color)
    IconFrandoid=PhotoImage(master=BoutonFrandoid,file="image/IconFrandroid.png")
    BoutonFrandoid.image_names = IconFrandoid
    BoutonFrandoid.config(command=Frandroid,image=IconFrandoid)

    BoutonLiberation=Button(CadreLeft,bg=color)
    IconLiberation=PhotoImage(master=BoutonLiberation,file="image/IconLiberation.png")
    BoutonLiberation.image_names = IconLiberation
    BoutonLiberation.config(command=Liberation,image=IconLiberation)

    BoutonMcarte=Button(CadreLeft,bg=color)
    IconMcarte=PhotoImage(master=BoutonMcarte,file="image/IconCarte.png")
    BoutonMcarte.image_names = IconMcarte
    BoutonMcarte.config(command=Mcarte,image=IconMcarte)

    BoutonMvigilance=Button(CadreLeft,bg=color)
    IconMvigilance=PhotoImage(master=BoutonMvigilance,file="image/IconVigilance.png")
    BoutonMvigilance.image_names = IconMvigilance
    BoutonMvigilance.config(command=Mvigilance,image=IconMvigilance)

    BoutonFilboard=Button(CadreLeft,bg=color)
    IconFlipBoard=PhotoImage(master=BoutonFilboard,file="image/IconFlipboard.png")
    BoutonFilboard.image_names = IconFlipBoard
    BoutonFilboard.config(command=FlipBoard,image=IconFlipBoard)

    #Label
    Label1 = Label(screen1,height=10,bg=color)
    Label2=Label(CadreRight,width=5,bg=color)
    Label3=Label(CadreRight,width=5,bg=color)
    Label4=Label(CadreRight,width=5,bg=color)
    Label5=Label(CadreLeft,width=5,bg=color)
    Label6=Label(CadreLeft,width=5,bg=color)
    Label7=Label(CadreLeft,width=5,bg=color)
    #affichage
    CadreLeft.pack(side="left")
    CadreRight.pack(side="right")
    BoutonLeMonde.pack()
    Label2.pack()
    BoutonVoixDuNOrd.pack()
    BoutonONU.pack()
    Label3.pack()
    BoutonFrandoid.pack()
    BoutonLiberation.pack()
    BoutonMcarte.pack()
    Label6.pack()
    BoutonMvigilance.pack()
    Label7.pack()
    BoutonFilboard.pack()
    screen1.mainloop()

ArreraNews()