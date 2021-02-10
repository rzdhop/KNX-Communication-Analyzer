# Guillaume
import os
import datetime
from tkinter import messagebox


class logs:

    def __init__(self, path: str = None):
        """
        Initialisation du path repo des logs
        Si il n'y a pas de chemin initialisé prends un chemin relatif
        """

        if path == None:
            path = str(os.path.dirname(__file__))

        path = path + "/logs"

        self.path = path

        # try:
        os.mkdir(path)
        # except OSError:
        # messagebox.showerror(title="Err", message="Creation Failed")
        # else:
        #     print("Creation Successfully")

    def err(self, err: str = None):
        """
        Méthode permettant de log l'erreur
        """
        print(err)

        try:
            file = open(self.path + "/Err.txt", 'a')

            date = datetime.datetime.now()

            if err == None:
                err = "Erreur Inconnu"

            messagebox.showerror(title="Err", message=err)

            file.write("--------- {0} {1} {2} {3} {4} ---------\n{5}\n\n\n".format(date.strftime(
                "%Y"), date.strftime("%A"), date.strftime("%d"), date.strftime("%B"), date.strftime("%X"), err))

            file.close()

        except IOError:
            messagebox.showerror(title="Err", message="Can't log Err")

    def info(self, info: str):
        """
        Méthode permettant de log l'info
        """

        print(info)

        try:
            file = open(self.path + "/Info.txt", 'a')

            date = datetime.datetime.now()

            file.write("--------- {0} {1} {2} {3} {4} ---------\n{5}\n\n\n".format(date.strftime(
                "%Y"), date.strftime("%A"), date.strftime("%d"), date.strftime("%B"), date.strftime("%X"), info))

            file.close()

        except IOError:
            messagebox.showerror(title="Err", message="Can't log Info")
