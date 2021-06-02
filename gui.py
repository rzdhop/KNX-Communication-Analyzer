# Kwin

# Kwin

import threading
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk 
import webbrowser

from serial.tools.list_ports_windows import NULL
from classes import CTrameKNX
from driver import driverKNX 
from threading import *

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
        menuOption.add_command(label = "Quitter", command = self.exitProgram)
        menu.add_cascade(label = "Options", menu = menuOption)

        menuAPropos = Menu(menu) 
        menuAPropos.add_command(label="Voir notre Github", command = self.github)
        menu.add_cascade(label="À Propos", menu=menuAPropos)

        self.state = False

        self.driver = driverKNX()
        

        self.tab = []

        self.histo = []


        self._initUI()

        global th1 
        th1 = threading.Thread(target = self.process_capture)
        
        listrame.bind("<Double-1>", self.showInfo)   

    def exitProgram(self):
        exit()


    



#Création de la fonction qui permettra à l'utilisateur d'aller regarder le Github 

    def github(self) :
        
        link = webbrowser.open('https://github.com/GuillaumeDorschner/KNX-Communication-Analyzer')

        
        

#Fonction pour les widgets de la fenêtre principale de l'analyseur de trames
    def _initUI(self):

        self.pack(fill = BOTH)

        global vide
        vide = Label(self, text = " ")
        vide.pack()


        valeur_port = self.driver.getComPort()

        #select_port = ttk.Combobox(self, values = ["Veuillez choisir un port", "Port COM"])
        select_port = ttk.Combobox(self, state = "readonly")
        select_port['values']=(str(valeur_port),'Aucun autre port détecté')
        select_port.current(0)
        select_port.pack()

        

        select_port.pack()

        vide = Label(self, text = " ")
        vide.pack()

        #Frame pour afficher les deux listbox (affichage de trames)
        global FrameWidgets
        FrameWidgets = Frame(self)
        FrameWidgets.pack()


        #Frame pour contenir les boutons Start, Pause et WriteInfo
        global Frameboutons
        Frameboutons = Frame(self)
        Frameboutons.pack(pady = 10)
        
       

        global start_img
        start_img = Image.open("Start_logo.png")
        start_img = start_img.resize((50,50))
        start_img = ImageTk.PhotoImage(start_img)


        
        global pause_img
        #pause_img = Image.open("pause-button-clipart-4.jpg")
        pause_img = Image.open("Pause_logo_2.png")
        pause_img = pause_img.resize((50,50))
        pause_img = ImageTk.PhotoImage(pause_img)


        global writeinfo_img
        writeinfo_img = Image.open("ecriture-log.png")
        writeinfo_img = writeinfo_img.resize((50,50))
        writeinfo_img = ImageTk.PhotoImage(writeinfo_img)

        global listrame 
        listrame = Listbox(FrameWidgets, width = 105)
        listrame.pack(side = LEFT, padx = 20)

        global listinfo
        listinfo = Listbox(FrameWidgets, width = 40, height= 15)

        listinfo.configure(font=("Courier", 16, "italic"))
        #listinfo.pack(side = RIGHT, padx = 20)
        

        boutonStart = Button(Frameboutons, text = "Démarrer", image = start_img, relief = "flat", command = self.startAnalyse)
        boutonStart.pack(side = LEFT, padx = 20)
        

       
        boutonPause = Button(Frameboutons, text = "Pause", image = pause_img, relief = "flat", command = self.stopAnalyse)
        boutonPause.pack(side = RIGHT, padx = 20)

        self.boutonWriteInfo = Button(Frameboutons, text = "Write Info", image = writeinfo_img, relief = "flat")
        self.boutonWriteInfo.pack_forget()       
       

    #Montre les infos de la trame

        

    def process_capture(self) :
        
        listrame.configure(font=(16))
        self.tab = []

        knxBck = NULL

        #knxBck.flushInput()

        while True:  # Sa boucle la capture à l'infini

            knxBck = self.driver.getKNX()


            if len(knxBck) != 0:  # Ça vérifie si jamais knxBack n'est pas vide et on quitte la boucle

                self.test = CTrameKNX(knxBck)

                print(knxBck)
                self.histo.append(knxBck)
                del knxBck

                print(self.test.adresseDestinataire)
                self.tab.append(self.test)

                
                for i in range(len(self.tab)):
                    listrame.delete(0,1)
                    
                print(self.tab)

                for i in range(len(self.tab)):

                
                    listrame.insert("end", self.tab[i].trameBruteKNX)
                    #listrame.bind("<Double-1>", self.showInfo)
                    

        
                    print(self.tab[i].trameBruteKNX)

            

    def historique(self, listrame) : 

        selection = listrame.curselection
        print(selection)
 
        """for i in range(len(self.histo)) : 

            if i == selection : 

                #listrame.insert("end", self.histo[i])
                listrame.bind("<Double-1>", self.showInfo)"""



        

        

    def showInfo(self, listrame): 
        #listinfo = Listbox(FrameWidgets, width = 40, height= 15)
        #listinfo.configure(font=("Courier", 16, "italic"))

        #self.listrame.bind("<Double-1>", self.showInfo)

        listinfo.pack(side = RIGHT, padx = 20)

    
        #th1.join()

        listinfo.delete(0,"end")

        octetControle = "Octet de Contrôle :  " + str(self.test.octetControle)
        listinfo.insert("end", octetControle)

        typePriorite = "Type de priorité : " +  str(self.test.typePriority)
        listinfo.insert("end", typePriorite)

        typeEmission = "Type d'émission : " + str(self.test.typeEmision)
        listinfo.insert("end", typeEmission)

        typeFrame = "Type de trame : " + str(self.test.typeFrame)
        listinfo.insert("end", typeFrame)

        adresseDestinataire = "Adresse destinataire : " + str(self.test.adresseDestinataire)
        listinfo.insert("end", adresseDestinataire)

        adresseSource = "Adresse source : " + str(self.test.adresseSoucre)
        listinfo.insert("end", adresseSource)
        
        typeCast = "Type de Cast : " + str(self.test.typeCast)
        listinfo.insert("end", typeCast)

        lCRLG = "CRLG : " + str(self.test.CRLG)
        listinfo.insert("end", lCRLG)

        lCR = "CR : " + str(self.test.CR)
        listinfo.insert("end", lCR)

        lLG = "LG : " + str(self.test.LG)
        listinfo.insert("end", lLG)

        Data = "Data : " + str(self.test.Data)
        listinfo.insert("end", Data)

        Securite = "Sécurité : " + str(self.test.securite)
        listinfo.insert("end", Securite)

        Checksum = "Checksum : " + str(self.test.Checksum)
        listinfo.insert("end", Checksum)

        #th1.start()


        #self.boutonWriteInfo.bind(self.test.writeInfo)

        self.boutonWriteInfo.bind("<Button-1>", self.test.writeInfo)
        self.boutonWriteInfo.pack(side= RIGHT, padx= 30)
        
    def startAnalyse(self):
        
        th1.start()
        #listrame.bind("<Double-1>", self.showInfo)
        listrame.bind("<Double-1>", self.historique)
        

    def stopAnalyse(self):
        
        th1.join(5)


        
def main():
  
    f1 = Tk()
    f1.resizable(width = 1000, height = 1000)
    app = Fenetre_principale(f1)
    f1.mainloop()  

if __name__ == '__main__':
    main()



















"""import threading
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk 
import webbrowser

from serial.tools.list_ports_windows import NULL
from classes import CTrameKNX
from driver import driverKNX 
from threading import *

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
        menuOption.add_command(label = "Afficher les logs", command = self.log)
        menuOption.add_command(label = "Quitter", command = self.exitProgram)
        menu.add_cascade(label = "Options", menu = menuOption)

        menuAPropos = Menu(menu) 
        menuAPropos.add_command(label="Voir notre Github", command = self.github)
        menu.add_cascade(label="À Propos", menu=menuAPropos)

        self.state = False

        self.driver = driverKNX()

        self.tab = []


        self._initUI()

        global th1 
        th1 = threading.Thread(target = self.process_capture)
        
        listrame.bind("<Double-1>", self.showInfo)   

    def exitProgram(self):
        exit()


    #Création de la fonction qui servira d'afficher les fichiers log
    def log(self) :
        print("Afficher les logs")
        global fenlog 
        fenlog = Toplevel(self)
        self.pack(fill = BOTH)

        text = Label(fenlog, text = "Voici la fenêtre où seront affichés les logs")
        text.pack()

    



#Création de la fonction qui permettra à l'utilisateur d'aller regarder le Github 

    def github(self) :
        
        link = webbrowser.open('https://github.com/GuillaumeDorschner/KNX-Communication-Analyzer')

        
        

#Fonction pour les widgets de la fenêtre principale de l'analyseur de trames
    def _initUI(self):

        self.pack(fill = BOTH)

        global vide
        vide = Label(self, text = " ")
        vide.pack()


        valeur_port = self.driver.getComPort()
        select_port = ttk.Combobox(self, state = "readonly", values = valeur_port)
        select_port.pack()

        

        select_port.pack()

        vide = Label(self, text = " ")
        vide.pack()

        #Frame pour afficher les deux listbox (affichage de trames)
        global FrameWidgets
        FrameWidgets = Frame(self)
        FrameWidgets.pack()


        #Frame pour contenir les boutons Start, Pause et WriteInfo
        global Frameboutons
        Frameboutons = Frame(self)
        Frameboutons.pack(pady = 10)
        
       

        global start_img
        start_img = Image.open("Start_logo.png")
        start_img = start_img.resize((50,50))
        start_img = ImageTk.PhotoImage(start_img)


        
        global pause_img
        pause_img = Image.open("Pause_logo_2.png")
        pause_img = pause_img.resize((50,50))
        pause_img = ImageTk.PhotoImage(pause_img)


        global writeinfo_img
        writeinfo_img = Image.open("ecriture-log.png")
        writeinfo_img = writeinfo_img.resize((50,50))
        writeinfo_img = ImageTk.PhotoImage(writeinfo_img)

        global listrame 
        listrame = Listbox(FrameWidgets, width = 105)
        listrame.pack(side = LEFT, padx = 20)

        global listinfo
        listinfo = Listbox(FrameWidgets, width = 40, height= 15)
        listinfo.configure(font=("Courier", 16, "italic"))

        

        boutonStart = Button(Frameboutons, text = "Démarrer", image = start_img, relief = "flat", command = self.startAnalyse)
        boutonStart.pack(side = LEFT, padx = 20)
        

       
        boutonPause = Button(Frameboutons, text = "Pause", image = pause_img, relief = "flat", command = self.stopAnalyse)
        boutonPause.pack(side = RIGHT, padx = 20)

        #boutonWriteInfo = Button(Frameboutons, text = "Write Info", image = writeinfo_img, relief = "flat")
        #boutonWriteInfo.pack(side= RIGHT, padx= 30)
       

    #Montre les infos de la trame
    def showInfo(self, listrame): 

                  
        listinfo.pack(side = RIGHT, padx = 20)
        listinfo.delete(0,"end")

        octetControle = "Octet de Contrôle :  " + str(self.test.octetControle)
        listinfo.insert("end", octetControle)

        typePriorite = "Type de priorité : " +  str(self.test.typePriority)
        listinfo.insert("end", typePriorite)

        typeEmission = "Type d'émission : " + str(self.test.typeEmision)
        listinfo.insert("end", typeEmission)

        typeFrame = "Type de trame : " + str(self.test.typeFrame)
        listinfo.insert("end", typeFrame)

        adresseDestinataire = "Adresse destinataire : " + str(self.test.adresseDestinataire)
        listinfo.insert("end", adresseDestinataire)

        adresseSource = "Adresse source : " + str(self.test.adresseSoucre)
        listinfo.insert("end", adresseSource)
        
        typeCast = "Type de Cast : " + str(self.test.typeCast)
        listinfo.insert("end", typeCast)

        lCRLG = "CRLG : " + str(self.test.CRLG)
        listinfo.insert("end", lCRLG)

        lCR = "CR : " + str(self.test.CR)
        listinfo.insert("end", lCR)

        lLG = "LG : " + str(self.test.LG)
        listinfo.insert("end", lLG)

        Data = "Data : " + str(self.test.Data)
        listinfo.insert("end", Data)

        Securite = "Sécurité : " + str(self.test.securite)
        listinfo.insert("end", Securite)

        Checksum = "Checksum : " + str(self.test.Checksum)
        listinfo.insert("end", Checksum)
        

    def process_capture(self) :
        
        listrame.configure(font=(16))
        self.tab = []

        knxBck = NULL


        while True:  # Sa boucle la capture à l'infini

            knxBck = self.driver.getKNX()


            if len(knxBck) != 0:  # Ça vérifie si jamais knxBack n'est pas vide et on quitte la boucle

                self.test = CTrameKNX(knxBck)

                print(knxBck)
                del knxBck

                print(self.test.adresseDestinataire)
                self.tab.append(self.test)


                
                for i in range(len(self.tab)):
                    listrame.delete(0,1)
                    
                print(self.tab)

                for i in range(len(self.tab)):
                    listrame.insert("end", self.tab[i].trameBruteKNX)
                    
                    

        
                    print(self.tab[i].trameBruteKNX)

            listrame.bind("<Double-1>", self.showInfo)


    def startAnalyse(self):
        
        th1.start()
        

    def stopAnalyse(self):
        
        th1.join(5)

        
def main():
  
    f1 = Tk()
    f1.resizable(width = 1000, height = 1000)
    app = Fenetre_principale(f1)
    f1.mainloop()  

if __name__ == '__main__':
    main()"""

