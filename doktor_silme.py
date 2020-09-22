# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'silinen_doktor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction,QDateEdit, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
import tkinter.messagebox
import pyodbc

class Ui_MainWindow(object):
    def goster(self):
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SELIM\SQLSCA;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()  
            cursor.execute('SELECT * FROM hastane.dbo.silinmis_doktor_kayitlari')       
            self.tableWidget.setRowCount(20)
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setColumnWidth
            records = cursor.fetchall()
            a=1
            b=0
            self.tableWidget.clear()
            for row in records:
                self.tableWidget.setItem(0,0, QTableWidgetItem("ID"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("AD"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("SOYAD"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("UNVAN"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("CINSIYET"))
                self.tableWidget.setItem(0,5, QTableWidgetItem("DOGUM TARIHI"))
                self.tableWidget.setItem(0,6, QTableWidgetItem("SILINME TARIHI"))
                self.tableWidget.setItem(a,b, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(a,b+1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(a,b+2, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(a,b+3, QTableWidgetItem(row[3]))
                self.tableWidget.setItem(a,b+4, QTableWidgetItem(row[4]))
                self.tableWidget.setItem(a,b+5, QTableWidgetItem(str(row[6])))
                self.tableWidget.setItem(a,b+6, QTableWidgetItem(str(row[6])))

                a=a+1
                conn.commit()
        finally:
            if (conn):
                conn.close()      
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 550)
        MainWindow.setMinimumSize(QtCore.QSize(730, 550))
        MainWindow.setMaximumSize(QtCore.QSize(730, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 730, 550))
        self.tableWidget.setMinimumSize(QtCore.QSize(730, 550))
        self.tableWidget.setMaximumSize(QtCore.QSize(730, 550))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Column"))
        self.goster()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
