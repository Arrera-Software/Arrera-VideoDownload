import yt_dlp
from tkinter import filedialog

class CArreraDownload :
    def __init__(self):
        self.__url = ""
        self.__urlSet = False
        self.__downloadFolderSet = False
        self.__ydlOpts = {}
    
    def setDownloadFolder(self):
        folder = ""
        folder = filedialog.askdirectory(title="Dossier de telechargement")
        if (folder == ""):
            self.__downloadFolderSet = False
            return False
        else :
            self.__downloadFolderSet = True
            self.__ydlOpts = {
                'format': 'best',  # Sélectionne la meilleure qualité disponible
                'outtmpl': folder+"/"+ '%(title)s.%(ext)s',  # Définit le chemin de sortie
                'quiet': True,  # Désactive les messages de la console
                'no_warnings': True,  # Supprime les avertissements
            }   
            return True
    
    def setDownloadFolderDur(self,folder:str):
        if (folder == ""):
            self.__downloadFolderSet = False
            return False
        else :
            self.__downloadFolderSet = True
            self.__ydlOpts = {
                'format': 'best',  # Sélectionne la meilleure qualité disponible
                'outtmpl': folder+"/"+ '%(title)s.%(ext)s',  # Définit le chemin de sortie
                'quiet': True,  # Désactive les messages de la console
                'no_warnings': True,  # Supprime les avertissements
            }   
            return True
    
    def setURL(self,url:str):
        if (url != ""):
            self.__url = url
            self.__urlSet = True
        else :
            self.__urlSet = False
      
    def download(self):
        if ((self.__downloadFolderSet == True) and (self.__urlSet == True)):
            with yt_dlp.YoutubeDL(self.__ydlOpts) as ydl:
                ydl.download([self.__url])
            self.__urlSet = False
            self.__url = ""
            return True
        else :
            return False
        