# Kwin

from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk 
from webbrowser import *
from affitrame import *

#Fenêtre principale 
class Fenetre_principale(Frame) :

    def __init__(self, parent): 
        Frame.__init__(self, parent)

        self.parent = parent 
        
        self.parent.title("Analyseur de trames KNX")

        self.pack(fill = BOTH)

        #Création du menu de la fenêtre

        menu = Menu(self.parent)
        self.parent.config(menu=menu)

        menuOption = Menu(menu)
        menuOption.add_checkbutton(label = "Afficher les logs", command = self.log)
        menuOption.add_checkbutton(label = "Mode sombre", command = self.darkmode)
        menuOption.add_command(label = "Quitter", command = self.exitProgram)
        menu.add_cascade(label = "Options", menu = menuOption)

        menuAPropos = Menu(menu)
        menuAPropos.add_command(label="Voir de l'aide")
        menuAPropos.add_command(label="Afficher notre Github", command = self.github)
        menu.add_cascade(label="À Propos", menu=menuAPropos)

        #Création de la Combobox

        self._initUI()

    def exitProgram(self):
        exit()

    def log(self) :
        print("Afficher les logs")

    def darkmode(self) :
        print("Afficher le mode sombre")




#Création de la fonction qui permettra à l'utilisateur d'aller regarder le Github 

    def github(self) :
        print("Afficher notre GitHub")

        fengit = Toplevel(self)
        self.pack(fill = BOTH)

        text = Label(fengit, text = "Voici le lien de notre Github", font =("Impact", 12))
        text.pack()

        global git_img
        git_img = Image.open("github_PNG19.png")
        git_img = git_img.resize((150,150))
        git_img = ImageTk.PhotoImage(git_img)
        
        git_logo = Label(fengit, image = git_img)
        git_logo.pack()

        #Création d'un lien hypertexte 

        lien = Label(fengit, text = r"https://github.com/GuillaumeDorschner/KNX-Communication-Analyzer", fg = "blue", cursor = "arrow")
        lien.pack()




        

        
        

#Fonction pour les widgets de la première fenêtre 
    def _initUI(self):

        self.pack(fill = BOTH)

        vide = Label(self, text = " ")
        vide.pack()


        select_port = ttk.Combobox(self, values = ["Veuillez choisir un port", "Port COM"])
        select_port.pack()

        vide = Label(self, text = " ")
        vide.pack()


        can = Canvas(self, width = 400, height = 400, background = "white")
        #can.pack(side = LEFT)
        can.pack()

        global start_img
        start_img = Image.open("Start_logo.png")
        start_img = start_img.resize((50,50))
        #start_img = start_img.resize((25,25), Image.ANTIALIAS)
        start_img = ImageTk.PhotoImage(start_img)


        
        global pause_img
        pause_img = Image.open("pause-button-clipart-4.jpg")
        pause_img = pause_img.resize((50,50))
        #pause_img = pause_img.resize((25,25), Image.ANTIALIAS)
        pause_img = ImageTk.PhotoImage(pause_img)
        

        boutonStart = Button(self, text = "Démarrer", image = start_img, relief = "flat", command = self.startAnalyse)
        #boutonStart.pack(side = BOTTOM)
        boutonStart.pack(side = LEFT)

        boutonPause = Button(self, text = "Pause", image = pause_img, relief = "flat", command = self.stopAnalyse)
        #boutonPause.pack()
        boutonPause.pack(side = RIGHT)

    def startAnalyse(self):
        print("Lancer l'analyseur de trames")

    def stopAnalyse(self):
        print("Stopper l'analyseur de trames")


   

      

def main():
  
    f1 = Tk()
    f1.resizable(width = 1000, height = 1000)
    app = Fenetre_principale(f1)
    f1.mainloop()  

if __name__ == '__main__':
    main()