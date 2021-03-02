# Kwin
import sys
import os

from PyQt5 import QtWidgets, QtGui, QtCore
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

"""app = QApplication(sys.argv)"""



class Fenetre_principale(QMainWindow):
    #Class for the main window

    def __init__(self, parent = None):
        # Class Constructor
        super().__init__(parent)
        self.setWindowTitle("Analyseur de trame KNX")
        self.setWindowIcon(QtGui.QIcon("C:\PROJET ANALYSEUR DE TRAMES KNX\KNX.png"))
        self.resize(400, 200)
        self.centralWidget = QLabel("Voici l'analyseur de trames KNX")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) 
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createMenuBar()
        self._createToolBars()

    def _createToolBars(self):
        #Creating a toolbar function
        fileToolBar = self.addToolBar("File")
        # Using a QToolBar object
        editToolBar = QToolBar("Edit", self) 
        self.addToolBar(editToolBar)
        # Using a QToolBar object and a toolbar area
        helpToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

    def _createMenuBar(self):
        #Create a menubar function
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Edit")
        #helpMenu = menuBar.addMenu("&Help")
        helpMenu = menuBar.addMenu(QIcon(""), "&Help")


    def _createDropDownMenu(self):
        #Create a dropdown menu function
        dropDownMenu = QComboBox("Veuillez choisir un port", self)
        self.addItems(["Port Com", "Port USB"]) 

    def _onClicked(self, val):
        #Check if any item is selected or not 
        if val == "Choissisez votre port":
            message = "Vous n'avez rien selectionné"
        
        else : 
            message = "Vous avez selectionné le port" + val 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre_principale()
    fenetre.show()
    sys.exit(app.exec_())









