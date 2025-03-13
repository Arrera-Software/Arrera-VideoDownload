import yt_dlp
from tkinter import filedialog

class CArreraDownload:
    def __init__(self):
        self.__url = ""
        self.__urlSet = False
        self.__downloadFolderSet = False
        self.__ydlOpts = {}
        self.__mode = 1

    def setMode(self, m: int):
        """
        1 -> Vidéo complète
        2 -> Juste audio
        3 -> Juste vidéo
        """
        self.__mode = m

    def setDownloadFolder(self):
        folder = ""
        folder = filedialog.askdirectory(title="Dossier de téléchargement")
        if folder == "":
            self.__downloadFolderSet = False
            return False
        else:
            self.__downloadFolderSet = True
            self.updateYdlOpts(folder)
            return True

    def setDownloadFolderDur(self, folder: str):
        if folder == "":
            self.__downloadFolderSet = False
            return False
        else:
            self.__downloadFolderSet = True
            self.updateYdlOpts(folder)
            return True

    def updateYdlOpts(self, folder: str):
        self.__ydlOpts = {
            'format': '',  # Sélectionne la meilleure qualité disponible
            'outtmpl': folder + "/" + '%(title)s.%(ext)s',  # Définit le chemin de sortie
            'quiet': True,  # Désactive les messages de la console
            'no_warnings': True,  # Supprime les avertissements
            'noplaylist': False,  # Permet de traiter les playlists
        }

    def setURL(self, url: str):
        if url != "":
            self.__url = url
            self.__urlSet = True
        else:
            self.__urlSet = False

    def download(self):
        if ((self.__downloadFolderSet == True) and (self.__urlSet == True)):
            match self.__mode:
                case 1:
                    self.__ydlOpts['format'] = "best"
                case 2:
                    self.__ydlOpts['format'] = "bestaudio"
                case 3:
                    self.__ydlOpts['format'] = "bestvideo"

            try:
                with yt_dlp.YoutubeDL(self.__ydlOpts) as ydl:
                    ydl.download([self.__url])
                self.__urlSet = False
                self.__url = ""
                return True
            except Exception as e:
                print("Erreur lors du téléchargement :", e)
                return False
        else:
            print("Le dossier ou l'URL n'a pas été configuré correctement.")
            return False
