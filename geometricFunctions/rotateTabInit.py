
import numpy as np
import cv2 as cv

from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
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

def imgToPixmap(image):
    im2 = image.convert("RGBA")
    data = im2.tobytes("raw", "BGRA")
    qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap

def rotateWidgetInit(disAreas, logDisp):
    for i in disAreas:
        functionalAreas.append(i)
        
    for i in logDisp:
        logDisplay.append(i)
        
    try:
        pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
        inputImage.append(np.asarray(pixmapImage))
    except:
        globalFunc.logDialog("WARNING: Není načten obrázek")
                
    def changeValueSlider():
        sender = QObject().sender()
        
        if sender.objectName() == "rotateSlider":
            degree = int(sender.value())
            
            if (int(sender.value()) == 0):
                txtLabel2.setText("°[stupňů]")
                
            if (int(sender.value()) < 0):
                txtLabel2.setText("°[stupňů] do leva")
                
            if (int(sender.value()) > 0):
                txtLabel2.setText("°[stupňů] do prava")
                
            rotateValue.setText(str(degree))
            rotateValue.setAlignment(Qt.AlignRight)
        
        try:
            value = int(rotateValue.toPlainText())
            slider.setValue(value) 
        except:
            None
            
        rotatePicture(value)
        return None
    

    
    def setToDefault():
        rotateValue.setText("0")
        return None
    
    def saveChanges():
        globalFunc.addImageDict("rotation")
        return None
    
    def rotatePicture(val):
        try:
            img = inputImage[-1]
            rows,cols, _ = img.shape
            
            M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),val,1)

            dst = cv.warpAffine(img,M,(cols,rows))
            
            pixmap = imgToPixmap(Image.fromarray(dst, "RGB"))
            
            functionalAreas[2].setPixmap(pixmap)
        except:
            globalFunc.logDialog("WARNING: Není načten obrázek")
        
    #LAYOUT 
    rotateWidget = QWidget(objectName = "rotate")
    rotateWidgetLayout = QGridLayout()
    
    labelNamesBox = QBoxLayout(0)
    # labelNamesBox.setContentsMargins(10,10,10,10)
    rotateLeft = QLabel("Doleva")
    rotateLeft.setAlignment(Qt.AlignLeft)
    
    rotateRight = QLabel("Doprava")
    rotateRight.setAlignment(Qt.AlignRight)
    
    labelNamesBox.addWidget(rotateLeft)
    labelNamesBox.addWidget(rotateRight)
    
    slider = QSlider(Qt.Horizontal, objectName = "rotateSlider")
    slider.setMinimum(-180)
    slider.setMaximum(180)
    slider.setTickInterval(10)
    
    slider.setTickPosition(QSlider.TicksBelow)
    slider.valueChanged.connect(changeValueSlider)
    
    labelAndSetValue = QBoxLayout(0)
    
    txtLabel = QLabel("Otoč obraz ")
    rotateValue = QTextEdit()
    rotateValue.setText("0")
    rotateValue.setMaximumSize(60,30)
    rotateValue.setAlignment(Qt.AlignRight)
    rotateValue.textChanged.connect(changeValueSlider)
    
    txtLabel2 = QLabel("°[stupňů]")
    
    labelAndSetValue.addWidget(txtLabel)
    labelAndSetValue.addWidget(rotateValue)
    labelAndSetValue.addWidget(txtLabel2)
    
    #empty label init
    emptyLabel = QLabel(" ")
    
    #maip buttns init
    rotateManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Zahodit")
    saveBtn = QPushButton("Uložit")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    rotateManipBtns.addWidget(discardBtn)
    rotateManipBtns.addWidget(emptyLabel)
    rotateManipBtns.addWidget(saveBtn)
    
    #adding all thing of widget together
    
    rotateWidgetLayout.addLayout(labelNamesBox,     0,0,1,0)
    rotateWidgetLayout.addWidget(slider,            1,0,1,0)
    rotateWidgetLayout.addLayout(labelAndSetValue,  2,0,1,0)
    
    rotateWidgetLayout.addWidget(emptyLabel,        3,0,1,0)
    
    rotateWidgetLayout.addLayout(rotateManipBtns,   4,0,1,0)
    
    rotateWidgetLayout.setRowStretch(3,2)
    
    rotateWidget.setLayout(rotateWidgetLayout)
    return rotateWidget