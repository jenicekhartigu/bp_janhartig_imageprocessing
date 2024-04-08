import numpy as np
import cv2 as cv

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image


import globalFunc

from PIL import ImageQt


operationBtns = []
functionalAreas = []
logDisplay = []

inputImage = []

selectedColorDict = {}
selectedColorPILDict = {}

def imgToPixmap(image):
    im2 = image.convert("RGBA")
    data = im2.tobytes("raw", "BGRA")
    qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap

def tophatWidgetInit(disAreas, logDisp):
    for i in disAreas:
        functionalAreas.append(i)
        
    for i in logDisp:
        logDisplay.append(i)
        
    try:
        pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
        fromArray = np.asarray(pixmapImage)
        inputImage.append(fromArray)

    except:
        globalFunc.logDialog("WARNING: Není načten obrázek")    
    
        
    def iterationsSliderChange():
        sender = QObject().sender()
        if sender.objectName() == "iterations":
            tophatExecution(sender.value(),sliderMatrixSize.value())
        if sender.objectName() == "matrixSize":
            tophatExecution(sliderIterations.value(),sender.value())
                
        return None
    
    def buttonChange():
        tophatExecution(sliderIterations.value(),sliderMatrixSize.value())
    
    def getCheckedButton():
        return radioBtnGroup.checkedId()
    
    def tophatExecution(iterations, size):
        if getCheckedButton() == -3:
            kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(size,size))
        elif getCheckedButton() == -4:
            kernel = cv.getStructuringElement(cv.MORPH_CROSS,(size,size))
        else:
            kernel = cv.getStructuringElement(cv.MORPH_RECT,(size,size))
        
        try:
            tophatArray = cv.morphologyEx(inputImage[-1],cv.MORPH_TOPHAT,kernel, iterations = iterations)
            
            tophatImg = Image.fromarray(tophatArray, "RGB")
                    
            functionalAreas[2].setPixmap(imgToPixmap(tophatImg))
        except:
            globalFunc.logDialog("ERR: Operace tophat nemuze byt provedena")
            
        return None
        
    def setToDefault():
        square.setChecked(True)
        sliderIterations.setValue(0)
        return None
    
    def saveChanges():
        globalFunc.addImageDict("tophat")
        return None
    
    #LAYOUT 
    tophatWidget = QWidget(objectName = "tophat")
    tophatWidgetLayout = QGridLayout()
    
    tophatSettingBox = QBoxLayout(2)
    
    tophatSettingBox.addWidget(QLabel("Velikost matice pro operaci tophat"))
    
    sliderMatrixSize = QSlider()
    sliderMatrixSize = QSlider(Qt.Horizontal, objectName = "matrixSize")
    sliderMatrixSize.setMinimum(1)
    sliderMatrixSize.setMaximum(25)
    sliderMatrixSize.setTickInterval(1)
    sliderMatrixSize.setTickPosition(QSlider.TicksBelow)
    sliderMatrixSize.valueChanged.connect(iterationsSliderChange)
    
    tophatSettingBox.addWidget(sliderMatrixSize)
    
    tophatSettingBox.addWidget(QLabel("Počet iterací pro operaci tophat (rozdíl mezi vstupním obrazem a otevřením)"))
    
    sliderIterations = QSlider()
    sliderIterations = QSlider(Qt.Horizontal, objectName = "iterations")
    sliderIterations.setMinimum(0)
    sliderIterations.setMaximum(10)
    sliderIterations.setTickInterval(1)
    sliderIterations.setTickPosition(QSlider.TicksBelow)
    sliderIterations.valueChanged.connect(iterationsSliderChange)
    
    tophatSettingBox.addWidget(sliderIterations)
    
    tophatSettingBox.addWidget(QLabel("Vyber vzor násobícího jádra"))
    
    square = QRadioButton("Čtverec",objectName = "square")
    square.clicked.connect(buttonChange)
    square.setChecked(True)
    
    ellipse = QRadioButton("Elipsa",objectName = "ellipse")
    ellipse.clicked.connect(buttonChange)
    
    cross = QRadioButton("Kříž", objectName = "cross")
    cross.clicked.connect(buttonChange)
    
    radioBtnGroup = QButtonGroup()
    radioBtnGroup.addButton(square)
    radioBtnGroup.addButton(ellipse)
    radioBtnGroup.addButton(cross)
    
    radioBtns = QBoxLayout(0)
    
    radioBtnSquare = QBoxLayout(2)
    
    radioBtnSquare.addWidget(square, 0, Qt.AlignCenter)
    
    exampleSquare = QLabel("[1, 1, 1, 1, 1]\n[1, 1, 1, 1, 1]\n[1, 1, 1, 1, 1]\n[1, 1, 1, 1, 1]\n[1, 1, 1, 1, 1]")
    exampleSquare.setFont(QFont('Arial', 15))
    radioBtnSquare.addWidget(exampleSquare, 0, Qt.AlignCenter)
    
    radioBtnEllipse = QBoxLayout(2)
    
    radioBtnEllipse.addWidget(ellipse, 0, Qt.AlignCenter)
    
    exampleEllipse = QLabel("[0, 0, 1, 0, 0]\n[1, 1, 1, 1, 1]\n[1, 1, 1, 1, 1]\n[1, 1, 1, 1, 1]\n[0, 0, 1, 0, 0]")
    exampleEllipse.setFont(QFont('Arial', 15))
    radioBtnEllipse.addWidget(exampleEllipse, 0, Qt.AlignCenter)
    
    
    radioBtnCross = QBoxLayout(2)
    
    radioBtnCross.addWidget(cross, 0, Qt.AlignCenter)
    
    exampleCross = QLabel("[0, 0, 1, 0, 0]\n[0, 0, 1, 0, 0]\n[1, 1, 1, 1, 1]\n[0, 0, 1, 0, 0]\n[0, 0, 1, 0, 0]")
    exampleCross.setFont(QFont('Arial', 15))
    radioBtnCross.addWidget(exampleCross, 0, Qt.AlignCenter)
    
    radioBtns.addLayout(radioBtnSquare)
    radioBtns.addLayout(radioBtnEllipse)
    radioBtns.addLayout(radioBtnCross)
    
    tophatSettingBox.addLayout(radioBtns)
    
    #maip buttns init
    tophatManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Zahodit")
    saveBtn = QPushButton("Uložit")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    tophatManipBtns.addWidget(discardBtn)
    tophatManipBtns.addWidget(QLabel(" "))
    tophatManipBtns.addWidget(saveBtn)
    
    
    tophatWidgetLayout.addLayout(tophatSettingBox,0,0)
    tophatWidgetLayout.addWidget(QLabel(" ")      ,1,0)
    tophatWidgetLayout.addLayout(tophatManipBtns ,2,0)
    
    tophatWidgetLayout.setRowStretch(1,2)
    
    tophatWidget.setLayout(tophatWidgetLayout)
    return tophatWidget