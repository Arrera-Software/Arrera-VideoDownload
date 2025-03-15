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
        # Initilisation du theard
        self.__tDownload = th.Thread()
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

        # Frame
        #main
        self.__fMain = self.__arreraTk.createFrame(self.__windows,width=450,height=450)
        # Para
        self.__fPara = self.__arreraTk.createFrame(self.__windows,width=450,height=450)
        # Download
        self.__fDownload = self.__arreraTk.createFrame(self.__windows,width=450,height=450)
        # Widget
        # fmain
        labelTitle = self.__arreraTk.createLabel(self.__fMain,text="Arrera Download",
                                                 ppolice="Arial",ptaille=30,
                                                 pstyle="bold")

        self.__entryURL = self.__arreraTk.createEntry(self.__fMain,ppolice="Arial",ptaille=20,width=400)
        btnDownload = self.__arreraTk.createButton(self.__fMain,text="Telecharger",command=self.__downlaodView,
                                                   ppolice="Arial",ptaille=20)
        btnPara = self.__arreraTk.createButton(self.__fMain,text="Parametre",ppolice="Arial",
                                               ptaille=20,command=self.__viewPara)
        modeSelection = self.__arreraTk.createOptionMenu(self.__fMain,
                                                         var = self.__varGetMode,
                                                         value=self.__listMode,
                                                         police="Arial",taille=20)
        # fpara
        labelTitlePara = self.__arreraTk.createLabel(self.__fPara,
                                                     text="Parametre Arrera Download",
                                                     ppolice="Arial",
                                                     ptaille=30,
                                                     pstyle="bold")

        btnChooseFile = self.__arreraTk.createButton(self.__fPara,text ="Emplacement de téléchargement",command=self.__setFolder,
                                                     ppolice="Arial",ptaille=20)

        btnDoc = self.__arreraTk.createButton(self.__fPara,text="Documentation d'Arrera Download",
                                              command= lambda : webbrowser.open(
                                                  "https://github.com/Arrera-Software/Arrera-VideoDownload/blob/main/README.md")
                                              ,ppolice="Arial",ptaille=20)

        btnApropos = self.__arreraTk.createButton(self.__fPara,text="A propos d'Arrera Download"
                                                  ,command= lambda : self.__arreraTk.aproposWindows(
                nameSoft="Arrera Download",version="",
                iconFile="image/ArreraVideoDownload.png",
                copyright="",linkSource="",linkWeb=""),
                                                  ppolice="Arial",ptaille=20)

        btnExitPara = self.__arreraTk.createButton(self.__fPara,text="Retour a l'acceuil",ppolice="Arial",
                                                   ptaille=20,command=self.__backMain)
        # fDownload
        self.__labelDownload = self.__arreraTk.createLabel(self.__fDownload,text="",ppolice="Arial",ptaille=20)
        # Affichage
        self.__arreraTk.placeCenter(self.__fMain)
        # fmain
        self.__arreraTk.placeTopCenter(labelTitle)
        modeSelection.place(x=10,y=60)
        self.__arreraTk.placeLeftBottom(btnPara)
        self.__arreraTk.placeRightBottom(btnDownload)
        self.__arreraTk.placeCenter(self.__entryURL)
        # fpara
        self.__arreraTk.placeTopCenter(labelTitlePara)
        self.__arreraTk.placeCenter(btnDoc)
        self.__arreraTk.placeCenterOnWidth(btnChooseFile,120)
        self.__arreraTk.placeCenterOnWidth(btnApropos,300)

        #fDonwload
        self.__arreraTk.placeCenter(self.__labelDownload)

        self.__arreraTk.placeBottomRight(btnExitPara)
        # Mise d'une valeur sur l'option menu 
        self.__varGetMode.set(self.__listMode[0])
        
        # Mise en place de objet 
        self.__objetArrera = CArreraDownload()
        self.__jsonSetting = jsonWork("download.json")
    
    def active(self):
        self.__windows.mainloop()
    
    def __setFolder(self):
        folder = filedialog.askdirectory(title="Dossier de telechargement")
        if (folder != "") :
            self.__jsonSetting.EcritureJSON("folder",folder)
            showinfo("Download","Dossier enregistrer")
        else :
            showerror("Download","Aucun dossier selectionner")

    def __viewPara(self):
        self.__fMain.place_forget()
        self.__arreraTk.placeCenter(self.__fPara)

    def __backMain(self):
        self.__fPara.place_forget()
        self.__arreraTk.placeCenter(self.__fMain)

    def __downlaodView(self):
        url = self.__entryURL.get()
        self.__entryURL.delete(0,END)
        folder = self.__jsonSetting.lectureJSON("folder")
        if (folder == ""):
            showerror("Download","Aucun dossier de telechargement enregistrer")
            return
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
        if (url == ""):
            showerror("Download","Aucun URL")
            return
        self.__objetArrera.setURL(url)
        self.__tDownload = th.Thread(target=self.__objetArrera.download)

        self.__fMain.place_forget()
        self.__arreraTk.placeCenter(self.__fDownload)
        self.__labelDownload.configure(text="Telechargement en cours...")
        self.__tDownload.start()
        self.__windows.after(500,self.__downloadCheck)

    def __downloadCheck(self):
        if (self.__tDownload.is_alive()):
            text1 = "Telechargement en cours..."
            text2 = "Telechargement en cours......"
            text3 = "Telechargement en cours........."

            textLabel = self.__labelDownload.cget("text")

            if (textLabel == text1):
                self.__labelDownload.configure(text=text2)
            else :
                if (textLabel == text2):
                    self.__labelDownload.configure(text=text3)
                else :
                    self.__labelDownload.configure(text=text1)

            self.__windows.after(500,self.__downloadCheck)
        else :
            showinfo("Download","Telechargement terminer")
            self.__fDownload.place_forget()
            self.__tDownload = th.Thread()
            self.__arreraTk.placeCenter(self.__fMain)
            self.__windows.update()