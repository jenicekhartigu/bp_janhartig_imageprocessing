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

def convolutionWidgetInit(disAreas, logDisp):
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
            
        except:
            None  
            
        convolutionPicture(value)
    
    def convolutionPicture(size):
        try:
            kernel = np.ones((size,size),np.float32)/25
            bluredArray = cv.filter2D(inputImage[-1],-1,kernel)
        
            bluredImg = Image.fromarray(bluredArray, "RGB")
            
            functionalAreas[2].setPixmap(imgToPixmap(bluredImg))
        except:
            globalFunc.logDialog("ERR: Convolution cant be proceed")
        
    def setToDefault():
        matrixSizeSlider.setValue(1)
            
    def saveChanges():
        globalFunc.addImageDict("convolution")
    
    #LAYOUT 
    convolutionWidget = QWidget(objectName = "convolution")
    convolutionWidgetLayout = QGridLayout()
    settingBox = QBoxLayout(2)
    
    sizeOfMatrixLabel = QBoxLayout(0)
    matrixLabelText = QLabel("Convolution matrix size is")
    matrixLabelValue = QLabel("5x5")
    
    sizeOfMatrixLabel.addWidget(matrixLabelText)
    sizeOfMatrixLabel.addWidget(matrixLabelValue,0,Qt.AlignRight)
    sizeOfMatrixSet = QBoxLayout(0)
    
    matrixSizeSlider = QSlider(Qt.Horizontal, objectName = "matrixSize")
    matrixSizeSlider.setMinimum(1)
    matrixSizeSlider.setMaximum(15)
    matrixSizeSlider.setTickInterval(1)
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
    convolutionManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Discard")
    saveBtn = QPushButton("Save")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    convolutionManipBtns.addWidget(discardBtn)
    convolutionManipBtns.addWidget(QLabel(" "))
    convolutionManipBtns.addWidget(saveBtn)
    
    convolutionWidgetLayout.addLayout(sizeOfMatrixLabel, 0 ,0)
    convolutionWidgetLayout.addLayout(settingBox,        1 ,0)
    convolutionWidgetLayout.addLayout(convolutionManipBtns,2 ,0)
    
    convolutionWidget.setLayout(convolutionWidgetLayout)
    return convolutionWidget