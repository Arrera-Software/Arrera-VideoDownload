from librairy.arrera_tk import *
from librairy.dectectionOS import*
from ArreraDownload import*
from tkinter.messagebox import*
from librairy.travailJSON import*
import threading as th
import webbrowser

class CArreraDGUI :
    def __init__(self) :
        # Initilisation d'Arrera Tk
        self.__arreraTk = CArreraTK()
        # Initilisation de l'objet OS
        dectOs = OS()
        # Mise en place de l'icon
        if (dectOs.osWindows() == True):
            icon = "image/ArreraVideoDownload.ico"
        else :
            icon = "image/ArreraVideoDownload.png"
        # Fenetre
        self.__windows = self.__arreraTk.aTK(title="Arrera Download",
                                             width=500,height=500,
                                             resizable=False,icon=icon)

        # Var
        self.__listMode = ["Video Simple","Juste sons","Juste Video"]
        self.__varGetMode = StringVar(self.__windows)

        # Menu
        menu = Menu(self.__windows)
        menu.add_command(label = "A Propos",command=lambda :
        self.__arreraTk.aproposWindows(nameSoft="Arrera Download",
                                       version="",
                                       iconFile="image/ArreraVideoDownload.png",
                                       copyright="",
                                       linkSource="",
                                       linkWeb=""))
        menu.add_command(label="Documentation",command= lambda : webbrowser.open("https://github.com/Arrera-Software/Arrera-VideoDownload/blob/main/README.md"))
        self.__windows.configure(menu=menu)
        
        # Widget
        labelTitle = self.__arreraTk.createLabel(self.__windows,text="Arrera Download",
                                                 ppolice="Arial",ptaille=30,
                                                 pstyle="bold")

        self.__entryURL = self.__arreraTk.createEntry(self.__windows,ppolice="Arial",ptaille=30,width=400)
        btnDownload = self.__arreraTk.createButton(self.__windows,text="Telecharger",command=self.__download,
                                                   ppolice="Arial",ptaille=25)
        btnChooseFile = self.__arreraTk.createButton(self.__windows,text ="Dossier Sortie",command=self.__setFolder,
                                                     ppolice="Arial",ptaille=25)
        modeSelection = self.__arreraTk.createOptionMenu(self.__windows,
                                                         var = self.__varGetMode,
                                                         value=self.__listMode,
                                                         police="Arial",taille=20)
        # Affichage
        labelTitle.pack()
        modeSelection.place(x=10,y=60)
        btnDownload.place(relx=1, rely=1, anchor='se')
        btnChooseFile.place(relx=0, rely=1, anchor='sw')
        self.__arreraTk.placeCenter(self.__entryURL)
        
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