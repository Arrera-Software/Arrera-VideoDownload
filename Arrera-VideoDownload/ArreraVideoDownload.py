from pytube import*
from tkinter import*
from tkinter.messagebox import showinfo
from time import*
import os

def Ecriture(file,text):#Fonction d'écriture sur un fichier texte
    doc = open(file,"w")
    doc.truncate()
    doc.write(text)
    doc.close()
    return text,file
def Lecture(file):#Fonction de lecture d'un fichier texte et stokage dans une varriable
    fichier = open(file,"r")
    contenu= fichier.readlines()[0]
    fichier.close()
    return contenu

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
def FoncModif(file):
    Contenu = Lecture(file)
    ScreenModif = Toplevel()
    ScreenModif.maxsize(300,150)
    ScreenModif.minsize(300,150)
    ScreenModif.wait_visibility(ScreenModif)
    ScreenModif.wm_attributes('-alpha',0.9)
    ScreenModif.config(bg=Color)
    LabelContenu = Label(ScreenModif,text=Contenu,font=("arial","20"),bg=Color,fg=TextColor).pack()
    entry = Entry(ScreenModif)
    def Modif():
        Var = str(entry.get())
        Ecriture(file,Var)
        ScreenModif.destroy()
    Modif = Button(ScreenModif,text="Modifier",bg=Color,fg=TextColor,command=Modif).pack(side="right",anchor="s")
    entry.pack(side="left",anchor="s")

def FileChange1():
    FoncModif("Config/emplacementMusic.txt")
    FileMusic = str(Lecture("Config/emplacementMusic.txt"))
def FileChange2():
    FoncModif("Config/emplacementVideo.txt")
    FileVideo = str(Lecture("Config/emplacementVideo.txt"))
def YoutubeDownload():
    screen = Tk()
    FileMusic = str(Lecture("Config/emplacementMusic.txt"))
    FileVideo = str(Lecture("Config/emplacementVideo.txt"))
    screen.title("Arrera Video Download")
    menu = Menu(screen,bg=Color,fg=TextColor)
    screen.config(bg=Color,menu=menu)
    screen.iconphoto(False,PhotoImage(file="image/ArreraVideoDownload.png"))
    screen.maxsize(500,600)
    screen.minsize(500,600)
    #Menu
    Fichier = Menu(menu,tearoff=0)
    Fichier.add_command(label="Fichier musique",command=FileChange1)
    Fichier.add_command(label="Fichier video",command=FileChange2)
    menu.add_cascade(label="fichier",menu=Fichier)
    menu.add_command(label="A propos")
    #Label et Cadre
    LabelVideo = Label(screen,text= "Video",bg=Color,fg=TextColor,font=("arial","25"))
    CadreVideo = Frame(screen,bg=Color,width=400,height=100)
    LabelVideo2 = Label(screen,text= "Playlist Video",bg=Color,fg=TextColor,font=("arial","25"))
    CadreVideo2 = Frame(screen,bg=Color,width=400,height=100)
    LabelMusic = Label(screen,text= "Musique",bg=Color,fg=TextColor,font=("arial","25"))
    CadreMusic = Frame(screen,bg=Color,width=400,height=100)
    LabelMusic2 = Label(screen,text= "Playlist Musique",bg=Color,fg=TextColor,font=("arial","25"))
    CadreMusic2 = Frame(screen,bg=Color,width=400,height=100)
    LabelURL1 = Label(CadreVideo,text="Taper l'URL",fg=TextColor,bg=Color,font=("arial","15"))
    LabelURL2 = Label(CadreVideo2,text="Taper l'URL",fg=TextColor,bg=Color,font=("arial","15"))
    LabelURL3 = Label(CadreMusic,text="Taper l'URL",fg=TextColor,bg=Color,font=("arial","15"))
    LabelURL4 = Label(CadreMusic2,text="Taper l'URL",fg=TextColor,bg=Color,font=("arial","15"))
    #Entry
    EntryURL1 = Entry(CadreVideo,width=45)
    EntryURL2 = Entry(CadreVideo2,width=45)
    EntryURL3 = Entry(CadreMusic,width=45)
    EntryURL4 = Entry(CadreMusic2,width=45)
    #Fonction
    def AffichageCadre():
        LabelVideo.pack()
        CadreVideo.pack()
        LabelVideo2.pack()
        CadreVideo2.pack()
        LabelMusic.pack()
        CadreMusic.pack()
        LabelMusic2.pack()
        CadreMusic2.pack()
    def NoAffichageCadre():
        LabelVideo.pack_forget()
        CadreVideo.pack_forget()
        LabelVideo2.pack_forget()
        CadreVideo2.pack_forget()
        LabelMusic.pack_forget()
        CadreMusic.pack_forget()
        LabelMusic2.pack_forget()
        CadreMusic2.pack_forget()
    def Download1():
        URL = str(EntryURL1.get())
        Media = YouTube(URL)
        downloadMedia = Media.streams.get_by_itag(18)
        downloadMedia.download(FileVideo)
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        
    def Download2():
        URL = str(EntryURL2.get())
        playlist = Playlist(URL)
        for videos in playlist.videos:
            videos.streams.get_by_itag(18).download(FileVideo)
        showinfo(title="Youtube Downloader",message="Videos Télécharger")
    
    def Download3():
        URL = str(EntryURL3.get())
        Media = YouTube(URL)
        downloadMedia = Media.streams.filter(only_audio=True).first()
        out_file = downloadMedia.download(FileMusic)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        showinfo(title="Youtube Downloader",message="Musique Télécharger")

    def Download4():
        URL = str(EntryURL4.get())
        playlist = Playlist(URL)
        for videos in playlist.videos:
            downloadMedia = videos.streams.filter(only_audio=True).first()
            out_file = downloadMedia.download(FileMusic)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        showinfo(title="Youtube Downloader",message="Musiques Télécharger")
    #Bouton
    BoutonDownload1 = Button(CadreVideo,text="Télécharger",bg=Color,fg=TextColor,command=Download1)
    BoutonDownload2 = Button(CadreVideo2,text="Télécharger",bg=Color,fg=TextColor,command=Download2)
    BoutonDownload3 = Button(CadreMusic,text="Télécharger",bg=Color,fg=TextColor,command=Download3)
    BoutonDownload4 = Button(CadreMusic2,text="Télécharger",bg=Color,fg=TextColor,command=Download4)
    #Affichage
    AffichageCadre()
    LabelURL1.place(x="150",y="0")
    LabelURL2.place(x="150",y="0")
    LabelURL3.place(x="150",y="0")
    LabelURL4.place(x="150",y="0")
    EntryURL1.place(x="10",y="30")
    EntryURL2.place(x="10",y="30")
    EntryURL3.place(x="10",y="30")
    EntryURL4.place(x="10",y="30")
    BoutonDownload1.place(x="150",y="60")
    BoutonDownload2.place(x="150",y="60")
    BoutonDownload3.place(x="150",y="60")
    BoutonDownload4.place(x="150",y="60")
    screen.mainloop()

YoutubeDownload()
