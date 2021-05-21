# Kwin

from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk 
from webbrowser import *
import webbrowser
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
        
        cblog = IntVar()
        #menuOption.add_checkbutton(label = "Afficher les logs", variable = cblog, command = self.log)
        menuOption.add_command(label = "Afficher les logs", command = self.log)


        cbsombre = IntVar()
        menuOption.add_checkbutton(label = "Mode sombre", variable = cbsombre, command = self.darkmode)
        menuOption.add_command(label = "Quitter", command = self.exitProgram)
        menu.add_cascade(label = "Options", menu = menuOption)

        menuAPropos = Menu(menu) 
        menuAPropos.add_command(label="Voir de l'aide", command = self.aide)
        menuAPropos.add_command(label="Voir notre Github", command = self.github)
        menu.add_cascade(label="À Propos", menu=menuAPropos)

        #Création de la Combobox

        self._initUI()

    def exitProgram(self):
        exit()

    def affich(self):
        lab = Label(fenlog, text = "LOGS")
        lab.pack()

    def log(self) :
        print("Afficher les logs")
        global fenlog 
        fenlog = Toplevel(self)
        self.pack(fill = BOTH)

        text = Label(fenlog, text = "Voici la fenêtre où seront affichés les logs")
        text.pack()

        button = Button(fenlog, text = "Afficher les logs", command = self.affich)
        button.pack()

        
        #cblog.set(0)

        #if cblog.get() == 1 : 
            #fenlog = Toplevel(self)
            #self.pack(fill = BOTH)

            #text = Label(fenlog, text = "Voici la fenêtre où seront affichés les logs")
            #text.pack()

    def descriptif(self): 
        canv = Canvas(fenaide, width = 200, height = 200, background = "white")
        canv.create_text()

    def equipe(self):
        canv = Canvas(fenaide, width = 200, height = 200, background = "white")
        canv.create_text()

    def aide(self): 

        global fenaide
        fenaide = Toplevel(self)
        self.pack(fill = BOTH)
        fenaide.title("Aide")
        text = Label(fenaide, text = "Bienvenue sur l'aide de notre analyseur de trames KNX")
        text.pack()

        But1 = Button(fenaide, text = "Voir notre Github", command = self.github)
        But1.pack()

        vide = Label(fenaide, text = " ")
        vide.pack()

        But2 = Button(fenaide, text = "Voir le descriptif", command = self.descriptif)
        But2.pack()

        vide = Label(fenaide, text = " ")
        vide.pack()

        But3 = Button(fenaide, text = "En savoir plus sur l'équipe", command = self.equipe)
        But3.pack()

        vide = Label(fenaide, text = " ")
        vide.pack()

        
    def darkmode(self) :
        print("Afficher le mode sombre")
        self.configure(bg = 'black')
        #self.vide.config(bg = 'black')


#Création de la fonction qui permettra à l'utilisateur d'aller regarder le Github 

    def github(self) :
        #print("Afficher notre GitHub")

        #fengit = Toplevel(self)
        #self.pack(fill = BOTH)

        #text = Label(fengit, text = "Voici le lien de notre Github", font =("Impact", 12))
        #text.pack()

        #global git_img
        #git_img = Image.open("github_PNG19.png")
        #git_img = git_img.resize((150,150))
        #git_img = ImageTk.PhotoImage(git_img)
        
        #git_logo = Label(fengit, image = git_img)
        #git_logo.pack()

        #Création d'un lien hypertexte 

        #lien = Label(fengit, text = r"https://github.com/GuillaumeDorschner/KNX-Communication-Analyzer", fg = "blue", cursor = "arrow")
        #lien.pack()
        link = webbrowser.open('https://github.com/GuillaumeDorschner/KNX-Communication-Analyzer')

        
        

#Fonction pour les widgets de la première fenêtre 
    def _initUI(self):

        self.pack(fill = BOTH)

        global vide
        vide = Label(self, text = " ")
        vide.pack()


        select_port = ttk.Combobox(self, values = ["Veuillez choisir un port", "Port COM"])
        select_port.pack()

        vide = Label(self, text = " ")
        vide.pack()

        #global can
        #can = Canvas(self, width = 400, height = 400, background = "white")
        #can.pack()

        global listrame 
        listrame = Listbox(self, width = 105, height = 20)
        listrame.pack()

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


    def writeinfo(self, listrame): 

        #feninfo = Toplevel(self)
        #self.pack(fill = BOTH)
        listinfo = Listbox(self, width = 40, height = 20)
        #listinfo.pack(side = TOP, anchor = NW)
        listinfo.pack(side = LEFT)
       

    def startAnalyse(self):
        print("Lancer l'analyseur de trames")
        #can.create_text(200, 20, text = TrameKNX(trame1))
    
        listrame.insert("end", trame1)

        listrame.bind("<Double-1>", self.writeinfo)
        
       

    def stopAnalyse(self, listrame):
        print("Stopper l'analyseur de trames")

        listrame.clear()
        

        
def main():
  
    f1 = Tk()
    f1.resizable(width = 1000, height = 1000)
    app = Fenetre_principale(f1)
    f1.mainloop()  

if __name__ == '__main__':
    main()