from tkinter import*
from urllib.robotparser import RequestRate
from ModuleInternet import*
import os
from time import*

def Touches(fenetre,fonc1,touche1,fonc2,touche2,fonc3,touche3,fonc4,touche4,fonc5,touche5):
    def anychar(event):
        if event.keycode == touche1:
            fonc1()
        if event.keycode == touche2:
            fonc2() 
        if event.keycode == touche3:
            fonc3()
        if event.keycode == touche4:
            fonc4() 
        if event.keycode == touche5:
            fonc5() 
    fenetre.bind("<Key>", anychar)

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

def Calculatrice():
    os.popen("gnome-calculator")
def FileSearch(name,path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)
def GrandRecherche(query):
    googleSearch(query)
    duckduckgoSearch(query)
    QwantSearch(query)
    EcosiaSearch(query)
    bingSearch(query) 

def NoInternet():
    ScreenSearch = Tk()
    ScreenSearch.title("Arrera Recherche")
    ScreenSearch.maxsize(525,70)
    ScreenSearch.minsize(525,70)
    ScreenSearch.config(bg="black")
    label=Label(ScreenSearch,text="Pas d'acces a internet",font=("arial",30),bg="black",fg="white").pack()
    ScreenSearch.mainloop()

def InterafaceSearch():
    ResultatHour1 = HourSup(21)
    ResultatHour2 = HourInf(6)
    if ResultatHour1 == False or ResultatHour2 == False :
        Color = "white"
        TextColor = "black"
    if ResultatHour1 == True or ResultatHour2 == True :
        Color = "black"
        TextColor = "white"
    TailleText =  "15"
    ScreenSearch = Tk()
    ScreenSearch.iconphoto(False,PhotoImage(file="image/ArreraRecherche.png"))
    ScreenSearch.title("Arrera Recherche")
    ScreenSearch.maxsize(550,680)
    ScreenSearch.minsize(550,680)
    ScreenSearch.config(bg=Color)
    #Cadre
    CadreSearch = Frame(ScreenSearch,bg=Color)

    #CadreAPP = Frame(ScreenSearch,bg=Color)
    CadreInternet = Frame(ScreenSearch,bg=Color)
    CadreTrad = Frame(ScreenSearch,bg=Color)
    CadreFile = Frame(ScreenSearch,bg=Color)
    CadreDico = Frame(ScreenSearch,bg=Color)
    CadreMusic = Frame(ScreenSearch,bg=Color)
    CadreCalcule = Frame(ScreenSearch,bg=Color)
    #Bouton
    BoutonLarousse = Button(CadreDico,bg="blue",fg="white",text="Definition\n Larousse",width=5,height=3)
    BoutonWikipedia = Button(CadreDico,bg="blue",fg="white",text="Definition\n Wikipedia",width=5,height=3)
    BoutonDuck = Button(CadreInternet,bg="blue")
    BoutonGoogle = Button(CadreInternet,bg="blue")
    BoutonEcosia = Button(CadreInternet,bg="blue")
    BoutonBing = Button(CadreInternet,bg="blue")
    BoutonQwant = Button(CadreInternet,bg="blue")
    BoutonMRArerra = Button(CadreInternet,bg="blue")    
    BoutonGoogleTrad = Button(CadreTrad,bg="blue")
    BoutonWord = Button(CadreTrad,bg="blue")
    BoutonFile = Button(CadreFile,bg="blue")
    BoutonMusic = Button(CadreMusic,bg="blue")
    LabelCalcule = Label(CadreCalcule,bg="grey",fg="white",width=50,height=15)
    BoutonCalcule = Button(CadreCalcule,bg="blue",fg="white",text="Fin",width=30,font=("arial","30"))
    #BoutonApplication = Button(CadreAPP,bg="blue")
    #Image
    IconDuck = PhotoImage(file="image/duck.png",master=BoutonDuck)
    IconGoogle = PhotoImage(file="image/google.png",master=BoutonGoogle)
    IconEcosia = PhotoImage(file="image/ecosia.png",master=BoutonEcosia)
    IconBing = PhotoImage(file="image/bing.png",master=BoutonBing)
    IconQwant = PhotoImage(file="image/qwant.png",master=BoutonQwant)
    IconMRArerra =  PhotoImage(file="image/MoteurArreraRecherche.png",master=BoutonMRArerra)
    IconWordreference =  PhotoImage(file="image/Wordreference.png",master=BoutonWord)
    IconGoogleTrad =  PhotoImage(file="image/googleTrad.png",master=BoutonGoogleTrad)
    IconFile =  PhotoImage(file="image/fichier.png",master=BoutonFile)
    IconMusic =  PhotoImage(file="image/Music.png",master=BoutonMusic)
    #IconApp =   PhotoImage(file="image/Application.png",master=BoutonApplication)

    BoutonDuck.image_names = IconDuck
    BoutonGoogle.image_names = IconGoogle
    BoutonEcosia.image_names = IconEcosia
    BoutonBing.image_names = IconBing
    BoutonQwant.image_names = IconQwant
    BoutonMRArerra.image_names = IconMRArerra
    BoutonWord.image_names = IconWordreference
    BoutonGoogleTrad.image_names = IconGoogleTrad
    BoutonFile.image_names = IconFile
    BoutonMusic.image_names = IconMusic
    #BoutonApplication.image_names = IconApp

    BoutonDuck.config(image = IconDuck)
    BoutonGoogle.config(image =IconGoogle)
    BoutonEcosia.config(image = IconEcosia)
    BoutonBing.config(image = IconBing)
    BoutonQwant.config(image =IconQwant)
    BoutonMRArerra.config(image =IconMRArerra)
    BoutonWord.config(image =IconWordreference)
    BoutonGoogleTrad.config(image=IconGoogleTrad)
    BoutonFile.config(image=IconFile)
    BoutonMusic.config(image=IconMusic)
    #BoutonApplication.config(image=IconApp )   
    #Label
    LabelEcart1 = Label(CadreDico,width=13,height=3,bg=Color)
    LabelEcart2 = Label(CadreDico,width=13,height=3,bg=Color)

    LabelEcart3 = Label(CadreInternet,width=3,height=5,bg=Color)
    LabelEcart4 = Label(CadreInternet,width=3,height=5,bg=Color)
    LabelEcart5 = Label(CadreInternet,width=3,height=5,bg=Color)
    LabelEcart6 = Label(CadreInternet,width=3,height=5,bg=Color)
    LabelEcart7 = Label(CadreInternet,width=3,height=5,bg=Color)

    LabelEcart8 = Label(CadreTrad,width=13,height=3,bg=Color)
    LabelEcart9 = Label(CadreTrad,width=13,height=3,bg=Color)

    LabelEcart10 = Label(CadreCalcule,width=13,height=3,bg=Color)
    LabelEcart11 = Label(CadreCalcule,width=13,height=3,bg=Color)
    #Zone de texte
    def FinCal():
        CadreCalcule.pack_forget()
        CadreInternet.pack()
        CadreTrad.pack()
        CadreFile.pack()
        CadreDico.pack()
        CadreMusic.pack()
        BoutonValider.config(command=Valider)
    ZoneEntrer = Entry(CadreSearch,width=50)
    def DuckTouche():
        requette = ZoneEntrer.get()
        duckduckgoSearch(requette)
    def GoogleTouche():
        requette = ZoneEntrer.get()
        googleSearch(requette)
    def GrandSearchTouche():
        requette = ZoneEntrer.get()
        GrandRecherche(requette)
    def YTmusicTouche():
        requette = ZoneEntrer.get()
        YTmusicSearch(requette)
    def Valider():
        requette = ZoneEntrer.get()
        #Command
        def Larousse():
            LarousseSearch(requette)
        def Wikipedia():
            WikipediaSearch(requette)
        def Duck():
            duckduckgoSearch(requette)
        def Google():
            googleSearch(requette)
        def Ecosia():
            EcosiaSearch(requette)
        def Bing():
            bingSearch(requette)
        def Qwant():
            QwantSearch(requette)
        def MRarrera():
            GrandRecherche(requette)
        def GoogleTrad():
            googleTrad(requette)
        def Wordreference():
            WordreferenceSearch(requette)
        def Music():
            YTmusicSearch(requette)
        def File():
            Search = str(FileSearch(requette,"/"))
            ScreenFile = Toplevel()
            def CopierPath():
                cp = ScreenFile.clipboard_get()
                cp
                ScreenFile.clipboard_clear()
                ScreenFile.clipboard_append(Search)  
            ScreenFile.title("Fichier")
            ScreenFile.config(bg=Color)
            ScreenFile.minsize(800,70)
            LabelResultat = Label(ScreenFile,text=Search,bg=Color,fg=TextColor).pack(side="left")
            BoutonCopier = Button(ScreenFile,text="Copier le chemin",bg=Color,fg=TextColor,command=CopierPath).pack(side="right")
        if requette == "Calcule" or requette == "calcule":
            Calculatrice()
        if requette == "meteo" or requette == "meteo" :
            Mcarte()
        #Config
        BoutonLarousse.config(command=Larousse)
        BoutonWikipedia.config(command=Wikipedia)
        BoutonDuck.config(command=Duck)
        BoutonGoogle.config(command=Google)
        BoutonEcosia.config(command=Ecosia)
        BoutonBing.config(command=Bing)
        BoutonQwant.config(command=Qwant)
        BoutonMRArerra.config(command=MRarrera)
        BoutonGoogleTrad.config(command=GoogleTrad)
        BoutonWord.config(command=Wordreference)
        BoutonFile.config(command=File)
        BoutonMusic.config(command=Music)

    #Bouton
    BoutonValider = Button(CadreSearch,command=Valider)
    IconValider = PhotoImage(master=BoutonValider,file="image/ArreraRecherche.png")
    BoutonValider.image_names = IconValider
    BoutonValider.config(image=IconValider,bg=Color)
    Touches(ScreenSearch,DuckTouche,96,GoogleTouche,67,GrandSearchTouche,68,YTmusicTouche,69,Valider,36)
    #Label
    LabelLigne = Label(ScreenSearch,bg="white",width=1000,height=1)
    Ligne = PhotoImage(file="image/ligne.png",master=LabelLigne)
    LabelLigne.image_names = Ligne
    LabelLigne.config(image=Ligne)   
    #LabelCategorie1 = Label(CadreAPP,text="Application",font=("arial",TailleText ),bg=Color,fg=TextColor)
    LabelCategorie2 = Label(CadreInternet,text="Recherche Internet",font=("arial",TailleText ),bg=Color,fg=TextColor)
    LabelCategorie3 = Label(CadreTrad,text="Traduction",font=("arial",TailleText ),bg=Color,fg=TextColor)
    LabelCategorie4 = Label(CadreFile,text="Fichier",font=("arial",TailleText ),bg=Color,fg=TextColor)
    LabelCategorie5 = Label(CadreDico,text="Dictionnaire",font=("arial",TailleText ),bg=Color,fg=TextColor)
    LabelCategorie6 = Label(CadreMusic,text="Musique",font=("arial",TailleText ),bg=Color,fg=TextColor)
    #affichage
    #cadre
    CadreSearch.pack()
    LabelLigne.pack()
    #CadreAPP.pack()
    CadreInternet.pack()
    CadreTrad.pack()
    CadreFile.pack()
    CadreDico.pack()
    CadreMusic.pack()
    #widget
    ZoneEntrer.pack(side="left")
    BoutonValider.pack(side="right")
    #LabelCategorie1.pack()
    LabelCategorie2.pack()
    LabelCategorie3.pack()
    LabelCategorie4.pack()
    LabelCategorie5.pack()
    LabelCategorie6.pack()
    BoutonLarousse.pack(side="left")
    LabelEcart1.pack(side="left")
    BoutonWikipedia.pack(side="right")
    LabelEcart2.pack(side="right")
    BoutonBing.pack(side="left")
    LabelEcart3.pack(side="left")
    BoutonEcosia.pack(side="left")
    LabelEcart5.pack(side="left")
    BoutonDuck.pack(side="left")
    BoutonQwant.pack(side="right")
    LabelEcart4.pack(side="right")
    BoutonGoogle.pack(side="right")
    LabelEcart6.pack(side="right")
    BoutonMRArerra.pack(side="right")
    LabelEcart7.pack(side="right")
    BoutonGoogleTrad.pack(side="right")
    LabelEcart8.pack(side="right")
    BoutonWord.pack(side="left")
    LabelEcart9.pack(side="left")
    BoutonFile.pack()
    BoutonMusic.pack()
    LabelEcart10.pack()
    LabelCalcule.pack()
    LabelEcart11.pack()
    BoutonCalcule.pack()
    #BoutonApplication.pack()
    ScreenSearch.mainloop()   


EtatInternet = TestInternet()
if EtatInternet == True:
    InterafaceSearch()
if EtatInternet == False :
    NoInternet()