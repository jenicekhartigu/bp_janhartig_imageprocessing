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

def imgToPixmap(image):
    im2 = image.convert("RGBA")
    data = im2.tobytes("raw", "BGRA")
    qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap

def averagingWidgetInit(disAreas, logDisp):
    for i in disAreas:
        functionalAreas.append(i)
        
    for i in logDisp:
        logDisplay.append(i)
        
    try:
        pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
        fromArray = np.asarray(pixmapImage)
        inputImage.append(fromArray)

    except:
        globalFunc.logDialog("WARNING: No image loaded")
      
    def changeValueSlider(): 
        
        sender = QObject().sender()
        
        value = 0
        
        if sender.objectName() == "matrixSize":
            
            matrixSizeValue.setText(str(sender.value()))
            matrixSizeValue.setAlignment(Qt.AlignRight)
            matrixLabelValue.setText(str(sender.value()) + "x" + str(sender.value()))
            matrixLabelValue.setAlignment(Qt.AlignRight)
            value = int(sender.value())
        
        try:
            value = int(matrixSizeValue.toPlainText())
            matrixSizeSlider.setValue(value) 
            
            # matrixLabelValue.setText(str(value, "x", value))
            # matrixLabelValue.setAlignment(Qt.AlignRight)
        except:
            None  
            
        averagingPicture(value)
    
    def averagingPicture(size):
        try:
            bluredArray = cv.blur(inputImage[-1],(size,size))
            
            bluredImg = Image.fromarray(bluredArray, "RGB")
            
            functionalAreas[2].setPixmap(imgToPixmap(bluredImg))
        
        except:
            globalFunc.logDialog("ERR: Averaging cant be proceed")
        
    def setToDefault():
        matrixSizeSlider.setValue(1)
            
        
    def saveChanges():
        globalFunc.addImageDict("averaging")
        
        
    #LAYOUT 
    averagingWidget = QWidget(objectName = "averaging")
    averagingWidgetLayout = QGridLayout()
    settingBox = QBoxLayout(2)
    
    sizeOfMatrixLabel = QBoxLayout(0)
    matrixLabelText = QLabel("Averaging matrix size is")
    matrixLabelValue = QLabel("5x5")
    
    sizeOfMatrixLabel.addWidget(matrixLabelText)
    sizeOfMatrixLabel.addWidget(matrixLabelValue,0,Qt.AlignRight)
    sizeOfMatrixSet = QBoxLayout(0)
    
    matrixSizeSlider = QSlider(Qt.Horizontal, objectName = "matrixSize")
    matrixSizeSlider.setMinimum(1)
    matrixSizeSlider.setMaximum(50)
    matrixSizeSlider.setTickInterval(2)
    matrixSizeSlider.setTickPosition(QSlider.TicksBelow)
    matrixSizeSlider.valueChanged.connect(changeValueSlider)
    
    matrixSizeValue = QTextEdit()
    matrixSizeValue.setText("0")
    matrixSizeValue.setMaximumSize(60,30)
    matrixSizeValue.setAlignment(Qt.AlignRight)
    matrixSizeValue.textChanged.connect(changeValueSlider)
    
    sizeOfMatrixSet.addWidget(matrixSizeSlider)
    sizeOfMatrixSet.addWidget(matrixSizeValue)
    
    
    settingBox.addLayout(sizeOfMatrixSet)
    settingBox.addWidget(QLabel(" "),2)
    
    #maip buttns init
    averagingManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Discard")
    saveBtn = QPushButton("Save")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    averagingManipBtns.addWidget(discardBtn)
    averagingManipBtns.addWidget(QLabel(" "))
    averagingManipBtns.addWidget(saveBtn)
    
    averagingWidgetLayout.addLayout(sizeOfMatrixLabel, 0 ,0)
    averagingWidgetLayout.addLayout(settingBox,        1 ,0)
    averagingWidgetLayout.addLayout(averagingManipBtns,2 ,0)
    
    averagingWidget.setLayout(averagingWidgetLayout)
    return averagingWidget