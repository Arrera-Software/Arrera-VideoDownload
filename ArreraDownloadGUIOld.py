import customtkinter as ctk
from tkinter import*
from PIL import Image, ImageTk
from ArreraDownload import*
from tkinter.messagebox import*
from librairy.travailJSON import*
import threading as th
import webbrowser

class CArreraDGUI :
    def __init__(self) :
        # Fenetre
        self.__windows = ctk.CTk()
        
        # Var 
        self.__nameApp = "Arrera Download"
        self.__versionApp = "I2024-"
        self.__imagePath = "image/ArreraVideoDownload.png"
        self.__listMode = ["Video Simple","Juste sons","Juste Video"]
        self.__varGetMode = StringVar(self.__windows)
        
        # Parametrage de la fenetre
        self.__windows.title(self.__nameApp)
        self.__windows.maxsize(500,500)
        self.__windows.minsize(500,500)
        # self.__windows.iconbitmap("image/ArreraVideoDownload.ico")
        
        # Menu
        menu = Menu(self.__windows)
        menu.add_command(label = "A Propos",command=self.__Apropos)
        menu.add_command(label="Documentation",command= lambda : webbrowser.open("https://github.com/Arrera-Software/Arrera-VideoDownload/blob/main/README.md"))
        self.__windows.configure(menu=menu)
        
        # Widget
        labelTitle = ctk.CTkLabel(self.__windows,text="Arrera Download",font=("Arial",30))
        self.__entryURL = ctk.CTkEntry(self.__windows, placeholder_text="Entrez URL",font=("Arial",15),width=300)
        btnDownload = ctk.CTkButton(self.__windows,text ="Telecharger",font=("Arial",25),command=self.__download)
        btnChooseFile = ctk.CTkButton(self.__windows,text ="Dossier Sortie",font=("Arial",25),command=self.__setFolder)
        modeSelection = ctk.CTkOptionMenu(self.__windows,variable=self.__varGetMode,values=self.__listMode)
                
        # Affichage
        labelTitle.pack()
        modeSelection.place(x=10,y=60)
        btnDownload.place(relx=1, rely=1, anchor='se')
        btnChooseFile.place(relx=0, rely=1, anchor='sw')
        self.__entryURL.place(relx=0.5, rely=0.3, anchor="center")
        
        # Mise d'une valeur sur l'option menu 
        self.__varGetMode.set(self.__listMode[0])
        
        # Mise en place de objet 
        self.__objetArrera = CArreraDownload()
        self.__jsonSetting = jsonWork("download.json")
    
    def active(self):
        self.__windows.mainloop()
    
    def __download(self):
        folder = self.__jsonSetting.lectureJSON("folder")
        if (folder == ""):
            self.__objetArrera.setDownloadFolder()
        else :
            self.__objetArrera.setDownloadFolderDur(folder)
            
        # Recuperation du mode 
        mode = self.__varGetMode.get()
        
        if (mode == "Video Simple"):
            self.__objetArrera.setMode(1)
        else :
            if (mode == "Juste sons") :
                self.__objetArrera.setMode(2)
            else :
                if (mode == "Juste Video") :
                    self.__objetArrera.setMode(3)
        
        tDownload = th.Thread(target=self.__objetArrera.setURL(self.__entryURL.get()))
        tDownload.start()
        tDownload.join()
        del tDownload
        
        self.__entryURL.delete(0,END)
        
        sortie = self.__objetArrera.download()
        
        if (sortie == True):
            showinfo("Download","Video telecharger")
        else :
            showerror("Download","Erreur de telechargement")
    
    def __setFolder(self):
        folder = filedialog.askdirectory(title="Dossier de telechargement")
        if (folder != "") :
            self.__jsonSetting.EcritureJSON("folder",folder)
            showinfo("Download","Dossier enregistrer")
        else :
            showerror("Download","Aucun dossier selectionner")
    
    def __Apropos(self):
        #Variable
        copyrightApp = "Copyright Arrera Software by Baptiste P 2023-2024"
        color = "white"
        #Creation de la fenetre
        about = Toplevel()
        about.title("A propos : "+self.__nameApp)
        about.maxsize(400,300)
        about.minsize(400,300)
        about.configure(bg=color)
        about.iconphoto(False,PhotoImage(file=self.__imagePath))
        #Traitement Image
        icon = ImageTk.PhotoImage(Image.open(self.__imagePath).resize((100,100)))
        #Label
        labelIcon = Label(about,bg=color)
        labelIcon.image_names = icon
        labelIcon.configure(image=icon)
        labelName = Label(about,text="\n"+self.__nameApp+"\n",font=("arial","12"),bg=color)
        labelVersion = Label(about,text=self.__versionApp+"\n",font=("arial","11"),bg=color)
        labelCopyright = Label(about,text=copyrightApp,font=("arial","9"),bg=color)
        #affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()