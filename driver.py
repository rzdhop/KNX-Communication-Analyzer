'''
Created on 23-02-2021

@author: Thibaud
'''


#J'importe les packets de pyserial
import serial
from serial import Serial


def driverCap(userPort,nbBytes = 16):
    capKNX = serial.Serial(userPort, 9600, timeout= 1) # ici j'ouvre et configure le port série, en lui précisant le port sélectionner, puis le taux de bauds pour le port et je lui défini un timeout
    dataKNX = capKNX.readline(nbBytes) # ici je vais lire les données sur le port pour une durée de nbBytes 

    return dataKNX


print(driverCap('COM1',16))
l