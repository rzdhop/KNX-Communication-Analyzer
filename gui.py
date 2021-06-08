#Kwin

import threading
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk 
import webbrowser

#from serial.tools.list_ports_windows import NULL
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

        self.sauvInfo = []


        self._initUI()

        global th1 
        th1 = threading.Thread(target = self.process_capture)

        self.th_infos = threading.Thread(target = self.historique)

        self.selection = 0
        
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
        start_img = Image.open("./Img/Start_logo.png")
        start_img = start_img.resize((50,50))
        start_img = ImageTk.PhotoImage(start_img)


        
        global pause_img
        #pause_img = Image.open("pause-button-clipart-4.jpg")
        pause_img = Image.open("./Img/Pause_logo_2.png")
        pause_img = pause_img.resize((50,50))
        pause_img = ImageTk.PhotoImage(pause_img)


        global writeinfo_img
        writeinfo_img = Image.open("./Img/ecriture-log.png")
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

        #self.boutonWriteInfo = Button(Frameboutons, text = "Write Info", image = writeinfo_img, relief = "flat", command = self.test.writeInfo)
        self.boutonWriteInfo = Button(Frameboutons, text = "Write Info", image = writeinfo_img, relief = "flat")
        self.boutonWriteInfo.pack_forget()       
       

    #Montre les infos de la trame

        

    def process_capture(self) :
        
        listrame.configure(font=(16))
        self.tab = []

        knxBck = 0

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
                    listrame.bind("<Double-1>", self.showInfo)
                    

        
                    print(self.tab[i].trameBruteKNX)

            listrame.bind("<<ListboxSelect>>", self.historique)
                     

            
    def historique(self, event) :
    #def historique(self, event, listrame) : 

        self.selection = listrame.curselection()
        self.selection = self.selection[0]
        print(self.selection)
    


        

        

    def showInfo(self, listrame): 


        #listrame.bind("<Double-1>", self.showInfo())

        listinfo.pack(side = RIGHT, padx = 20)

    
        #th1.join()

        listinfo.delete(0,"end")

        octetControle = "Octet de Contrôle :  " + str(self.tab[self.selection].octetControle)
        listinfo.insert("end", octetControle)

        typePriorite = "Type de priorité : " +  str(self.tab[self.selection].typePriority)
        listinfo.insert("end", typePriorite)

        typeEmission = "Type d'émission : " + str(self.tab[self.selection].typeEmision)
        listinfo.insert("end", typeEmission)

        typeFrame = "Type de trame : " + str(self.tab[self.selection].typeFrame)
        listinfo.insert("end", typeFrame)

        adresseDestinataire = "Adresse destinataire : " + str(self.tab[self.selection].adresseDestinataire)
        listinfo.insert("end", adresseDestinataire)

        adresseSource = "Adresse source : " + str(self.tab[self.selection].adresseSoucre)
        listinfo.insert("end", adresseSource)
        
        typeCast = "Type de Cast : " + str(self.tab[self.selection].typeCast)
        listinfo.insert("end", typeCast)

        lCRLG = "CRLG : " + str(self.tab[self.selection].CRLG)
        listinfo.insert("end", lCRLG)

        lCR = "CR : " + str(self.tab[self.selection].CR)
        listinfo.insert("end", lCR)

        lLG = "LG : " + str(self.tab[self.selection].LG)
        listinfo.insert("end", lLG)

        Data = "Data : " + str(self.tab[self.selection].Data)
        listinfo.insert("end", Data)

        Securite = "Sécurité : " + str(self.tab[self.selection].securite)
        listinfo.insert("end", Securite)

        Checksum = "Checksum : " + str(self.tab[self.selection].Checksum)
        listinfo.insert("end", Checksum)

        #th1.start()



        self.boutonWriteInfo.bind("<Button-1>", self.test.writeInfo())
        self.boutonWriteInfo.pack(side= RIGHT, padx= 30)

        

        self.sauvInfo.append(octetControle, "\n" + typePriorite, "\n" + typeEmission, "\n" + typeFrame, "\n")

        """i = 0
        for i in range(len(self.sauvInfo)) : 

            self.sauvInfo[0] = octetControle
            self.sauvInfo[1] = typePriorite
            self.sauvInfo[2] = typeEmission
            self.sauvInfo[3] = typeFrame
            self.sauvInfo[4] = adresseDestinataire
            self.sauvInfo[5] = adresseSource
            self.sauvInfo[6] = typeCast
            self.sauvInfo[7] = lCRLG
            self.sauvInfo[8] = lCR
            self.sauvInfo[9] = lLG
            self.sauvInfo[10] = Data 
            self.sauvInfo[11] = Securite
            self.sauvInfo[12] = Checksum"""
 


    def startAnalyse(self):
        
        th1.start()
        listrame.bind("<Double-1>", self.showInfo)
        #listrame.bind("<Double-1>", self.historique)
        

    def stopAnalyse(self):
        
        th1.join(5)


        
def main():
  
    f1 = Tk()
    f1.resizable(width = 1000, height = 1000)
    app = Fenetre_principale(f1)
    f1.mainloop()  

if __name__ == '__main__':
    main()

