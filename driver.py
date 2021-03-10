'''
Created on 03-03-2021

@author: Thibaud
'''

#J'importe les packets de pyserial
import serial
import serial.tools.list_ports # import de la biblio pour recup les ports

import binascii

class driverKNX:
    def __init__(self): # Correspond au constructeur
        self.ports = '' #Défini les variables utilisables dans toutes la classes
        self.portCOM = ''
        self.dataKNX = ''

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

            if 'Prolific' or ' USB Serial' in strPort: #Je procéde à une vérification par un mot clés
                splitPort = strPort.split(' ') #Ici je sépare strPort à chaques éspaces
                self.portCOM = (splitPort[0]) #J'assigne à portCOM le premier champs de splitPort qui correspond au COM du port
            else:
                raise Exception('Erreur aucun port trouver')  #Crée un exception qui sera utiliser par la classe log de guillaume

    def getKNX(self):
        
        capKNX = serial.Serial(self.portCOM, baudrate=9600, timeout= 1, bytesize= serial.EIGHTBITS, stopbits=serial.STOPBITS_TWO) # ici j'ouvre et configure le port série, en lui précisant le port sélectionner, puis le taux de bauds pour le port et je lui défini un timeout

        capKNX.flushInput()   #Clear du buffer Input
        capKNX.flushOutput()  #Clear du buffer Output

        self.dataKNX = binascii.hexlify(capKNX.readline(),'-')# ici je vais lire les données sur le port et les mettres en hexa en séparant par -
        
        return self.dataKNX

    def getComPort(self):

        return self.portCOM

    def telegKNX(self):
        splitDataKNX, splitKNXReturn,telegKNX = [], [], []

        splitDataKNX = self.dataKNX.split('-') #Ici je sépare dataKNX à chaques -     

        for i in range(len(splitDataKNX)):                                                                      #
            splitKNXReturn += splitDataKNX[i] #Ajout de splitDataKNX[i] dans splitKNXReturn[i]                  #                                                                                            # Cette partie permet de ne récupérer que un Télègrame KNX
            if splitDataKNX[i] == '0c' or splitDataKNX[i] == 'c0' or splitDataKNX[i] == 'cc':                   # Je vérifie tout les caractères de fin d'un télégrammes KNX                 
                telegKNX = ''.join(map(str,splitKNXReturn))                                                     #transformation du tableau en chaine de str                                                                                               #
                break                                                                                           #
                       
        return telegKNX