from pytube import*
from tkinter import*
from tkinter import Tk, filedialog
from tkinter.messagebox import showinfo ,showerror
import os
import webbrowser
from PIL import Image, ImageTk

class ArreraVideoDownload :
    def __init__(self,color,colorbutton,textcolorbutton,textcolorlabel):
        #Var 
        self.__nameApp = "Arrera Video Download"
        self.__versionApp = "I2024-3.00"
        self.__imagePath = "image/ArreraVideoDownload.png" 
        self.__copyrightApp = "Copyright Arrera Software by Baptiste P 2023-2024"
        #fenetre
        self.__screen = Tk()
        self.__varChoix = StringVar(self.__screen)
        self.__listChoix = ["simple","playlist"]
        self.__screen.title(self.__nameApp)
        self.__screen.config(bg=color)
        self.__screen.iconphoto(False,PhotoImage(file=self.__imagePath))
        self.__screen.maxsize(500,300)
        self.__screen.minsize(500,300)
        #Menu 
        menu = Menu(self.__screen)
        menu.add_command(label="A propos",command=self.__Apropop)
        self.__screen.configure(menu=menu)
        #cadre
        self.__cardeMain = Frame(self.__screen,bg=color,width=450,height=250)
        self.__cadreDownload = Frame(self.__screen,bg=color,width=450,height=250)
        self.__cadreWait = Frame(self.__screen,bg=color,width=450,height=250)
        #entry
        self.__entryURL = Entry(self.__cadreDownload,width=30,border=2,font=("arial","15"))
        #label
        self.__labelBeinvenu = Label(self.__cardeMain,text="Bienvenu sur Arrera Download",font=("arial","15"),bg=color,fg=textcolorlabel)
        self.__labelindiction = Label(self.__cadreDownload,font=("arial","15"),bg=color,fg=textcolorlabel)
        self.__labelWait = Label(self.__cadreWait,text="En court",font=("arial","25"),bg=color,fg=textcolorlabel)
        #option menu
        self.__menu = OptionMenu(self.__cadreDownload,self.__varChoix,*self.__listChoix)
        #button
        self.__boutonVideo = Button(self.__cardeMain,text="Télécharger \ndes vidéos",bg=colorbutton,fg=textcolorbutton,font=("arial","15"),command=self.__downloadVideoView)
        self.__boutonMusique = Button(self.__cardeMain,text="Télécharger \ndes musiques",bg=colorbutton,fg=textcolorbutton,font=("arial","15"),command=self.__downloadPlaylistView)
        self.__boutonRetour = Button(self.__cadreDownload,text="retour",bg=colorbutton,fg=textcolorbutton,font=("arial","15"),command=self.__main)
        self.__boutonDownload = Button(self.__cadreDownload,text="Télécharger",bg=colorbutton,fg=textcolorbutton,font=("arial","15"))
        self.__boutonYoutube = Button(self.__cadreDownload,text="Ouvrir Youtube",bg=colorbutton,fg=textcolorbutton,font=("arial","15"),command= lambda : webbrowser.open("https://www.youtube.com/"))
        #affichage
        self.__labelBeinvenu.place(relx=0.5, rely=0, anchor="n")
        self.__boutonVideo.place(x=0,y=100)
        self.__boutonMusique.place(x=313,y=100)
        
        self.__labelindiction.place(x=100,y=0)
        self.__menu.place(x=0,y=0)
        self.__entryURL.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.__boutonRetour.place(x=0,y=210)
        self.__boutonDownload.place(x=330,y=210)
        self.__boutonYoutube.place(relx=0.5, rely=1.0, anchor="s")
        
        self.__labelWait.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        self.__main()
        
        self.__screen.mainloop()
    
    def __downloadVideoSimple(self):
        self.__waitView()
        file = filedialog.askdirectory()
        if file :
            valURL = self.__entryURL.get()
            self.__entryURL.delete(0,END)
            Media = YouTube(valURL)
            downloadMedia = Media.streams.get_by_itag(18)
            downloadMedia.download(file)
            showinfo(title="Youtube Downloader",message="Video Télécharger")
        else :
           showerror(title="Video download",message="Aucun dossier selectionner") 
        self.__waitNoView()
    
    def __downloadVideoPlaylist(self):
        self.__waitView()
        file = filedialog.askdirectory()
        if file :
            valURL = self.__entryURL.get()
            self.__entryURL.delete(0,END)
            playlist = Playlist(valURL)
            for videos in playlist.videos:
                videos.streams.get_by_itag(18).download(file)      
            showinfo(title="Youtube Downloader",message="Video Télécharger")
        else :
           showerror(title="Video download",message="Aucun dossier selectionner") 
        self.__waitNoView()
    
    def __downloadMusiqueSimple(self):
        self.__waitView()
        file = filedialog.askdirectory()
        if file :
            valURL = self.__entryURL.get()
            self.__entryURL.delete(0,END)
            Media = YouTube(valURL)
            downloadMedia = Media.streams.filter(only_audio=True).first()
            out_file = downloadMedia.download(file)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            showinfo(title="Youtube Downloader",message="Video Télécharger")
        else :
           showerror(title="Video download",message="Aucun dossier selectionner")
        self.__waitNoView()
    
    def __downloadMusiquePlaylist(self):
        self.__waitView()
        file = filedialog.askdirectory()
        if file :
            valURL = self.__entryURL.get()
            self.__entryURL.delete(0,END)
            playlist = Playlist(valURL)
            for videos in playlist.videos:
                downloadMedia = videos.streams.filter(only_audio=True).first()
                out_file = downloadMedia.download(file)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
            showinfo(title="Youtube Downloader",message="Video Télécharger")
        else :
           showerror(title="Video download",message="Aucun dossier selectionner")
        self.__waitNoView()
    
    def __downloadVideo(self):
        var = self.__varChoix.get()
        if var == "simple" :
            self.__downloadVideoSimple()
        else :
            self.__downloadVideoPlaylist()
            
    
    def __downloadMusique(self):
        var = self.__varChoix.get()
        if var == "simple" :
            self.__downloadMusiqueSimple()
        else :
            self.__downloadMusiquePlaylist()
            
    
    def __main(self):
        self.__cadreDownload.place_forget()
        self.__cardeMain.place(relx=0.5,rely=0.5,anchor=CENTER)
        
    def __downloadView(self):
        self.__cardeMain.place_forget()
        self.__cadreDownload.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.__varChoix.set(self.__listChoix[0])
        
    def __waitView(self):
        self.__cadreDownload.place_forget()
        self.__cadreWait.place(relx=0.5,rely=0.5,anchor=CENTER)
        
    def __waitNoView(self):
        self.__cadreWait.place_forget()
        self.__cadreDownload.place(relx=0.5,rely=0.5,anchor=CENTER)

    
    def __downloadVideoView(self):
        self.__labelindiction.configure(text="Copier L'URL d'une video")
        self.__downloadView()
        self.__boutonDownload.config(command=self.__downloadVideo)
        self.__boutonRetour.config(command=self.__main)
        
    def __downloadPlaylistView(self):
        self.__labelindiction.configure(text="Copier L'URL d'une musique")
        self.__downloadView()
        self.__boutonDownload.config(command=self.__downloadMusique)
        self.__boutonRetour.config(command=self.__main)
    
    def __Apropop(self):
        #Variable
        tailleIMG = (100,100)
        #Creation de la fenetre
        about = Toplevel()
        about.iconphoto(False,PhotoImage(file=self.__imagePath))
        about.title("A propos : "+self.__nameApp)
        about.maxsize(400,300)
        about.minsize(400,300)
        #Traitement Image
        imageOrigine = Image.open(self.__imagePath)    
        imageRedim = imageOrigine.resize(tailleIMG)
        icon = ImageTk.PhotoImage(imageRedim)
        #Label
        labelIcon = Label(about,image=icon)
        labelName = Label(about,text="\n"+self.__nameApp+"\n",font=("arial","12"))
        labelVersion = Label(about,text=self.__versionApp+"\n",font=("arial","11"))
        labelCopyright = Label(about,text=self.__copyrightApp,font=("arial","9"))
        #affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()
        about.mainloop()
        
ArreraVideoDownload("white","red","white","black")