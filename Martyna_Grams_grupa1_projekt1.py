# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:54:04 2019

@author: Martyna
"""

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QGridLayout, QColorDialog, QMessageBox, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt
import numpy as np

class Window(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        
        self.button = QPushButton('Rysuj', self)
        self.button.setEnabled(False)
        self.clrChoose = QPushButton('Wybierz kolor', self)
        self.clrChoose.setEnabled(False)
        self.crossPoint = QPushButton('Oblicz punkt przecięcia', self)
        self.saveButton = QPushButton('Zapisz punkty', self)
        self.saveButton.setEnabled(False)
        self.openButton = QPushButton('Wczytaj punkty', self)
        self.clearButton = QPushButton('Wyczyść', self)
        self.x1label = QLabel("X1", self)
        self.x1Edit = QLineEdit()
        self.y1label = QLabel("Y1", self)
        self.y1Edit = QLineEdit()
        self.x2label = QLabel("X2", self)
        self.x2Edit = QLineEdit()
        self.y2label = QLabel("Y2", self)
        self.y2Edit = QLineEdit()
        self.x3label = QLabel("X3", self)
        self.x3Edit = QLineEdit()
        self.y3label = QLabel("Y3", self)
        self.y3Edit = QLineEdit()
        self.x4label = QLabel("X4", self)
        self.x4Edit = QLineEdit()
        self.y4label = QLabel("Y4", self)
        self.y4Edit = QLineEdit()
        self.xplabel = QLabel("XP", self)
        self.xpEdit = QLineEdit()
        self.yplabel = QLabel("YP", self)
        self.ypEdit = QLineEdit()
        self.desEdit = QLineEdit()
        self.xpEdit.setReadOnly(True)
        self.ypEdit.setReadOnly(True)
        self.desEdit.setReadOnly(True)
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        # ladne ustawienie i wysrodkowanie
        layout =  QGridLayout(self)
        
        layout.addWidget(self.x1label, 1, 0)
        layout.addWidget(self.x1Edit, 1, 1)
        layout.addWidget(self.y1label, 2, 0)
        layout.addWidget(self.y1Edit, 2, 1)
        layout.addWidget(self.x2label, 1, 3)
        layout.addWidget(self.x2Edit, 1, 4)
        layout.addWidget(self.y2label, 2, 3)
        layout.addWidget(self.y2Edit, 2, 4)
        layout.addWidget(self.x3label, 1, 5)
        layout.addWidget(self.x3Edit, 1, 6)
        layout.addWidget(self.y3label, 2, 5)
        layout.addWidget(self.y3Edit, 2, 6)
        layout.addWidget(self.x4label, 1, 7)
        layout.addWidget(self.x4Edit, 1, 8)
        layout.addWidget(self.y4label, 2, 7)
        layout.addWidget(self.y4Edit, 2, 8)
        layout.addWidget(self.xplabel, 6,0)
        layout.addWidget(self.xpEdit, 6,1)
        layout.addWidget(self.yplabel, 6,3)
        layout.addWidget(self.ypEdit, 6,4)
        layout.addWidget(self.desEdit, 6, 5, 1,-1)
        
        layout.addWidget(self.clearButton, 3, 1, 1, -1)
        layout.addWidget(self.canvas, 4, 1, 1, -1)
        layout.addWidget(self.crossPoint, 5, 1, 1, -1)
        layout.addWidget(self.button, 7, 1, 1, 4)
        layout.addWidget(self.clrChoose, 7, 5, 1, -1)
        layout.addWidget(self.openButton, 8, 1, 1, 4)
        layout.addWidget(self.saveButton, 8, 5, 1, -1)
        
        # połączenie przycisku (signal) z akcją (slot)
        
        self.clrChoose.clicked.connect(self.handleButton2)
        self.crossPoint.clicked.connect(self.crossPointf)
        self.button.clicked.connect(self.handleButton)
        self.openButton.clicked.connect(self.wczytajPKT)
        self.saveButton.clicked.connect(self.zapiszPKT)
        self.clearButton.clicked.connect(self.wyczysc)
        
    def podaj(self,lineE):
        if lineE.text()=="":
            return "brak"
        try:
            w=float(lineE.text())
            #lineE.setText(str(round(w,3)))
        except ValueError:
            msg_err = QMessageBox()
            msg_err.setWindowTitle("Komunikat")
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText("Podana wartość %s jest niepoprawna" % lineE.text())
            msg_err.exec_()
            self.figure.clear()
            self.canvas.draw()
            return None
        return w

    def podaj_mini(self,lineE):
        if lineE.text()=="":
            return "brak"
        try:
            w=float(lineE.text())
        except ValueError:
            return None
        return w              
    
    def wyczysc(self):
        self.x1Edit.clear()
        self.y1Edit.clear()
        self.x2Edit.clear()
        self.y2Edit.clear()
        self.x3Edit.clear()
        self.y3Edit.clear()
        self.x4Edit.clear()
        self.y4Edit.clear()
        self.xpEdit.clear()
        self.ypEdit.clear()
        self.desEdit.clear()
        self.figure.clear()
        self.canvas.draw()
        
    def wczytajPKT(self):
        otworz_plik=QFileDialog.getOpenFileName(self, 'Wczytaj plik', '', 'Plik tekstowy (*.txt)')
        if otworz_plik[0]:
            f = open(otworz_plik[0],'r')
            with f:
                l=[]
                for line in f.readlines():
                    l+=line.split('\t')
                self.x1Edit.setText(l[0].strip().replace('\n', ''))
                self.y1Edit.setText(l[1].strip().replace('\n', ''))
                self.x2Edit.setText(l[2].strip().replace('\n', ''))
                self.y2Edit.setText(l[3].strip().replace('\n', ''))
                self.x3Edit.setText(l[4].strip().replace('\n', ''))
                self.y3Edit.setText(l[5].strip().replace('\n', ''))
                self.x4Edit.setText(l[6].strip().replace('\n', ''))
                self.y4Edit.setText(l[7].strip().replace('\n', ''))    
    
    def zapiszMM(self, lineE):
        if lineE.text()=='brak':
            return lineE.text()
        elif lineE.text()=='':
            msg_err = QMessageBox()
            msg_err.setWindowTitle("Komunikat")
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText("Brak wartości")
            msg_err.exec_()
        else:
            w=round(float(lineE.text()),3)
            return '{:.3f}'.format(w)
        
    def zapiszPKT(self):
        nowy_plik=QFileDialog.getSaveFileName(self, 'Zapisz plik', '', 'Plik tekstowy (*.txt)')
        if nowy_plik[0]:
            f = open(nowy_plik[0], 'w')
            with f:
                width=10
                f.write('{}\t{}\t{}'.format('Pkt'.ljust(5),'X'.ljust(width),'Y'.ljust(width))+'\n')
                f.write('{}\t{}\t{}'.format('1'.ljust(5),self.zapiszMM(self.x1Edit).ljust(width),self.zapiszMM(self.y1Edit).ljust(width)+'\n'))
                f.write('{}\t{}\t{}'.format('2'.ljust(5),self.zapiszMM(self.x2Edit).ljust(width),self.zapiszMM(self.y2Edit).ljust(width)+'\n'))
                f.write('{}\t{}\t{}'.format('3'.ljust(5),self.zapiszMM(self.x3Edit).ljust(width),self.zapiszMM(self.y3Edit).ljust(width)+'\n'))
                f.write('{}\t{}\t{}'.format('4'.ljust(5),self.zapiszMM(self.x4Edit).ljust(width),self.zapiszMM(self.y4Edit).ljust(width)+'\n'))
                f.write('{}\t{}\t{}'.format('P'.ljust(5),self.zapiszMM(self.xpEdit).ljust(width),self.ypEdit.text().ljust(width)+'\n'))

    def blizszy(self, pkt, pkt_lista):
        dyst=999999999
        for i in pkt_lista:
            dyst2=np.linalg.norm(pkt-i)
            if dyst2 <= dyst:
                dyst=dyst2
                b_pkt=i
        return b_pkt
    
    def handleButton(self):
        self.crossPointf()
        self.rysuj2()
        
    def clrChoosef(self):
        color1=QColorDialog.getColor()
        color2=QColorDialog.getColor()
        if color1.isValid() and color2.isValid():
                self.rysuj2(color1.name(),color2.name())
        else:
                pass
    def handleButton2(self):
        self.crossPointf()
        self.clrChoosef()
            
    def crossPointf(self):
        listXY=[[self.podaj(self.x1Edit),self.podaj(self.y1Edit)],[self.podaj(self.x2Edit),self.podaj(self.y2Edit)],[self.podaj(self.x3Edit),self.podaj(self.y3Edit)],[self.podaj(self.x4Edit),self.podaj(self.y4Edit)]]
        if any(i=="brak" for i in listXY[0]+listXY[1]+listXY[2]+listXY[3]):
            msg_err = QMessageBox()
            msg_err.setWindowTitle("Komunikat")
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText("Nie podano wszystkich wartości")
            msg_err.exec_()
        
        elif not (any(i is None for i in listXY[0]+listXY[1]+listXY[2]+listXY[3])):
            XY=np.array(listXY)
        
            deltaAC=XY[2]-XY[0]
            deltaCD=XY[3]-XY[2]
            deltaAB=XY[1]-XY[0]
        
            M=deltaAB[0]*deltaCD[1]-deltaAB[1]*deltaCD[0]
        
            if M==0:
                self.xpEdit.setText("brak")
                self.ypEdit.setText("brak")
                self.desEdit.setText("Odcinki są równoległe")   
            else:
                t1=(deltaAC[0]*deltaCD[1]-deltaAC[1]*deltaCD[0])/M
                t2=(deltaAC[0]*deltaAB[1]-deltaAC[1]*deltaAB[0])/M

                XP=XY[0][0]+t1*deltaAB[0]
                YP=XY[0][1]+t1*deltaAB[1]

                self.xpEdit.setText(str(round(XP,3)))
                self.ypEdit.setText(str(round(YP,3)))
        
                if (0<=t1<=1) and (0<=t2<=1):
                    self.desEdit.setText("P na przecięciu")
            
                elif 0 <= t1 <=1:
                    self.desEdit.setText("P na przedłużeniu drugiego odcinka")
        
                elif 0 <= t2 <=1:
                    self.desEdit.setText("P na przedłużeniu pierwszego odcinka")
                
                else:
                    self.desEdit.setText("P na przedłużeniu obu odcinków")

                self.figure.clear()
                self.canvas.draw()
            self.button.setEnabled(True)
            self.clrChoose.setEnabled(True)
            self.saveButton.setEnabled(True)
            self.xpEdit.setReadOnly(True)
            self.ypEdit.setReadOnly(True)
            self.desEdit.setReadOnly(True)
                
    def rysuj2(self, clr1='r', clr2='b'):
        XY=np.array([[self.podaj_mini(self.x1Edit),self.podaj_mini(self.y1Edit)],[self.podaj_mini(self.x2Edit),self.podaj_mini(self.y2Edit)],[self.podaj_mini(self.x3Edit),self.podaj_mini(self.y3Edit)],[self.podaj_mini(self.x4Edit),self.podaj_mini(self.y4Edit)]])
        XP=self.podaj_mini(self.xpEdit)
        YP=self.podaj_mini(self.ypEdit)
        l=XY.tolist()
        
        if any(i=="brak" for i in [self.xpEdit.text(),self.ypEdit.text()]):
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot([XY[0][0],XY[1][0]], [XY[0][1],XY[1][1]],color=clr1)
            ax.plot([XY[2][0],XY[3][0]], [XY[2][1],XY[3][1]], color=clr2)
            self.canvas.draw()
            
        elif not (any(i is None for i in l[0]+l[1]+l[2]+l[3]+[XP,YP]) or any(i=="brak" for i in l[0]+l[1]+l[2]+l[3])):
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot([XY[0][0],XY[1][0]], [XY[0][1],XY[1][1]],color=clr1)
            ax.plot([XY[2][0],XY[3][0]], [XY[2][1],XY[3][1]], color=clr2)
            ax.plot(XP, YP, 'o', color='black')
            
            blizszy12=self.blizszy(np.array([XP,YP]),XY[:2])
            blizszy34=self.blizszy(np.array([XP,YP]),XY[2:])
            
            if self.desEdit.text()=="P na przedłużeniu obu odcinków":
                ax.plot((blizszy12[0],XP),(blizszy12[1],YP),'--', color='grey', dashes=(3,6))
                ax.plot((blizszy34[0],XP),(blizszy34[1],YP),'--', color='grey', dashes=(3,6))
            if self.desEdit.text()=="P na przedłużeniu pierwszego odcinka":
                ax.plot((blizszy12[0],XP),(blizszy12[1],YP),'--', color='grey', dashes=(3,6))
            if self.desEdit.text()=="P na przedłużeniu drugiego odcinka":
                ax.plot((blizszy34[0],XP),(blizszy34[1],YP),'--', color='grey', dashes=(3,6))
            self.canvas.draw()
            
            
        elif any(i=="brak" for i in XY.tolist()):
            msg_err = QMessageBox()
            msg_err.setWindowTitle("Komunikat")
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText("Nie podano wszystkich wartości")
            msg_err.exec_()
            self.figure.clear()
            self.canvas.draw()

if __name__ == '__main__':
    if not QApplication.instance():
        app=QApplication(sys.argv)
        app.aboutToQuit.connect(app.deleteLater)
    else:
        app=QApplication.instance()

    
    window = Window()
    window.setWindowTitle("Wyznacz punkt przecięcia")
    window.show()
    app.exec_()
