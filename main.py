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
        self.combobox_fill()
        
        
    
 #######new
#Button Functions 
    def Handle_Buttons(self):            
        self.addon_button.clicked.connect(self.add_item)



  
        
    def combobox_fill(self):
                   
        db=sqlite3.connect("countrywingsdatabase.db") #database file
        cursor=db.cursor()
        
        command= ''' SELECT item_name from inventory''' # db command line filter
        result = cursor.execute(command)
        
        data = []
        # data = ['A','C','D','B']        
        for row in result.fetchall():
            data.append(row[0])
        # self.addon_listbox['values'] = data
        # return data
        # self.addon_listbox.items(data)
        for x in data:
            self.addon_listbox.addItem(x)
    
    def add_item(self):
        db=sqlite3.connect("countrywingsdatabase.db") #database file
        cursor2=db.cursor()        
        addon_text= str(self.addon_listbox.currentText())         
        getprice= ''' SELECT item_price from inventory where item_name =?''' # db command line filter        
        resultitem_price=cursor2.execute(getprice,[addon_text])        
        item_price=str(resultitem_price.fetchone()[0])        
        addon_list = [ addon_text, item_price ]        
        # addon_list = ['1','12323']
        table = self.addon_table        
        self.addTableRow(table , addon_list) 
            
    
    def addTableRow(self, addon_table, row_data):
        
        
        row = addon_table.rowCount()
        addon_table.setRowCount(row+1)
        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            addon_table.setItem(row, col, cell)
            col += 1

    








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

    
    
    
