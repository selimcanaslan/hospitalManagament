# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleted_records_list_sunum.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def slinenhasta(self):
        os.system("hasta_silme.py")
    def silinendoktor(self):
        os.system("doktor_silme.py")    
    def silinenmuayene(self):
        os.system("muayene_silme.py")     
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(265, 240)
        MainWindow.setMinimumSize(QtCore.QSize(265, 240))
        MainWindow.setMaximumSize(QtCore.QSize(265, 240))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 241, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.deleted_patient_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleted_patient_button.setFont(font)
        self.deleted_patient_button.setObjectName("deleted_patient_button")
        self.verticalLayout.addWidget(self.deleted_patient_button)
        self.deleted_doctor_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleted_doctor_button.setFont(font)
        self.deleted_doctor_button.setObjectName("deleted_doctor_button")
        self.verticalLayout.addWidget(self.deleted_doctor_button)
        self.deleted_muayene_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleted_muayene_button.setFont(font)
        self.deleted_muayene_button.setObjectName("deleted_muayene_button")
        self.verticalLayout.addWidget(self.deleted_muayene_button)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-72, -53, 351, 251))
        self.frame.setStyleSheet("background-color: rgb(70, 169, 135);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 21))
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
        self.deleted_patient_button.setText(_translate("MainWindow", "Silinen Hasta Kayitlari"))
        self.deleted_doctor_button.setText(_translate("MainWindow", "Silinen Doktor Kayitlari"))
        self.deleted_muayene_button.setText(_translate("MainWindow", "Silinen Muayene Kayitlari"))
        self.deleted_patient_button.clicked.connect(self.slinenhasta)
        self.deleted_doctor_button.clicked.connect(self.silinendoktor)
        self.deleted_muayene_button.clicked.connect(self.silinenmuayene)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
