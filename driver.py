'''
Created on 03-03-2021

@author: Thibaud
'''


#J'importe les packets de pyserial
import serial
import serial.tools.list_ports # import de la biblio pour recup les ports

class driverKNX:
    def __init__(self):
        self.ports = ''
        self.portCOM = ''

        self.getListesPorts() #Permet de lancer au démarrage sans l'appeler
        self.findKnxPort()

    
    def getListesPorts(self):
        self.ports = serial.tools.list_ports.comports() #Permet de stocker dans un liste tout les ports qui sont connéctés
        
    def findKnxPort(self):
        self.portCOM = 'Erreur'
        listePorts = len(self.ports)

        for i in range (0, listePorts):
            port = self.ports [i]
            strPort = str(port) 

            if 'Prolific' in strPort: #Je procéde à une vérification par un mot clés
                splitPort = strPort.split(' ') #Ici je sépare strPort à chaques éspaces
                self.portCOM = (splitPort[0]) #J'assigne à portCOM le premier champs de splitPort qui correspond au COM du port
            else:
                print('Erreur aucun port trouver')    

    def driverCap(self):

        capKNX = serial.Serial(self.portCOM, 9600, timeout= 1) # ici j'ouvre et configure le port série, en lui précisant le port sélectionner, puis le taux de bauds pour le port et je lui défini un timeout

        dataKNX = capKNX.readline() # ici je vais lire les données sur le port jusqu'a un EOL characters

        return dataKNX.decode('utf-8')
   
