'''
Created on 23-02-2021

@author: Thibaud
'''


#J'importe les packets de pyserial
import serial
from serial import Serial


def getListesPorts():
    ports = serial.tools.list_ports.comports() #Permet de stocker dans un liste tout les ports qui sont connéctés
    
    return ports

def findKnxPort(ports):
    portCOM = 'Erreur aucun port correspondant'
    listePorts = len(ports)

    for i in range (0, listePorts):
        port = ports [i]
        strPort = str(port) 

        if 'nom du périphe' in strPort: #Je procéde à une vérification par un mot clés
            splitPort = strPort.split(' ') #Ici je sépare strPort à chaques éspaces
            portCOM = (splitPort[0]) #J'assigne à portCOM le premier champs de splitPort qui correspond au COM du port

    return portCOM


def driverCap(userPort):
    capKNX = serial.Serial(userPort, 9600, timeout= 1) # ici j'ouvre et configure le port série, en lui précisant le port sélectionner, puis le taux de bauds pour le port et je lui défini un timeout
    dataKNX = capKNX.readline() # ici je vais lire les données sur le port jusqu'a un EOL characters
   
    return dataKNX