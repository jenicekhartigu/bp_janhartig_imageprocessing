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

actualSize = [[0,0]]

def imgToPixmap(image):
    im2 = image.convert("RGBA")
    data = im2.tobytes("raw", "BGRA")
    qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap

def shiftingWidgetInit(disAreas, logDisp):
    for i in disAreas:
        functionalAreas.append(i)
        
    for i in logDisp:
        logDisplay.append(i)
        
    try:
        pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
        fromArray = np.asarray(pixmapImage)
        inputImage.append(fromArray)
        wid, hei, _ = fromArray.shape
        
        actualSize[0] = [wid, hei]      
    except:
        globalFunc.logDialog("WARNING: Není načten obrázek")
        
    #Functions
    def changeValueSlider():
        sender = QObject().sender()
        
        if sender.objectName() == "sliderHei":
            heiValue.setText(str(sliderHei.value()))
            heiValue.setAlignment(Qt.AlignRight)
        
        if sender.objectName() == "sliderWid":
            widValue.setText(str(sliderWid.value()))
            widValue.setAlignment(Qt.AlignRight)
            
        try:
            heiVal = int(heiValue.toPlainText())
            widVal = int(widValue.toPlainText())
            
            sliderHei.setValue(heiVal)
            sliderWid.setValue(widVal)
            
        except:
            None
            
        shiftPicture(heiVal,widVal)
    
    def getPixelsOfPixmap():
        try:

            pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
            inputImage.append(np.asarray(pixmapImage))
            
            hei, wid, z = np.asarray(pixmapImage).shape
            actualSize[0] = [hei, wid]
            
        except:
            globalFunc.logDialog("ERR: Nemohu získat velikost obrazu")

    def setToDefault():
        heiValue.setText("0")
        widValue.setText("0")
        
        widValue.setAlignment(Qt.AlignRight)
        heiValue.setAlignment(Qt.AlignRight)
        
    def saveChanges():
        globalFunc.addImageDict("shifting")
        
    def shiftPicture(hei, wid):
        try:
            heiPixmap, widPixmap = actualSize[0]
            
            hei1 = heiPixmap/100
            wid1 = widPixmap/100
            
            img = inputImage[-1]
            
            heiValueLabel.setText("Posunutý o "+str(abs(int(hei*hei1)))+ " pixelu")
            widValueLabel.setText("/osunutý o "+str(abs(int(wid*wid1)))+ " pixelu")
            heiValueLabel.setAlignment(Qt.AlignRight)
            widValueLabel.setAlignment(Qt.AlignRight)
            
            M = np.float32([[1,0,int(wid*wid1)],[0,1,int(hei*hei1)]])
            dst = cv.warpAffine(img,M,(widPixmap,heiPixmap))
            
            pixmap = imgToPixmap(Image.fromarray(dst, "RGB"))
            functionalAreas[2].setPixmap(pixmap)
        except:
            globalFunc.logDialog("ERR: Obrazek nemuze byt posunut")
          
    #LAYOUT
    shiftingWidget = QWidget(objectName = "shifting")
    #placeholder
    emptyLabel = QLabel(" ")
    
    shiftingWidgetLayout = QGridLayout()
     
    heiMainBox = QBoxLayout(2)
    widMainBox = QBoxLayout(2)
    
    #hei 
    heiLabelBox = QBoxLayout(0)
    heiValueBox = QBoxLayout(0)
    #first row in box
    heiLabel = QLabel("Posuvník výšky")
    heiValueLabel = QLabel("pixelů")
    
    heiLabelBox.addWidget(heiLabel)
    heiLabelBox.addWidget(heiValueLabel, 0, Qt.AlignRight)
    
    #second row in box
    sliderHei = QSlider(Qt.Horizontal, objectName = "sliderHei")
    sliderHei.setMinimum(-100)
    sliderHei.setMaximum(100)
    sliderHei.setTickInterval(10)
    
    sliderHei.setTickPosition(QSlider.TicksBelow)
    sliderHei.valueChanged.connect(changeValueSlider)
    
    heiValue = QTextEdit()
    heiValue.setText("0")
    heiValue.setMaximumSize(60,20)
    heiValue.setAlignment(Qt.AlignRight)
    heiValue.textChanged.connect(changeValueSlider)
    
    heiValueBox.addWidget(sliderHei)
    heiValueBox.addWidget(heiValue)
    
    #width
    widLabelBox = QBoxLayout(0)
    widValueBox = QBoxLayout(0)
    #first row in box
    widLabel = QLabel("Posuvník šířky")
    widValueLabel = QLabel("pixelů")
    
    widLabelBox.addWidget(widLabel)
    widLabelBox.addWidget(widValueLabel, 0, Qt.AlignRight)
    
    #second row in box
    sliderWid = QSlider(Qt.Horizontal, objectName = "sliderWid")
    sliderWid.setMinimum(-100)
    sliderWid.setMaximum(100)
    sliderWid.setTickInterval(10)
    
    sliderWid.setTickPosition(QSlider.TicksBelow)
    sliderWid.valueChanged.connect(changeValueSlider)
    
    widValue = QTextEdit()
    widValue.setText("0")
    widValue.setMaximumSize(60,20)
    widValue.setAlignment(Qt.AlignRight)
    widValue.textChanged.connect(changeValueSlider)
    
    widValueBox.addWidget(sliderWid)
    widValueBox.addWidget(widValue)
    
    #main manip box
    heiMainBox.addLayout(heiLabelBox)
    heiMainBox.addLayout(heiValueBox)
    
    widMainBox.addLayout(widLabelBox)
    widMainBox.addLayout(widValueBox)
    
    getPixelsBtn = QPushButton("Získej rozměry")
    getPixelsBtn.clicked.connect(getPixelsOfPixmap)
    
    #maip buttns init
    shiftingManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Zahodit")
    saveBtn = QPushButton("Uložit")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    shiftingManipBtns.addWidget(discardBtn)
    shiftingManipBtns.addWidget(emptyLabel)
    shiftingManipBtns.addWidget(saveBtn)
    
    
    #adding all thing of widget together    
    shiftingWidgetLayout.addLayout(widMainBox,          0,0,1,0)
    shiftingWidgetLayout.addLayout(heiMainBox,          1,0,1,0)
    
    shiftingWidgetLayout.addWidget(getPixelsBtn,        2,0,1,0)
    
    shiftingWidgetLayout.addWidget(emptyLabel,          3,0,1,0)
    shiftingWidgetLayout.addLayout(shiftingManipBtns,   4,0,1,0)
    
    shiftingWidgetLayout.setRowStretch(3,2)
    
    shiftingWidget.setLayout(shiftingWidgetLayout)
    return shiftingWidget