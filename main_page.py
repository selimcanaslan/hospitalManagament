from PyQt5.QtWidgets import QMainWindow, QApplication, QAction,QDateEdit, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
import tkinter.messagebox
import pyodbc
import os
import webbrowser
Tk().withdraw()
class Ui_MainWindow(object):
    #Hasta Listeleme
    def satir(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('EXEC row_sayisi')
        records = cursor.fetchall()  

        sayi = str(records[0])
        uzunluk = len(sayi)

        if(uzunluk == 5):
            columnS = (int(sayi[1:2]))
            columnS = columnS +1
            return columnS
        elif (uzunluk == 6):
            columnS = (int(sayi[1:3]))
            columnS = columnS +1
            return columnS   
        elif (uzunluk == 7):
            columnS = (int(sayi[1:4]))
            columnS = columnS +1
            return columnS    
        elif (uzunluk == 8):
            columnS = (int(sayi[1:5]))
            columnS = columnS +1
            return columnS       
        elif (uzunluk == 9):
            columnS = (int(sayi[1:6]))
            columnS = columnS +1
            return columnS     
        elif (uzunluk == 10):
            columnS = (int(sayi[1:7]))
            columnS = columnS +1
            return columnS                             
        elif (uzunluk == 11):
            columnS = (int(sayi[1:8]))
            columnS = columnS +1
            return columnS     
        '''if (len(sayi ==))'''
        '''return int(sayi[1:4])  ''' 
    def show_patients(self):
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()  
            cursor.execute('SELECT * FROM hastane.dbo.hasta')   

            x = self.satir()  
            self.tableWidget.setRowCount(x)
            self.tableWidget.setColumnCount(11)
            self.tableWidget.setColumnWidth
            records = cursor.fetchall()
            a=1
            b=0
            self.tableWidget.clear()
            for row in records:
                self.tableWidget.setItem(0,0, QTableWidgetItem("Hasta ID"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("Hasta Adı"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("Hasta Soyadı"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("Hasta Adres"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("Cep Tel"))
                self.tableWidget.setItem(0,5, QTableWidgetItem("TC No"))
                self.tableWidget.setItem(0,6, QTableWidgetItem("Cinsiyet"))
                self.tableWidget.setItem(0,7, QTableWidgetItem("Kayıt Tarihi"))
                self.tableWidget.setItem(0,8, QTableWidgetItem("Kan Grubu"))
                self.tableWidget.setItem(0,9, QTableWidgetItem("Doğum Tarihi"))
                self.tableWidget.setItem(0,10, QTableWidgetItem("Doğum Yeri"))
                self.tableWidget.setItem(a,b, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(a,b+1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(a,b+2, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(a,b+3, QTableWidgetItem(row[3]))
                self.tableWidget.setItem(a,b+4, QTableWidgetItem(row[4]))
                self.tableWidget.setItem(a,b+5, QTableWidgetItem(row[5]))
                self.tableWidget.setItem(a,b+6, QTableWidgetItem(row[6]))
                self.tableWidget.setItem(a,b+7, QTableWidgetItem(str(row[7])))
                self.tableWidget.setItem(a,b+8, QTableWidgetItem(row[8]))
                self.tableWidget.setItem(a,b+9, QTableWidgetItem(str(row[9])))
                self.tableWidget.setItem(a,b+10, QTableWidgetItem(row[10]))
                a=a+1
                conn.commit()
        finally:
            if (conn):
                conn.close()
#Hasta Ekleme   
    def hasta_ekleme(self): 
        hasta_ad = self.patient_name.text()
        hasta_soyad = self.patient_surname.text()
        hasta_adres = self.patient_adress.text()
        cep_tel = self.patient_phone.text()
        cinsiyet = self.patient_gender.text()
        kangrubu = self.patient_blood_type.text()
        tcno = self.patient_tcno.text()
        dogumtar = self.patient_dob.text()
        dogumyeri = self.patient_country.text()

        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO hastane.dbo.hasta (hasta_ad,hasta_soyad,hasta_adres,hasta_CepTel,hasta_tcno,hasta_cinsiyet,hasta_kanGrubu,hasta_dogTar,hasta_dogYer)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s') '''%(hasta_ad,hasta_soyad,hasta_adres,cep_tel,tcno,cinsiyet,kangrubu,dogumtar,dogumyeri))
        conn.commit()                                    
#Hasta Ekle Message Box    
    def hastaekle_mesaj(self,MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Hasta Basariyla Eklendi", icon='info') 
#Doktor Sil Message Box
    def doktor_delete_messagebox(self,MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Doktor Bilgiler Basariyla Silindi", icon='info')                           
#Hasta update
    def hasta_update(self): 
        hasta_ad = self.patient_name.text()
        hasta_soyad = self.patient_surname.text()
        hasta_adres = self.patient_adress.text()
        cep_tel = self.patient_phone.text()
        cinsiyet = self.patient_gender.text()
        kayittar = self.patient_registiration_date.text()
        kangrubu = self.patient_blood_type.text()
        dogumtar = self.patient_dob.text()
        dogumyeri = self.patient_country.text()
        tcno = self.patient_tcno.text()

        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                UPDATE hastane.dbo.hasta SET hasta_ad=?,hasta_soyad =?,hasta_adres=?,hasta_CepTel=?,hasta_cinsiyet=?,hasta_kayittar=?,hasta_kanGrubu=?,hasta_dogTar=?,hasta_dogYer=? WHERE hasta_tcno=? ''',hasta_ad,hasta_soyad,hasta_adres,cep_tel,cinsiyet,kayittar,kangrubu,dogumtar,dogumyeri,tcno)
        conn.commit()  
#Hasta Update Message Box
    def hasta_update_mesaj(self,MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Hasta Bilgileri Basariyla Guncellendi", icon='info')
#Hasta Delete Message Box
    def hasta_delete_message_box(self,MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Hasta Bilgileri Basariyla Silindi", icon='info')
#Doktor Ekle Message Box
    def doktor_ekle_messagebox(self,MainWindow):  
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Yeni Doktor Basariyla Eklendi", icon='info')                                            
#Hasta tcno Arama          
    def hasta_tcno_search(self):
        tcno = self.hasta_tcno_arama.text()
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()  
            cursor.execute("EXEC hasta_getir @tcno= ?",tcno)       
            self.tableWidget.setRowCount(20)
            self.tableWidget.setColumnCount(11)
            self.tableWidget.setColumnWidth
            records = cursor.fetchall()
            a=1
            b=0
            self.tableWidget.clear()
            for row in records:
                self.tableWidget.setItem(0,0, QTableWidgetItem("Hasta ID"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("Hasta Adı"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("Hasta Soyadı"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("Hasta Adres"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("Cep Tel"))
                self.tableWidget.setItem(0,5, QTableWidgetItem("TC No"))
                self.tableWidget.setItem(0,6, QTableWidgetItem("Cinsiyet"))
                self.tableWidget.setItem(0,7, QTableWidgetItem("Kayıt Tarihi"))
                self.tableWidget.setItem(0,8, QTableWidgetItem("Kan Grubu"))
                self.tableWidget.setItem(0,9, QTableWidgetItem("Doğum Tarihi"))
                self.tableWidget.setItem(0,10, QTableWidgetItem("Doğum Yeri"))
                self.tableWidget.setItem(a,b, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(a,b+1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(a,b+2, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(a,b+3, QTableWidgetItem(row[3]))
                self.tableWidget.setItem(a,b+4, QTableWidgetItem(row[4]))
                self.tableWidget.setItem(a,b+5, QTableWidgetItem(row[5]))
                self.tableWidget.setItem(a,b+6, QTableWidgetItem(row[6]))
                self.tableWidget.setItem(a,b+7, QTableWidgetItem(str(row[7])))
                self.tableWidget.setItem(a,b+8, QTableWidgetItem(row[8]))
                self.tableWidget.setItem(a,b+9, QTableWidgetItem(str(row[9])))
                self.tableWidget.setItem(a,b+10, QTableWidgetItem(row[10]))
                a=a+1
                conn.commit()
        finally:
            if (conn):
                conn.close()             
#Hasta isimle arama
    def hasta_isim_search(self):
        isim = self.hasta_ad_arama.text()
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()  
            cursor.execute("EXEC hasta_getir_ad @ad= ?",isim)       
            self.tableWidget.setRowCount(20)
            self.tableWidget.setColumnCount(11)
            self.tableWidget.setColumnWidth
            records = cursor.fetchall()
            a=1
            b=0
            self.tableWidget.clear()
            for row in records:
                self.tableWidget.setItem(0,0, QTableWidgetItem("Hasta ID"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("Hasta Adı"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("Hasta Soyadı"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("Hasta Adres"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("Cep Tel"))
                self.tableWidget.setItem(0,5, QTableWidgetItem("TC No"))
                self.tableWidget.setItem(0,6, QTableWidgetItem("Cinsiyet"))
                self.tableWidget.setItem(0,7, QTableWidgetItem("Kayıt Tarihi"))
                self.tableWidget.setItem(0,8, QTableWidgetItem("Kan Grubu"))
                self.tableWidget.setItem(0,9, QTableWidgetItem("Doğum Tarihi"))
                self.tableWidget.setItem(0,10, QTableWidgetItem("Doğum Yeri"))
                self.tableWidget.setItem(a,b, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(a,b+1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(a,b+2, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(a,b+3, QTableWidgetItem(row[3]))
                self.tableWidget.setItem(a,b+4, QTableWidgetItem(row[4]))
                self.tableWidget.setItem(a,b+5, QTableWidgetItem(row[5]))
                self.tableWidget.setItem(a,b+6, QTableWidgetItem(row[6]))
                self.tableWidget.setItem(a,b+7, QTableWidgetItem(str(row[7])))
                self.tableWidget.setItem(a,b+8, QTableWidgetItem(row[8]))
                self.tableWidget.setItem(a,b+9, QTableWidgetItem(str(row[9])))
                self.tableWidget.setItem(a,b+10, QTableWidgetItem(row[10]))
                a=a+1
                conn.commit()
        finally:
            if (conn):
                conn.close() 
#Muayene Id Ile Arama
    def hasta_muayene_id_search(self):
        hastaId = self.hasta_id_arama.text()
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()  
            cursor.execute("EXEC muayene_listele @hastaId= ?",hastaId)       
            self.tableWidget.setRowCount(20)
            self.tableWidget.setColumnCount(11)
            self.tableWidget.setColumnWidth
            records = cursor.fetchall()
            a=1
            b=0
            self.tableWidget.clear()
            for row in records:
                self.tableWidget.setItem(0,0, QTableWidgetItem("Muayene ID"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("Hasta ID"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("Muayene Tarihi"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("Muayene Saati"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("Doktor Id"))
                self.tableWidget.setItem(a,b, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(a,b+1, QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(a,b+2, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(a,b+3, QTableWidgetItem(row[3]))
                self.tableWidget.setItem(a,b+4, QTableWidgetItem(str(row[4])))
                a=a+1
                conn.commit()
        finally:
            if (conn):
                conn.close()                     
#Hasta doktor ekleme                                          
    def doktor_ekleme(self): 
        doktorAd = self.doktor_ad_edit.text()
        doktorSoyad = self.doktor_soyad_edit.text()
        doktorUnvan = self.doktor_unvan_edit.text()
        doktorCinsiyet = self.doktor_cinsiyet_edit.text()
        doktorDob = self.doktor_dob_edit.text()

        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                INSERT INTO hastane.dbo.doktor (doc_ad,doc_soyad,doc_unvan,doc_cinsiyet,doc_DogTar)
                 VALUES 
                ('%s','%s','%s','%s','%s') 
                '''%(doktorAd,doktorSoyad,doktorUnvan,doktorCinsiyet,doktorDob))
        conn.commit()
#Doktor LineEdit temizleme   
    def clearDataDoctor(self):
        self.doktor_ad_edit.setText("")
        self.doktor_dob_edit.setText("")
        self.doktor_soyad_edit.setText("")
        self.doktor_cinsiyet_edit.setText("")
        self.doktor_unvan_edit.setText("")
        self.doktor_sil_id.setText("")
#Muayene Ekle
    def muayene_ekle(self):
        patientid=self.muayene_add_hasta_id.text()
        docId=self.doctor_id.text()
        MuayeneType=self.muayene_turu.text()

        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO hastane.dbo.muayene (hastaId,doktorId,muayeneTuru)VALUES ('%s','%s','%s') '''%(patientid,docId,MuayeneType))
        conn.commit()    
#Muayene Ekle MessageBox
    def muayene_ekle_messagebox(self,MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Yeni Muayene Basariyla Eklendi", icon='info')                               
#Muayene Silme
    def deleteMuayene(self):
        muayeneid = self.muayene_sil_muayene_id.text()   
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                DELETE FROM muayene where muayeneId = '%s'
                '''%(muayeneid))
        conn.commit()
#Muayene Silme sonrasi text temizleme
    def muayene_id_text_clear(self):
        self.muayene_sil_muayene_id.setText("")
#Muayene Silme Button message box
    def muayene_delete_messagebox(self,MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Muayene Basariyla Silindi ! ", icon='info')

#Doktor Silme   
    def deleteDoktor(self):
        doktorid = self.doktor_sil_id.text()   
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                DELETE FROM dbo.doktor where doktorId = '%s'
                '''%(doktorid))
        conn.commit()  
#Doktor bilgileri aktarma    
    def show_doctor(self):
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()  
            cursor.execute('SELECT * FROM hastane.dbo.doktor')       
            self.tableWidget.setRowCount(20)
            self.tableWidget.setColumnCount(11)
            self.tableWidget.setColumnWidth
            records = cursor.fetchall()
            a=1
            b=0
            self.tableWidget.clear()
            for row in records:
                self.tableWidget.setItem(0,0, QTableWidgetItem("Doktor ID"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("Doktor Adı"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("Doktor Soyadı"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("Unvan"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("Cinsiyet"))
                self.tableWidget.setItem(0,5, QTableWidgetItem("Doğum Tarihi"))
                self.tableWidget.setItem(a,b, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(a,b+1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(a,b+2, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(a,b+3, QTableWidgetItem(row[3]))
                self.tableWidget.setItem(a,b+4, QTableWidgetItem(row[4]))
                self.tableWidget.setItem(a,b+5, QTableWidgetItem(str(row[5])))
                a=a+1
                conn.commit()
        finally:
            if (conn):
                conn.close() 
#Muayene bilgileri aktarma
    def show_muayene(self):
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()  
            cursor.execute('SELECT * FROM hastane.dbo.muayene')       
            self.tableWidget.setRowCount(20)
            self.tableWidget.setColumnCount(11)
            self.tableWidget.setColumnWidth
            records = cursor.fetchall()
            a=1
            b=0
            self.tableWidget.clear()
            for row in records:
                self.tableWidget.setItem(0,0, QTableWidgetItem("Muayene ID"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("Hasta ID"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("Muayene Tarihi"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("Muayene Saat"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("Doktor ID"))
                self.tableWidget.setItem(0,5, QTableWidgetItem("Muayene Turu"))
                self.tableWidget.setItem(a,b, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(a,b+1, QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(a,b+2, QTableWidgetItem(str(row[2])))
                self.tableWidget.setItem(a,b+3, QTableWidgetItem(str(row[3])))
                self.tableWidget.setItem(a,b+4, QTableWidgetItem(str(row[4])))
                self.tableWidget.setItem(a,b+5, QTableWidgetItem(str(row[5])))
                a=a+1
                conn.commit()
        finally:
            if (conn):
                conn.close()  
#Muayene sonucu aktarma
    def show_muayeneSonuc(self):
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()  
            cursor.execute('''select hasta_ad AS 'ADI',hasta_soyad AS 'SOYADI',hasta_tcno AS 'TCNO',hasta_cinsiyet AS 'CINSIYET',hasta_kanGrubu AS 'KAN GRUBU',hasta_dogTar AS 'DOGUM TARIHI',d.doc_ad AS 'DOKTORUN ADI',d.doc_soyad AS 'DOKTORUN SOYADI',m.muayeneTar as 'MUAYENE TARIHI',m.muayeneSaat AS 'MUAYENE SAATI',ms.aciklama AS 'SONUC' from hasta h join muayene m on h.hastaId=m.hastaId join doktor d on d.doktorId=m.doktorId join muayeneSonuc ms on m.muayeneId=ms.muayeneId ''')       
            self.tableWidget.setRowCount(20)
            self.tableWidget.setColumnCount(11)
            records = cursor.fetchall()
            a=1
            b=0
            self.tableWidget.clear()
            for row in records:
                self.tableWidget.setItem(0,0, QTableWidgetItem("ADI"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("SOYADI"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("TCNO"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("CINSIYET"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("KAN GRUBU"))
                self.tableWidget.setItem(0,5, QTableWidgetItem("D.TARIHI"))
                self.tableWidget.setItem(0,6, QTableWidgetItem("DOKTOR AD"))
                self.tableWidget.setItem(0,7, QTableWidgetItem("DOKTOR SOYAD"))
                self.tableWidget.setItem(0,8, QTableWidgetItem("MUAYENE TAR."))
                self.tableWidget.setItem(0,9, QTableWidgetItem("MUAYENE SAATI"))
                self.tableWidget.setItem(0,10, QTableWidgetItem("SONUC"))
                self.tableWidget.setItem(a,b, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(a,b+1, QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(a,b+2, QTableWidgetItem(str(row[2])))
                self.tableWidget.setItem(a,b+3, QTableWidgetItem(str(row[3])))
                self.tableWidget.setItem(a,b+4, QTableWidgetItem(str(row[4])))
                self.tableWidget.setItem(a,b+5, QTableWidgetItem(str(row[5])))
                self.tableWidget.setItem(a,b+6, QTableWidgetItem(str(row[6])))
                self.tableWidget.setItem(a,b+7, QTableWidgetItem(str(row[7])))
                self.tableWidget.setItem(a,b+8, QTableWidgetItem(str(row[8])))
                self.tableWidget.setItem(a,b+9, QTableWidgetItem(str(row[9])))
                self.tableWidget.setItem(a,b+10, QTableWidgetItem(str(row[10])))
                a=a+1
                conn.commit()
        finally:
            if (conn):
                conn.close()
#Ameliyat Tablo aktarma                    
    def show_ameliyat(self):
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
            cursor = conn.cursor()  
            cursor.execute('SELECT * FROM hastane.dbo.ameliyat')       
            self.tableWidget.setRowCount(20)
            self.tableWidget.setColumnCount(11)
            self.tableWidget.setColumnWidth
            records = cursor.fetchall()
            a=1
            b=0
            self.tableWidget.clear()
            for row in records:
                self.tableWidget.setItem(0,0, QTableWidgetItem("Ameliyat ID"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("Ameliyat Türü"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("Açıklama"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("Ücret"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("Hasta ID"))
                self.tableWidget.setItem(0,5, QTableWidgetItem("Doktor ID"))
                self.tableWidget.setItem(a,b, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(a,b+1, QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(a,b+2, QTableWidgetItem(str(row[2])))
                self.tableWidget.setItem(a,b+3, QTableWidgetItem(str(row[3])))
                self.tableWidget.setItem(a,b+4, QTableWidgetItem(str(row[4])))
                self.tableWidget.setItem(a,b+5, QTableWidgetItem(str(row[5])))
                a=a+1
                conn.commit()
        finally:
            if (conn):
                conn.close()     
#Hasta bilgisi getirme
    def patient_text_aktar(self):
        tcno=self.patient_tcno.text()
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
        cursor = conn.cursor()  
        cursor.execute("""SELECT * FROM hastane.dbo.hasta WHERE hasta_tcno='%s'"""%(tcno))       
        records = cursor.fetchall()
        for row in records:
            self.patient_name.setText(row[1])
            self.patient_surname.setText(row[2])
            self.patient_adress.setText(row[3])
            self.patient_phone.setText(row[4])
            self.patient_registiration_date.setText(str(row[7]))
            self.patient_gender.setText(row[6])
            self.patient_blood_type.setText(row[8])
            self.patient_dob.setText(row[9])
            self.patient_tcno.setText(row[5])
            self.patient_country.setText(row[10])
            self.hasta_id.setText(str(row[0]))
     
#Hasta Line edit temizleme                                                    
    def clearData(self):
        self.patient_name.setText("")
        self.patient_surname.setText("") 
        self.patient_adress.setText("") 
        self.patient_phone.setText("") 
        self.patient_registiration_date.setText("Otomatik Atanir") 
        self.patient_gender.setText("") 
        self.patient_blood_type.setText("") 
        self.patient_tcno.setText("") 
        self.patient_country.setText("")
        self.hasta_id.setText("")
        self.patient_dob.clear()

#Muayene Silme        
    def deleteMuayene(self):
        muayeneid = self.muayene_sil_muayene_id.text()   
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                DELETE FROM muayene where muayeneId = '%s'
                '''%(muayeneid))
        conn.commit() 
#Hasta Silme
    def hasta_delete(self):
        hastatcno = self.patient_tcno.text()   
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                DELETE FROM hasta where hasta_tcno = '%s'
                '''%(hastatcno))
        conn.commit()         
#Ameliyat Ekleme
    def ameliyat_ekle(self):
        tur = self.ameliyat_turu.text()
        aciklama = self.ameliyat_aciklama.text()
        ucret = self.ameliyat_ucret.text()
        hastaId = self.ameliyat_hasta_id.text()
        doktorId = self.ameliyat_doktor_id.text()
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                INSERT ameliyat VALUES ('%s','%s','%s','%s','%s')
                '''%(tur,aciklama,ucret,hastaId,doktorId))
        conn.commit() 
#Ameliyat ekle messagebox
    def ameliyat_ekle_messagebox(self,MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Ameliyat Basariyla Eklendi", icon='info')            
#Muayene Sonucu Ekleme
    def muayene_sonuc_ekle(self):
        ms_muayeneId = self.muayeneSonuc_muayeneId.text()
        ms_aciklama = self.muayene_sonuc_text_edit.toPlainText()
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                INSERT muayeneSonuc VALUES ('%s','%s')
                '''%(ms_muayeneId,ms_aciklama))
        conn.commit() 
#Muayene Sonuc Update
    def muayene_sonuc_update(self):
        ms_muayeneId = self.muayeneSonuc_muayeneId.text()
        ms_aciklama = self.muayene_sonuc_text_edit.toPlainText()

        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                UPDATE hastane.dbo.muayeneSonuc SET aciklama=? WHERE muayeneId=? ''',ms_aciklama,ms_muayeneId)
        conn.commit()                  

#Muayene Guncelleme
    def muayene_update(self): 
        mid=self.muayene_add_hasta_id.text()
        tarih=self.date_of_muayene.text()
        mtime=self.muayene_time.text()         
        did=self.doctor_id.text()
        mtype=self.muayene_turu.text()
        muayeneid=self.muayeneSonuc_muayeneId.text()

        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                UPDATE hastane.dbo.muayene SET hastaId=?,muayeneTar =?,muayeneSaat=?,doktorId=?,muayeneTuru=? WHERE muayeneId=? ''',mid,tarih,mtime,did,mtype,muayeneid)
        conn.commit()  
#Muayene guncelleme message box
    def muayene_update_messagebox(self,MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Muayene Bilgileri Basariyla Guncellendi", icon='info')    
#Ameliyat guncelleme messagebox
    def ameliyat_update_messagebox(self,MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Ameliyat Bilgileri Basariyla Guncellendi", icon='info')                                
#Ameliyat Text Clear
    def ameliyat_text_clear(self):
        self.ameliyat_turu.setText("")
        self.ameliyat_aciklama.setText("")
        self.ameliyat_ucret.setText("") 
        self.ameliyat_hasta_id.setText("")
        self.ameliyat_doktor_id.setText("")   
        self.ameliyat_id_get.clear()             
#Muayene bilgi getirme
    def muayene_get_info(self):
        muayeneid=self.muayeneSonuc_muayeneId.text()
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
        cursor = conn.cursor()  
        cursor.execute("""SELECT * FROM hastane.dbo.muayene WHERE muayeneId='%s'"""%(muayeneid))       
        records = cursor.fetchall()
        for row in records:
            self.muayene_add_hasta_id.setText(str(row[1]))
            self.date_of_muayene.setText(str(row[2]))
            self.muayene_time.setText(str(row[3]))
            self.doctor_id.setText(str(row[4]))
            self.muayene_turu.setText(row[5])
#Muayene Sonuc getirme
    def muayene_sonuc_get_info(self):
        muayeneid=self.muayeneSonuc_muayeneId.text()
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
        cursor = conn.cursor()  
        cursor.execute("""SELECT * FROM hastane.dbo.muayeneSonuc WHERE muayeneId='%s'"""%(muayeneid))       
        records = cursor.fetchall()
        self.muayene_sonuc_text_edit.clear()
        for row in records:
            self.muayene_sonuc_text_edit.insertPlainText(row[2])    
#MuayeneSonuc Tex Clear
    def muayene_sonuc_text_clear(self):
        self.muayeneSonuc_muayeneId.clear()
        self.muayene_sonuc_text_edit.clear()   
#Muayene text clear
    def muayene_clear(self):
        self.muayene_add_hasta_id.clear()
        self.doctor_id.clear()
        self.muayene_turu.clear() 
        self.muayene_time.clear()
        self.date_of_muayene.clear()
        self.date_of_muayene.setText("Otomatik Atanir")
        self.muayene_time.setText("Otomatik Atanir")

#Ameliyat bilgi getirme
    def ameliyat_gett_info(self):
        ameliyatid=self.ameliyat_id_get.text()
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')
        cursor = conn.cursor()  
        cursor.execute("""SELECT * FROM hastane.dbo.ameliyat WHERE ameliyatId='%s'"""%(ameliyatid))       
        records = cursor.fetchall()
        self.muayene_sonuc_text_edit.clear()
        for row in records:
            self.ameliyat_turu.setText(row[1])
            self.ameliyat_aciklama.setText(row[2])
            self.ameliyat_ucret.setText(str(row[3]))
            self.ameliyat_hasta_id.setText(str(row[4]))
            self.ameliyat_doktor_id.setText(str(row[5]))
#Ameliyat Guncelleme
    def ameliyat_update(self):
        tur=self.ameliyat_turu.text()
        aciklama=self.ameliyat_aciklama.text()
        ucret=self.ameliyat_ucret.text()         
        hid=self.ameliyat_hasta_id.text()
        did=self.ameliyat_doktor_id.text()
        amid=self.ameliyat_id_get.text()

        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SCA\TEW_SQLEXPRESS;'
                      'Database=hastane;'
                      'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute('''

                UPDATE hastane.dbo.ameliyat SET ameliyatturu=?,ameliyataciklama =?,ameliyatucret=?,hastaId=?,doktorId=? WHERE ameliyatId=? ''',tur,aciklama,ucret,hid,did,amid)
        conn.commit()                                      
#deleted_record_button_def
    def deleted_records_list(self):
        os.system("delete_record_list.py")
#muayene sonucu ekle messagebox
    def muayene_sonuc_ekle_messagebox(self):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Muayene Sonucu Basariyla Eklendi", icon='info')         
#muayene sonucu guncelle messagebox
    def muayene_sonuc_guncelle_messagebox(self):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Muayene Sonucu Basariyla Guncellendi", icon='info')   
# Yetki sayfasi acma
    def yetki_page(self):
        os.system("yetkili_kullanicilar.py")                    
#Backup Alma
    def get_backup(self):
        connection = pyodbc.connect(driver='{SQL Server Native Client 11.0}', 
        server='SCA\TEW_SQLEXPRESS', database='master', 
        trusted_connection='yes', autocommit=True)
        try:
            os.remove('C:\Program Files\Microsoft SQL Server\MSSQL14.SQLSCA\MSSQL\Backup\hastane.bak')
        except OSError:
            pass
          
        backup = "EXEC back_up"
        cursor = connection.cursor().execute(backup)
        while cursor.nextset():
            pass

        connection.close()
#Backup Button show message
    def backup_messagebox(self,MainWindow):
        root = tkinter.Tk()
        root.withdraw()
        exit = tkinter.messagebox.showinfo("Bilgi","Yedek Alma Basarili", icon='info')
#Open Folder
    def backup_open_folder(self):
        webbrowser.open ('C:\Program Files\Microsoft SQL Server\MSSQL14.SQLSCA\MSSQL\Backup')
#Restore backup
    def restore_backup(self):
        connection = pyodbc.connect(driver='{SQL Server Native Client 11.0}', 
        server='SCA\TEW_SQLEXPRESS', database='master', 
        trusted_connection='yes', autocommit=True)  
        backup = "EXEC restore_back_up"
        cursor = connection.cursor().execute(backup)   
        while cursor.nextset():
            pass                     
        connection.close()
#Exit Button
    def exit(self):
        msgbox= tkinter.messagebox.askyesno('UYARI','Cikmak istediginize emin misiniz ?' )
        if msgbox > 0 :    
            exit()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 819)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 819))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 819))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(420, 680, 135, 70))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Muayene_Arama = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Muayene_Arama.setContentsMargins(0, 0, 0, 0)
        self.Muayene_Arama.setObjectName("Muayene_Arama")
        self.muayene_id_search_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.muayene_id_search_text.setFont(font)
        self.muayene_id_search_text.setAlignment(QtCore.Qt.AlignCenter)
        self.muayene_id_search_text.setObjectName("muayene_id_search_text")
        self.Muayene_Arama.addWidget(self.muayene_id_search_text)
        self.hasta_id_arama = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hasta_id_arama.setObjectName("hasta_id_arama")
        self.Muayene_Arama.addWidget(self.hasta_id_arama)
        self.hasta_id_arama_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hasta_id_arama_button.setObjectName("hasta_id_arama_button")
        self.Muayene_Arama.addWidget(self.hasta_id_arama_button)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(570, 680, 135, 70))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Hasta_Adile_Arama = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Hasta_Adile_Arama.setContentsMargins(0, 0, 0, 0)
        self.Hasta_Adile_Arama.setObjectName("Hasta_Adile_Arama")
        self.hasta_ad_search_text = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.hasta_ad_search_text.setFont(font)
        self.hasta_ad_search_text.setAlignment(QtCore.Qt.AlignCenter)
        self.hasta_ad_search_text.setObjectName("hasta_ad_search_text")
        self.Hasta_Adile_Arama.addWidget(self.hasta_ad_search_text)
        self.hasta_ad_arama = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.hasta_ad_arama.setObjectName("hasta_ad_arama")
        self.Hasta_Adile_Arama.addWidget(self.hasta_ad_arama)
        self.hasta_ad_arama_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.hasta_ad_arama_button.setObjectName("hasta_ad_arama_button")
        self.Hasta_Adile_Arama.addWidget(self.hasta_ad_arama_button)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(720, 680, 135, 70))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Hasta_Tcnoile_Arama = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Hasta_Tcnoile_Arama.setContentsMargins(0, 0, 0, 0)
        self.Hasta_Tcnoile_Arama.setObjectName("Hasta_Tcnoile_Arama")
        self.hasta_tcno_search_text = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.hasta_tcno_search_text.setFont(font)
        self.hasta_tcno_search_text.setAlignment(QtCore.Qt.AlignCenter)
        self.hasta_tcno_search_text.setObjectName("hasta_tcno_search_text")
        self.Hasta_Tcnoile_Arama.addWidget(self.hasta_tcno_search_text)
        self.hasta_tcno_arama = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.hasta_tcno_arama.setObjectName("hasta_tcno_arama")
        self.Hasta_Tcnoile_Arama.addWidget(self.hasta_tcno_arama)
        self.hasta_tcno_arama_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.hasta_tcno_arama_button.setObjectName("hasta_tcno_arama_button")
        self.Hasta_Tcnoile_Arama.addWidget(self.hasta_tcno_arama_button)
        self.hasta_add_text = QtWidgets.QLabel(self.centralwidget)
        self.hasta_add_text.setGeometry(QtCore.QRect(10, 45, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hasta_add_text.setFont(font)
        self.hasta_add_text.setObjectName("hasta_add_text")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 65, 1271, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.patient_name_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_name_text.setGeometry(QtCore.QRect(20, 85, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_name_text.setFont(font)
        self.patient_name_text.setObjectName("patient_name_text")
        self.patient_surname_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_surname_text.setGeometry(QtCore.QRect(20, 105, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_surname_text.setFont(font)
        self.patient_surname_text.setObjectName("patient_surname_text")
        self.patient_adress_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_adress_text.setGeometry(QtCore.QRect(20, 125, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_adress_text.setFont(font)
        self.patient_adress_text.setObjectName("patient_adress_text")
        self.patient_phone_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_phone_text.setGeometry(QtCore.QRect(20, 145, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_phone_text.setFont(font)
        self.patient_phone_text.setObjectName("patient_phone_text")
        self.patient_tcno_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_tcno_text.setGeometry(QtCore.QRect(200, 105, 71, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_tcno_text.setFont(font)
        self.patient_tcno_text.setObjectName("patient_tcno_text")
        self.patient_gender_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_gender_text.setGeometry(QtCore.QRect(200, 85, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_gender_text.setFont(font)
        self.patient_gender_text.setObjectName("patient_gender_text")
        self.patient_registiration_date_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_registiration_date_text.setGeometry(QtCore.QRect(20, 165, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_registiration_date_text.setFont(font)
        self.patient_registiration_date_text.setObjectName("patient_registiration_date_text")
        self.patient_blood_type_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_blood_type_text.setGeometry(QtCore.QRect(200, 105, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_blood_type_text.setFont(font)
        self.patient_blood_type_text.setObjectName("patient_blood_type_text")
        self.patient_dob_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_dob_text.setGeometry(QtCore.QRect(200, 145, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.patient_dob_text.setFont(font)
        self.patient_dob_text.setObjectName("patient_dob_text")
        self.patient_country_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_country_text.setGeometry(QtCore.QRect(200, 165, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.patient_country_text.setFont(font)
        self.patient_country_text.setObjectName("patient_country_text")
        self.patient_gender = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_gender.setGeometry(QtCore.QRect(280, 85, 111, 20))
        self.patient_gender.setObjectName("patient_gender")
        self.patient_blood_type = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_blood_type.setGeometry(QtCore.QRect(280, 105, 111, 20))
        self.patient_blood_type.setObjectName("patient_blood_type")
        self.patient_tcno = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_tcno.setGeometry(QtCore.QRect(280, 125, 111, 20))
        self.patient_tcno.setObjectName("patient_tcno")
        self.patient_country = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_country.setGeometry(QtCore.QRect(280, 165, 111, 20))
        self.patient_country.setObjectName("patient_country")
        self.patient_registiration_date = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_registiration_date.setGeometry(QtCore.QRect(80, 165, 113, 20))
        self.patient_registiration_date.setObjectName("patient_registiration_date")
        self.patient_name = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_name.setGeometry(QtCore.QRect(80, 85, 113, 20))
        self.patient_name.setObjectName("patient_name")
        self.patient_adress = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_adress.setGeometry(QtCore.QRect(80, 125, 113, 20))
        self.patient_adress.setObjectName("patient_adress")
        self.patient_surname = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_surname.setGeometry(QtCore.QRect(80, 105, 113, 20))
        self.patient_surname.setObjectName("patient_surname")
        self.patient_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_phone.setGeometry(QtCore.QRect(80, 145, 113, 20))
        self.patient_phone.setObjectName("patient_phone")
        self.patient_add_button = QtWidgets.QPushButton(self.centralwidget)
        self.patient_add_button.setGeometry(QtCore.QRect(20, 195, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.patient_add_button.setFont(font)
        self.patient_add_button.setObjectName("patient_add_button")
        self.muayene_ekle_text = QtWidgets.QLabel(self.centralwidget)
        self.muayene_ekle_text.setGeometry(QtCore.QRect(410, 51, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.muayene_ekle_text.setFont(font)
        self.muayene_ekle_text.setObjectName("muayene_ekle_text")
        self.hasta_id_text = QtWidgets.QLabel(self.centralwidget)
        self.hasta_id_text.setGeometry(QtCore.QRect(420, 90, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hasta_id_text.setFont(font)
        self.hasta_id_text.setObjectName("hasta_id_text")
        self.muayene_date_text = QtWidgets.QLabel(self.centralwidget)
        self.muayene_date_text.setGeometry(QtCore.QRect(420, 105, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.muayene_date_text.setFont(font)
        self.muayene_date_text.setObjectName("muayene_date_text")
        self.muayene_time_text = QtWidgets.QLabel(self.centralwidget)
        self.muayene_time_text.setGeometry(QtCore.QRect(420, 130, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.muayene_time_text.setFont(font)
        self.muayene_time_text.setObjectName("muayene_time_text")
        self.muayene_doctor_id_text = QtWidgets.QLabel(self.centralwidget)
        self.muayene_doctor_id_text.setGeometry(QtCore.QRect(420, 150, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.muayene_doctor_id_text.setFont(font)
        self.muayene_doctor_id_text.setObjectName("muayene_doctor_id_text")
        self.muayene_add_hasta_id = QtWidgets.QLineEdit(self.centralwidget)
        self.muayene_add_hasta_id.setGeometry(QtCore.QRect(520, 90, 111, 20))
        self.muayene_add_hasta_id.setObjectName("muayene_add_hasta_id")
        self.doctor_id = QtWidgets.QLineEdit(self.centralwidget)
        self.doctor_id.setGeometry(QtCore.QRect(520, 150, 111, 20))
        self.doctor_id.setObjectName("doctor_id")
        self.muayene_sil_text = QtWidgets.QLabel(self.centralwidget)
        self.muayene_sil_text.setGeometry(QtCore.QRect(880, 40, 81, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.muayene_sil_text.setFont(font)
        self.muayene_sil_text.setObjectName("muayene_sil_text")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(820, 90, 61, 111))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.muayene_id_text = QtWidgets.QLabel(self.centralwidget)
        self.muayene_id_text.setGeometry(QtCore.QRect(880, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.muayene_id_text.setFont(font)
        self.muayene_id_text.setObjectName("muayene_id_text")
        self.muayene_sil_muayene_id = QtWidgets.QLineEdit(self.centralwidget)
        self.muayene_sil_muayene_id.setGeometry(QtCore.QRect(860, 120, 131, 31))
        self.muayene_sil_muayene_id.setObjectName("muayene_sil_muayene_id")
        self.muayene_sil_button = QtWidgets.QPushButton(self.centralwidget)
        self.muayene_sil_button.setGeometry(QtCore.QRect(860, 160, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.muayene_sil_button.setFont(font)
        self.muayene_sil_button.setObjectName("muayene_sil_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(1200, 10, 71, 31))
        self.exit_button.setObjectName("exit_button")
        self.clear_all = QtWidgets.QPushButton(self.centralwidget)
        self.clear_all.setGeometry(QtCore.QRect(110, 195, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.clear_all.setFont(font)
        self.clear_all.setObjectName("clear_all")
        self.patient_get_info = QtWidgets.QPushButton(self.centralwidget)
        self.patient_get_info.setGeometry(QtCore.QRect(20, 235, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.patient_get_info.setFont(font)
        self.patient_get_info.setObjectName("patient_get_info")
        self.patient_info_update = QtWidgets.QPushButton(self.centralwidget)
        self.patient_info_update.setGeometry(QtCore.QRect(110, 235, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.patient_info_update.setFont(font)
        self.patient_info_update.setObjectName("patient_info_update")
        self.patient_id_text = QtWidgets.QLabel(self.centralwidget)
        self.patient_id_text.setGeometry(QtCore.QRect(200, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.patient_id_text.setFont(font)
        self.patient_id_text.setObjectName("patient_id_text")
        self.hasta_id = QtWidgets.QLabel(self.centralwidget)
        self.hasta_id.setGeometry(QtCore.QRect(290, 180, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hasta_id.setFont(font)
        self.hasta_id.setText("")
        self.hasta_id.setAlignment(QtCore.Qt.AlignCenter)
        self.hasta_id.setObjectName("hasta_id")
        self.muayene_ekle_button = QtWidgets.QPushButton(self.centralwidget)
        self.muayene_ekle_button.setGeometry(QtCore.QRect(420, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.muayene_ekle_button.setFont(font)
        self.muayene_ekle_button.setObjectName("muayene_ekle_button")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 520, 381, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.doktor_ekle_text = QtWidgets.QLabel(self.centralwidget)
        self.doktor_ekle_text.setGeometry(QtCore.QRect(10, 300, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doktor_ekle_text.setFont(font)
        self.doktor_ekle_text.setObjectName("doktor_ekle_text")
        self.doktor_ad_text = QtWidgets.QLabel(self.centralwidget)
        self.doktor_ad_text.setGeometry(QtCore.QRect(10, 340, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.doktor_ad_text.setFont(font)
        self.doktor_ad_text.setObjectName("doktor_ad_text")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 310, 381, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.doktor_soyad_text = QtWidgets.QLabel(self.centralwidget)
        self.doktor_soyad_text.setGeometry(QtCore.QRect(10, 360, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doktor_soyad_text.setFont(font)
        self.doktor_soyad_text.setObjectName("doktor_soyad_text")
        self.doktor_unvan_text = QtWidgets.QLabel(self.centralwidget)
        self.doktor_unvan_text.setGeometry(QtCore.QRect(10, 380, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doktor_unvan_text.setFont(font)
        self.doktor_unvan_text.setObjectName("doktor_unvan_text")
        self.doktor_cinsiyet_text = QtWidgets.QLabel(self.centralwidget)
        self.doktor_cinsiyet_text.setGeometry(QtCore.QRect(10, 400, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doktor_cinsiyet_text.setFont(font)
        self.doktor_cinsiyet_text.setObjectName("doktor_cinsiyet_text")
        self.doktor_dob = QtWidgets.QLabel(self.centralwidget)
        self.doktor_dob.setGeometry(QtCore.QRect(10, 420, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doktor_dob.setFont(font)
        self.doktor_dob.setObjectName("doktor_dob")
        self.doktor_ad_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.doktor_ad_edit.setGeometry(QtCore.QRect(110, 340, 113, 20))
        self.doktor_ad_edit.setObjectName("doktor_ad_edit")
        self.doktor_soyad_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.doktor_soyad_edit.setGeometry(QtCore.QRect(110, 360, 113, 20))
        self.doktor_soyad_edit.setObjectName("doktor_soyad_edit")
        self.doktor_unvan_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.doktor_unvan_edit.setGeometry(QtCore.QRect(110, 380, 113, 20))
        self.doktor_unvan_edit.setObjectName("doktor_unvan_edit")
        self.doktor_cinsiyet_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.doktor_cinsiyet_edit.setGeometry(QtCore.QRect(110, 400, 113, 20))
        self.doktor_cinsiyet_edit.setObjectName("doktor_cinsiyet_edit")
        self.doktor_dob_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.doktor_dob_edit.setGeometry(QtCore.QRect(110, 420, 113, 20))
        self.doktor_dob_edit.setObjectName("doktor_dob_edit")
        self.doktor_add_button = QtWidgets.QPushButton(self.centralwidget)
        self.doktor_add_button.setGeometry(QtCore.QRect(110, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.doktor_add_button.setFont(font)
        self.doktor_add_button.setObjectName("doktor_add_button")
        self.doktor_sil_text = QtWidgets.QLabel(self.centralwidget)
        self.doktor_sil_text.setGeometry(QtCore.QRect(260, 300, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doktor_sil_text.setFont(font)
        self.doktor_sil_text.setObjectName("doktor_sil_text")
        self.doktor_id_text = QtWidgets.QLabel(self.centralwidget)
        self.doktor_id_text.setGeometry(QtCore.QRect(260, 340, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.doktor_id_text.setFont(font)
        self.doktor_id_text.setObjectName("doktor_id_text")
        self.doktor_sil_id = QtWidgets.QLineEdit(self.centralwidget)
        self.doktor_sil_id.setGeometry(QtCore.QRect(240, 370, 131, 31))
        self.doktor_sil_id.setObjectName("doktor_sil_id")
        self.doktor_sil_button = QtWidgets.QPushButton(self.centralwidget)
        self.doktor_sil_button.setGeometry(QtCore.QRect(240, 410, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doktor_sil_button.setFont(font)
        self.doktor_sil_button.setObjectName("doktor_sil_button")
        self.ameliyat_ekle_text = QtWidgets.QLabel(self.centralwidget)
        self.ameliyat_ekle_text.setGeometry(QtCore.QRect(10, 510, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_ekle_text.setFont(font)
        self.ameliyat_ekle_text.setObjectName("ameliyat_ekle_text")
        self.ameliyat_turu_text = QtWidgets.QLabel(self.centralwidget)
        self.ameliyat_turu_text.setGeometry(QtCore.QRect(20, 540, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_turu_text.setFont(font)
        self.ameliyat_turu_text.setObjectName("ameliyat_turu_text")
        self.ameliyat_aciklama_text = QtWidgets.QLabel(self.centralwidget)
        self.ameliyat_aciklama_text.setGeometry(QtCore.QRect(20, 560, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_aciklama_text.setFont(font)
        self.ameliyat_aciklama_text.setObjectName("ameliyat_aciklama_text")
        self.ameliyat_ucret_text = QtWidgets.QLabel(self.centralwidget)
        self.ameliyat_ucret_text.setGeometry(QtCore.QRect(20, 595, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_ucret_text.setFont(font)
        self.ameliyat_ucret_text.setObjectName("ameliyat_ucret_text")
        self.ameliyat_hasta_id_text = QtWidgets.QLabel(self.centralwidget)
        self.ameliyat_hasta_id_text.setGeometry(QtCore.QRect(20, 610, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_hasta_id_text.setFont(font)
        self.ameliyat_hasta_id_text.setObjectName("ameliyat_hasta_id_text")
        self.ameliyat_doktor_id_text = QtWidgets.QLabel(self.centralwidget)
        self.ameliyat_doktor_id_text.setGeometry(QtCore.QRect(20, 635, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_doktor_id_text.setFont(font)
        self.ameliyat_doktor_id_text.setObjectName("ameliyat_doktor_id_text")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(150, 550, 231, 131))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ameliyat_turu = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.ameliyat_turu.setObjectName("ameliyat_turu")
        self.verticalLayout.addWidget(self.ameliyat_turu)
        self.ameliyat_aciklama = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.ameliyat_aciklama.setObjectName("ameliyat_aciklama")
        self.verticalLayout.addWidget(self.ameliyat_aciklama)
        self.ameliyat_ucret = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.ameliyat_ucret.setObjectName("ameliyat_ucret")
        self.verticalLayout.addWidget(self.ameliyat_ucret)
        self.ameliyat_hasta_id = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.ameliyat_hasta_id.setObjectName("ameliyat_hasta_id")
        self.verticalLayout.addWidget(self.ameliyat_hasta_id)
        self.ameliyat_doktor_id = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.ameliyat_doktor_id.setObjectName("ameliyat_doktor_id")
        self.verticalLayout.addWidget(self.ameliyat_doktor_id)
        self.ameliyat_ekle_button = QtWidgets.QPushButton(self.centralwidget)
        self.ameliyat_ekle_button.setGeometry(QtCore.QRect(150, 700, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_ekle_button.setFont(font)
        self.ameliyat_ekle_button.setObjectName("ameliyat_ekle_button")
        self.clear_all_doktor = QtWidgets.QPushButton(self.centralwidget)
        self.clear_all_doktor.setGeometry(QtCore.QRect(10, 450, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.clear_all_doktor.setFont(font)
        self.clear_all_doktor.setObjectName("clear_all_doktor")
        self.ameliyat_temizle_button = QtWidgets.QPushButton(self.centralwidget)
        self.ameliyat_temizle_button.setGeometry(QtCore.QRect(300, 700, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_temizle_button.setFont(font)
        self.ameliyat_temizle_button.setObjectName("ameliyat_temizle_button")
        self.hospital_managament_text = QtWidgets.QLabel(self.centralwidget)
        self.hospital_managament_text.setGeometry(QtCore.QRect(500, 290, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.hospital_managament_text.setFont(font)
        self.hospital_managament_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.hospital_managament_text.setObjectName("hospital_managament_text")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(410, 250, 851, 411))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.list_all_patient = QtWidgets.QPushButton(self.centralwidget)
        self.list_all_patient.setGeometry(QtCore.QRect(910, 670, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.list_all_patient.setFont(font)
        self.list_all_patient.setStyleSheet("")
        self.list_all_patient.setObjectName("list_all_patient")
        self.muayene_sonuc_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.muayene_sonuc_text_edit.setGeometry(QtCore.QRect(650, 120, 191, 81))
        self.muayene_sonuc_text_edit.setObjectName("muayene_sonuc_text_edit")
        self.muayene_sonucu_text = QtWidgets.QLabel(self.centralwidget)
        self.muayene_sonucu_text.setGeometry(QtCore.QRect(670, 49, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.muayene_sonucu_text.setFont(font)
        self.muayene_sonucu_text.setObjectName("muayene_sonucu_text")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(370, 90, 61, 111))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.muayene_sonuc_ekle_button = QtWidgets.QPushButton(self.centralwidget)
        self.muayene_sonuc_ekle_button.setGeometry(QtCore.QRect(650, 210, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.muayene_sonuc_ekle_button.setFont(font)
        self.muayene_sonuc_ekle_button.setObjectName("muayene_sonuc_ekle_button")
        self.muayeneSonuc_muayeneId = QtWidgets.QLineEdit(self.centralwidget)
        self.muayeneSonuc_muayeneId.setGeometry(QtCore.QRect(720, 90, 51, 21))
        self.muayeneSonuc_muayeneId.setObjectName("muayeneSonuc_muayeneId")
        self.muayene_sonuc_muayene_id_text = QtWidgets.QLabel(self.centralwidget)
        self.muayene_sonuc_muayene_id_text.setGeometry(QtCore.QRect(650, 90, 81, 16))
        self.muayene_sonuc_muayene_id_text.setObjectName("muayene_sonuc_muayene_id_text")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(870, 720, 371, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ameliyat_listele = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ameliyat_listele.setFont(font)
        self.ameliyat_listele.setObjectName("ameliyat_listele")
        self.horizontalLayout.addWidget(self.ameliyat_listele)
        self.muayene_listele = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.muayene_listele.setObjectName("muayene_listele")
        self.horizontalLayout.addWidget(self.muayene_listele)
        self.doktor_listele = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.doktor_listele.setObjectName("doktor_listele")
        self.horizontalLayout.addWidget(self.doktor_listele)
        self.muayene_sonuc_listele = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.muayene_sonuc_listele.setObjectName("muayene_sonuc_listele")
        self.horizontalLayout.addWidget(self.muayene_sonuc_listele)
        self.muayene_sonuc_getir_button = QtWidgets.QPushButton(self.centralwidget)
        self.muayene_sonuc_getir_button.setGeometry(QtCore.QRect(780, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.muayene_sonuc_getir_button.setFont(font)
        self.muayene_sonuc_getir_button.setObjectName("muayene_sonuc_getir_button")
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(1130, 10, 71, 31))
        self.export_button.setObjectName("export_button")
        self.muayene_update_button = QtWidgets.QPushButton(self.centralwidget)
        self.muayene_update_button.setGeometry(QtCore.QRect(490, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.muayene_update_button.setFont(font)
        self.muayene_update_button.setObjectName("muayene_update_button")
        self.muayene_sonucu_update_button = QtWidgets.QPushButton(self.centralwidget)
        self.muayene_sonucu_update_button.setGeometry(QtCore.QRect(710, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.muayene_sonucu_update_button.setFont(font)
        self.muayene_sonucu_update_button.setObjectName("muayene_sonucu_update_button")
        self.muayene_turu_text = QtWidgets.QLabel(self.centralwidget)
        self.muayene_turu_text.setGeometry(QtCore.QRect(420, 170, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.muayene_turu_text.setFont(font)
        self.muayene_turu_text.setObjectName("muayene_turu_text")
        self.muayene_turu = QtWidgets.QLineEdit(self.centralwidget)
        self.muayene_turu.setGeometry(QtCore.QRect(520, 170, 111, 20))
        self.muayene_turu.setObjectName("muayene_turu")
        self.deleted_records_button = QtWidgets.QPushButton(self.centralwidget)
        self.deleted_records_button.setGeometry(QtCore.QRect(90, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.deleted_records_button.setFont(font)
        self.deleted_records_button.setObjectName("deleted_records_button")
        self.patient_info_delete = QtWidgets.QPushButton(self.centralwidget)
        self.patient_info_delete.setGeometry(QtCore.QRect(200, 235, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.patient_info_delete.setFont(font)
        self.patient_info_delete.setObjectName("patient_info_delete")
        self.muayene_clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.muayene_clear_button.setGeometry(QtCore.QRect(560, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.muayene_clear_button.setFont(font)
        self.muayene_clear_button.setObjectName("muayene_clear_button")
        self.muayene_sonuc_clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.muayene_sonuc_clear_button.setGeometry(QtCore.QRect(780, 210, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.muayene_sonuc_clear_button.setFont(font)
        self.muayene_sonuc_clear_button.setObjectName("muayene_sonuc_clear_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1010, 70, 231, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("hosspital.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ameliyat_guncelle_button = QtWidgets.QPushButton(self.centralwidget)
        self.ameliyat_guncelle_button.setGeometry(QtCore.QRect(225, 700, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_guncelle_button.setFont(font)
        self.ameliyat_guncelle_button.setObjectName("ameliyat_guncelle_button")
        self.admin_yetki_button = QtWidgets.QPushButton(self.centralwidget)
        self.admin_yetki_button.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.admin_yetki_button.setFont(font)
        self.admin_yetki_button.setObjectName("admin_yetki_button")
        self.ameliyat_id_get = QtWidgets.QLineEdit(self.centralwidget)
        self.ameliyat_id_get.setGeometry(QtCore.QRect(10, 709, 50, 21))
        self.ameliyat_id_get.setObjectName("ameliyat_id_get")
        self.ameliyat_get_info = QtWidgets.QPushButton(self.centralwidget)
        self.ameliyat_get_info.setGeometry(QtCore.QRect(70, 700, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_get_info.setFont(font)
        self.ameliyat_get_info.setObjectName("ameliyat_get_info")
        self.ameliyat_id_text = QtWidgets.QLabel(self.centralwidget)
        self.ameliyat_id_text.setGeometry(QtCore.QRect(6, 689, 77, 25))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.ameliyat_id_text.setFont(font)
        self.ameliyat_id_text.setObjectName("ameliyat_id_text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1431, 841))
        self.label_2.setMaximumSize(QtCore.QSize(1431, 16777215))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("a-min.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.backup_button = QtWidgets.QPushButton(self.centralwidget)
        self.backup_button.setGeometry(QtCore.QRect(1130, 40, 71, 31))
        self.backup_button.setObjectName("backup_button")
        self.restore_button = QtWidgets.QPushButton(self.centralwidget)
        self.restore_button.setGeometry(QtCore.QRect(1200, 40, 71, 31))
        self.restore_button.setObjectName("restore_button")
        self.patient_dob = QtWidgets.QLineEdit(self.centralwidget)
        self.patient_dob.setGeometry(QtCore.QRect(280, 145, 111, 20))
        self.patient_dob.setObjectName("patient_dob")
        self.date_of_muayene = QtWidgets.QLineEdit(self.centralwidget)
        self.date_of_muayene.setGeometry(QtCore.QRect(520, 110, 111, 20))
        self.date_of_muayene.setObjectName("date_of_muayene")
        self.muayene_time = QtWidgets.QLineEdit(self.centralwidget)
        self.muayene_time.setGeometry(QtCore.QRect(520, 130, 111, 20))
        self.muayene_time.setObjectName("muayene_time")
        self.label_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.hasta_add_text.raise_()
        self.line.raise_()
        self.patient_name_text.raise_()
        self.patient_surname_text.raise_()
        self.patient_adress_text.raise_()
        self.patient_phone_text.raise_()
        self.patient_tcno_text.raise_()
        self.patient_gender_text.raise_()
        self.patient_registiration_date_text.raise_()
        self.patient_blood_type_text.raise_()
        self.patient_dob_text.raise_()
        self.patient_country_text.raise_()
        self.patient_gender.raise_()
        self.patient_blood_type.raise_()
        self.patient_tcno.raise_()
        self.patient_country.raise_()
        self.patient_registiration_date.raise_()
        self.patient_name.raise_()
        self.patient_adress.raise_()
        self.patient_surname.raise_()
        self.patient_phone.raise_()
        self.patient_add_button.raise_()
        self.muayene_ekle_text.raise_()
        self.hasta_id_text.raise_()
        self.muayene_date_text.raise_()
        self.muayene_time_text.raise_()
        self.muayene_doctor_id_text.raise_()
        self.muayene_add_hasta_id.raise_()
        self.doctor_id.raise_()
        self.muayene_sil_text.raise_()
        self.line_10.raise_()
        self.muayene_id_text.raise_()
        self.muayene_sil_muayene_id.raise_()
        self.muayene_sil_button.raise_()
        self.exit_button.raise_()
        self.clear_all.raise_()
        self.patient_get_info.raise_()
        self.patient_info_update.raise_()
        self.patient_id_text.raise_()
        self.hasta_id.raise_()
        self.muayene_ekle_button.raise_()
        self.line_4.raise_()
        self.doktor_ekle_text.raise_()
        self.doktor_ad_text.raise_()
        self.line_5.raise_()
        self.doktor_soyad_text.raise_()
        self.doktor_unvan_text.raise_()
        self.doktor_cinsiyet_text.raise_()
        self.doktor_dob.raise_()
        self.doktor_ad_edit.raise_()
        self.doktor_soyad_edit.raise_()
        self.doktor_unvan_edit.raise_()
        self.doktor_cinsiyet_edit.raise_()
        self.doktor_dob_edit.raise_()
        self.doktor_add_button.raise_()
        self.doktor_sil_text.raise_()
        self.doktor_id_text.raise_()
        self.doktor_sil_id.raise_()
        self.doktor_sil_button.raise_()
        self.ameliyat_ekle_text.raise_()
        self.ameliyat_turu_text.raise_()
        self.ameliyat_aciklama_text.raise_()
        self.ameliyat_ucret_text.raise_()
        self.ameliyat_hasta_id_text.raise_()
        self.ameliyat_doktor_id_text.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.ameliyat_ekle_button.raise_()
        self.clear_all_doktor.raise_()
        self.ameliyat_temizle_button.raise_()
        self.hospital_managament_text.raise_()
        self.tableWidget.raise_()
        self.list_all_patient.raise_()
        self.muayene_sonuc_text_edit.raise_()
        self.muayene_sonucu_text.raise_()
        self.line_11.raise_()
        self.muayene_sonuc_ekle_button.raise_()
        self.muayeneSonuc_muayeneId.raise_()
        self.muayene_sonuc_muayene_id_text.raise_()
        self.horizontalLayoutWidget.raise_()
        self.muayene_sonuc_getir_button.raise_()
        self.export_button.raise_()
        self.muayene_update_button.raise_()
        self.muayene_sonucu_update_button.raise_()
        self.muayene_turu_text.raise_()
        self.muayene_turu.raise_()
        self.deleted_records_button.raise_()
        self.patient_info_delete.raise_()
        self.muayene_clear_button.raise_()
        self.muayene_sonuc_clear_button.raise_()
        self.label.raise_()
        self.ameliyat_guncelle_button.raise_()
        self.admin_yetki_button.raise_()
        self.ameliyat_id_get.raise_()
        self.ameliyat_get_info.raise_()
        self.ameliyat_id_text.raise_()
        self.backup_button.raise_()
        self.restore_button.raise_()
        self.patient_dob.raise_()
        self.date_of_muayene.raise_()
        self.muayene_time.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHasta = QtWidgets.QAction(MainWindow)
        self.actionHasta.setObjectName("actionHasta")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.muayene_id_search_text.setText(_translate("MainWindow", "Hasta ID"))
        self.hasta_id_arama_button.setText(_translate("MainWindow", "Ara"))
        self.hasta_ad_search_text.setText(_translate("MainWindow", "Hasta Ad"))
        self.hasta_ad_arama_button.setText(_translate("MainWindow", "Ara"))
        self.hasta_tcno_search_text.setText(_translate("MainWindow", "Hasta Tc No"))
        self.hasta_tcno_arama_button.setText(_translate("MainWindow", "Ara"))
        self.hasta_add_text.setText(_translate("MainWindow", "Hasta Ekle"))
        self.patient_name_text.setText(_translate("MainWindow", "Ad"))
        self.patient_surname_text.setText(_translate("MainWindow", "Soyad"))
        self.patient_adress_text.setText(_translate("MainWindow", "Adres"))
        self.patient_phone_text.setText(_translate("MainWindow", "Cep Tel"))
        self.patient_tcno_text.setText(_translate("MainWindow", "TcNo"))
        self.patient_gender_text.setText(_translate("MainWindow", "Cinsiyet"))
        self.patient_registiration_date_text.setText(_translate("MainWindow", "Kayit Tar."))
        self.patient_blood_type_text.setText(_translate("MainWindow", "Kan Grubu"))
        self.patient_dob_text.setText(_translate("MainWindow", "Dogum Tarihi"))
        self.patient_country_text.setText(_translate("MainWindow", "Dogum Yeri"))
        self.patient_add_button.setText(_translate("MainWindow", "HASTA EKLE"))
        self.muayene_ekle_text.setText(_translate("MainWindow", "Muayene Ekle"))
        self.hasta_id_text.setText(_translate("MainWindow", "Hasta ID"))
        self.muayene_date_text.setText(_translate("MainWindow", "Muayene Tarihi"))
        self.muayene_time_text.setText(_translate("MainWindow", "Muayene Saati"))
        self.muayene_doctor_id_text.setText(_translate("MainWindow", "Doktor ID"))
        self.muayene_sil_text.setText(_translate("MainWindow", "Muayene Sil"))
        self.muayene_id_text.setText(_translate("MainWindow", "Muayene ID"))
        self.muayene_sil_button.setText(_translate("MainWindow", "MUAYENE SIL"))
        self.exit_button.setText(_translate("MainWindow", "EXIT"))
        self.clear_all.setText(_translate("MainWindow", "TEMIZLE"))
        self.patient_get_info.setText(_translate("MainWindow", "GET INFO"))
        self.patient_info_update.setText(_translate("MainWindow", "GUNCELLE"))
        self.patient_id_text.setText(_translate("MainWindow", "Hasta ID"))
        self.muayene_ekle_button.setText(_translate("MainWindow", "EKLE"))
        self.doktor_ekle_text.setText(_translate("MainWindow", "Doktor Ekle"))
        self.doktor_ad_text.setText(_translate("MainWindow", "Doktor Ad           :"))
        self.doktor_soyad_text.setText(_translate("MainWindow", "Doktor Soyad"))
        self.doktor_unvan_text.setText(_translate("MainWindow", "Unvan"))
        self.doktor_cinsiyet_text.setText(_translate("MainWindow", "Cinsiyet"))
        self.doktor_dob.setText(_translate("MainWindow", "Dogum Tarihi"))
        self.doktor_add_button.setText(_translate("MainWindow", "DOKTOR EKLE"))
        self.doktor_sil_text.setText(_translate("MainWindow", "Doktor Sil"))
        self.doktor_id_text.setText(_translate("MainWindow", "DOKTOR ID"))
        self.doktor_sil_button.setText(_translate("MainWindow", "DOKTOR SIL"))
        self.ameliyat_ekle_text.setText(_translate("MainWindow", "Ameliyat Ekle"))
        self.ameliyat_turu_text.setText(_translate("MainWindow", "Ameliyat Turu"))
        self.ameliyat_aciklama_text.setText(_translate("MainWindow", "Ameliyat Aciklamasi"))
        self.ameliyat_ucret_text.setText(_translate("MainWindow", "Ameliyat Ucreti"))
        self.ameliyat_hasta_id_text.setText(_translate("MainWindow", "Hasta ID"))
        self.ameliyat_doktor_id_text.setText(_translate("MainWindow", "Doktor ID"))
        self.ameliyat_ekle_button.setText(_translate("MainWindow", "EKLE"))
        self.clear_all_doktor.setText(_translate("MainWindow", "TEMIZLE"))
        self.ameliyat_temizle_button.setText(_translate("MainWindow", "TEMIZLE"))
        self.hospital_managament_text.setText(_translate("MainWindow", "HASTANE YONETIMI"))
        self.list_all_patient.setText(_translate("MainWindow", "TUM HASTALARI LISTELE"))
        self.muayene_sonucu_text.setText(_translate("MainWindow", "Muayene Sonucu"))
        self.muayene_sonuc_ekle_button.setText(_translate("MainWindow", "EKLE"))
        self.muayene_sonuc_muayene_id_text.setText(_translate("MainWindow", "Muayene ID"))
        self.ameliyat_listele.setText(_translate("MainWindow", "Ameliyat"))
        self.muayene_listele.setText(_translate("MainWindow", "Muayene"))
        self.doktor_listele.setText(_translate("MainWindow", "Doktor"))
        self.muayene_sonuc_listele.setText(_translate("MainWindow", "Muayene Sonuc"))
        self.muayene_sonuc_getir_button.setText(_translate("MainWindow", "GETIR"))
        self.export_button.setText(_translate("MainWindow", "EXPORT"))
        self.muayene_update_button.setText(_translate("MainWindow", "GUNCELLE"))
        self.muayene_sonucu_update_button.setText(_translate("MainWindow", "GUNCELLE"))
        self.muayene_turu_text.setText(_translate("MainWindow", "Muayene Turu"))
        self.deleted_records_button.setText(_translate("MainWindow", "Deleted Records"))
        self.patient_info_delete.setText(_translate("MainWindow", "DELETE"))
        self.muayene_clear_button.setText(_translate("MainWindow", "TEMIZLE"))
        self.muayene_sonuc_clear_button.setText(_translate("MainWindow", "TEMIZLE"))
        self.ameliyat_guncelle_button.setText(_translate("MainWindow", "GUNCELLE"))
        self.admin_yetki_button.setText(_translate("MainWindow", "Yetkilendir"))
        self.ameliyat_get_info.setText(_translate("MainWindow", "GET INFO"))
        self.ameliyat_id_text.setText(_translate("MainWindow", "Ameliyat ID"))
        self.backup_button.setText(_translate("MainWindow", "BACKUP"))
        self.restore_button.setText(_translate("MainWindow", "RESTORE"))
        self.actionHasta.setText(_translate("MainWindow", "Hasta"))
        self.patient_registiration_date.setReadOnly(TRUE)
        self.date_of_muayene.setReadOnly(TRUE)
        self.muayene_time.setReadOnly(TRUE)
        self.patient_registiration_date.setText("Otomatik Atanir")
        self.date_of_muayene.setText("Otomatik Atanir")
        self.muayene_time.setText("Otomatik Atanir")
        self.patient_tcno.setMaxLength(11)
        self.patient_phone.setMaxLength(10)
#Button Clicks        
        self.patient_add_button.clicked.connect(self.hasta_ekleme)
        self.patient_add_button.clicked.connect(self.hastaekle_mesaj)
        self.patient_add_button.clicked.connect(self.show_patients)
        self.list_all_patient.clicked.connect(self.satir)
        self.list_all_patient.clicked.connect(self.show_patients)
        self.muayene_sil_button.clicked.connect(self.deleteMuayene)
        self.muayene_sil_button.clicked.connect(self.muayene_id_text_clear)
        self.muayene_sil_button.clicked.connect(self.muayene_delete_messagebox)
        self.clear_all.clicked.connect(self.clearData)
        self.patient_get_info.clicked.connect(self.patient_text_aktar)
        self.clear_all_doktor.clicked.connect(self.clearDataDoctor)
        self.doktor_add_button.clicked.connect(self.doktor_ekleme)
        self.doktor_add_button.clicked.connect(self.doktor_ekle_messagebox)
        self.doktor_add_button.clicked.connect(self.show_doctor)
        self.doktor_sil_button.clicked.connect(self.deleteDoktor)
        self.doktor_sil_button.clicked.connect(self.doktor_delete_messagebox)
        self.doktor_sil_button.clicked.connect(self.show_doctor)
        self.doktor_listele.clicked.connect(self.show_doctor)
        self.muayene_listele.clicked.connect(self.show_muayene)
        self.muayene_sonuc_listele.clicked.connect(self.show_muayeneSonuc)
        self.ameliyat_listele.clicked.connect(self.show_ameliyat)
        self.patient_info_update.clicked.connect(self.hasta_update)
        self.patient_info_update.clicked.connect(self.hasta_update_mesaj)
        self.patient_info_update.clicked.connect(self.show_patients)
        self.hasta_tcno_arama_button.clicked.connect(self.hasta_tcno_search)
        self.hasta_ad_arama_button.clicked.connect(self.hasta_isim_search)
        self.hasta_id_arama_button.clicked.connect(self.hasta_muayene_id_search)
        self.patient_info_delete.clicked.connect(self.hasta_delete)
        self.patient_info_delete.clicked.connect(self.hasta_delete_message_box)
        self.muayene_ekle_button.clicked.connect(self.muayene_ekle)
        self.muayene_ekle_button.clicked.connect(self.muayene_ekle_messagebox)
        self.muayene_ekle_button.clicked.connect(self.show_muayene)
        self.patient_info_delete.clicked.connect(self.show_patients)
        self.muayene_sil_button.clicked.connect(self.show_muayene)
        self.ameliyat_ekle_button.clicked.connect(self.ameliyat_ekle)
        self.muayene_sonuc_ekle_button.clicked.connect(self.muayene_sonuc_ekle)
        self.ameliyat_ekle_button.clicked.connect(self.ameliyat_ekle_messagebox)
        self.ameliyat_ekle_button.clicked.connect(self.show_ameliyat)
        self.ameliyat_temizle_button.clicked.connect(self.ameliyat_text_clear)        
        self.muayene_sonuc_getir_button.clicked.connect(self.muayene_get_info)
        self.muayene_update_button.clicked.connect(self.muayene_update)
        self.muayene_update_button.clicked.connect(self.muayene_update_messagebox)
        self.muayene_update_button.clicked.connect(self.show_muayene)
        self.muayene_sonucu_update_button.clicked.connect(self.muayene_sonuc_update)
        self.muayene_sonuc_getir_button.clicked.connect(self.muayene_sonuc_get_info)
        self.muayene_sonuc_clear_button.clicked.connect(self.muayene_sonuc_text_clear)
        self.muayene_clear_button.clicked.connect(self.muayene_clear)
        self.ameliyat_get_info.clicked.connect(self.ameliyat_gett_info)
        self.ameliyat_guncelle_button.clicked.connect(self.ameliyat_update)
        self.ameliyat_guncelle_button.clicked.connect(self.show_ameliyat)
        self.ameliyat_guncelle_button.clicked.connect(self.ameliyat_update_messagebox)
        self.deleted_records_button.clicked.connect(self.deleted_records_list)
        self.muayene_sonuc_ekle_button.clicked.connect(self.muayene_sonuc_ekle_messagebox)
        self.muayene_sonuc_ekle_button.clicked.connect(self.show_muayeneSonuc)
        self.muayene_sonucu_update_button.clicked.connect(self.muayene_sonuc_guncelle_messagebox)
        self.muayene_sonucu_update_button.clicked.connect(self.show_muayeneSonuc)
        self.admin_yetki_button.clicked.connect(self.yetki_page) 
        self.backup_button.clicked.connect(self.get_backup)
        self.backup_button.clicked.connect(self.backup_messagebox)
        self.backup_button.clicked.connect(self.backup_open_folder)          
        self.restore_button.clicked.connect(self.restore_backup)
        self.exit_button.clicked.connect(self.exit)        
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
