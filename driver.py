'''
Created on 03-03-2021

@author: Thibaud
'''

# J'importe les packets de pyserial
import serial
import serial.tools.list_ports  # import de la biblio pour recup les ports

import binascii


class driverKNX:
    def __init__(self):  # Correspond au constructeur
        self.ports = ''  # Défini les variables utilisables dans toutes la classes
        self.portCOM = ''
        self.dataKNX = ''

        self.getListesPorts()  # Permet de lancer au démarrage sans l'appeler
        self.findKnxPort()

    def getListesPorts(self):
        # Permet de stocker dans un liste tout les ports qui sont connéctés
        self.ports = serial.tools.list_ports.comports()

    def findKnxPort(self):
        self.portCOM = 'Erreur'
        listePorts = len(self.ports)

        for i in range(0, listePorts):
            port = self.ports[i]
            strPort = str(port)

            if 'Prolific' or ' USB Serial' in strPort:  # Je procéde à une vérification par un mot clés
                # Ici je sépare strPort à chaques éspaces
                splitPort = strPort.split(' ')
                # J'assigne à portCOM le premier champs de splitPort qui correspond au COM du port
                self.portCOM = (splitPort[0])
            else:
                # Crée un exception qui sera utiliser par la classe log de guillaume
                raise Exception('Erreur aucun port trouver')

    def getKNX(self):

        # ici j'ouvre et configure le port série, en lui précisant le port sélectionner, puis le taux de bauds pour le port et je lui défini un timeout
        capKNX = serial.Serial(self.portCOM, baudrate=9600, timeout=1,
                               bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_TWO)

        capKNX.flushInput()  # Clear du buffer Input
        capKNX.flushOutput()  # Clear du buffer Output

        # ici je vais lire les données sur le port et les mettres en hexa en séparant par -
        self.dataKNX = binascii.hexlify(capKNX.readline())

        return self.dataKNX.decode('utf-8')

    def getComPort(self):

        return self.portCOM
