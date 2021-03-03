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
        #self._createDropDownMenu()
        #self.comboBox = QComboBox()
        #self.comboBox.setGeometry(QRect(40, 40, 491, 31))
        #self.comboBox.setObjectName(("comboBox"))
        #self.comboBox.addItem("PyQt")
        #self.comboBox.addItem("Qt")
        #self.comboBox.addItem("Python")
        #self.comboBox.addItem("Example")
        combo = QComboBox(self)
        combo.addItems(["Veuillez choisir un port", "Port 1", "Port 2"])
        combo.setGeometry(QRect(40, 40, 200, 31))
        combo.move(50, 50)

        self.qlabel = QLabel(self)
        self.qlabel.move(50,15)
        self.qlabel.setAlignment(Qt.AlignHCenter)
        #combo.activated[str].connect(self.onChanged)      


    def _createToolBars(self):
        #Creating a toolbar function
        fileToolBar = self.addToolBar("Fichier")
        # Using a QToolBar object
        editToolBar = QToolBar("Édition", self) 
        self.addToolBar(editToolBar)
        # Using a QToolBar object and a toolbar area
        helpToolBar = QToolBar("Aide", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

    def _createMenuBar(self):
        #Create a menubar function
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&Fichier", self)
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Édition")
        #helpMenu = menuBar.addMenu("&Help")
        helpMenu = menuBar.addMenu(QIcon(""), "&Aide")

    def _onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()



    #def _createDropDownMenu(self):
        #Create a dropdown menu function
        #dropDownMenu = self.QComboBox("Veuillez choisir un port")
        #self.addItems(["Port Com", "Port USB"]) 
       
    #def _onClicked(self, val):
        #Check if any item is selected or not 
        #if val == "Choissisez votre port":
         #   message = "Vous n'avez rien selectionné"
        
        #else : 
         #   message = "Vous avez selectionné le port" + val 

        #self.msg"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre_principale()
    fenetre.show()
    sys.exit(app.exec_())









