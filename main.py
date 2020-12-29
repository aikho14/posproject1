from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import sys
from os import path
from PyQt5.uic import loadUiType

FORM_x,_=loadUiType(path.join(path.dirname('__file__'),"sales.ui"))
FORM_x1,_=loadUiType(path.join(path.dirname('__file__'),"main.ui"))   



import sqlite3

#inventory form
class Another_Main(QMainWindow, FORM_x1):
    def __init__(self,parent=None):
        super(Another_Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
    
 
#Button Functions 
    def Handle_Buttons(self):
        pass
    
   
    
#sales window______________________________________________________--------------------------------------------        
class Main(QMainWindow, FORM_x):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
    
 
#Button Functions 
    def Handle_Buttons(self):
        self.addon_button.clicked.connect(self.combobox_fill)




    def combobox_fill(self):
        
        db=sqlite3.connect("countrywingsdatabase.db") #database file
        cursor=db.cursor()
        
        command= ''' SELECT item_name from inventory''' # db command line filter
        result=cursor.execute(command)
        
        x= str(result.fetchall())
        
        command2= ''' SELECT max(item_id) from inventory''' # db command line filter
        result2=cursor.execute(command)
        
        
        for i in enumerate(result2):
            self.addon_listbox.addItem(str(i))
        







   













def main():
        app=QApplication(sys.argv)
        window=Main()
        
        window.show()
        app.exec_()  
        

def mains():
        app=QApplication(sys.argv)
        window=Another_Main()
        window.show()
        app.exec_() 

        
 #updatelistbox

main()

    
    
    
