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

def medianWidgetInit(disAreas, logDisp):
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
            matrixLabelValue.setText("[" + str(sender.value()) + "x" + str(sender.value())+"]")
            matrixLabelValue.setAlignment(Qt.AlignRight)
            value = int(sender.value())
        
        try:
            
            value = int(matrixSizeValue.toPlainText())
            matrixSizeSlider.setValue(value) 
            
        except:
            None  
            
        medianPicture(value)
    
    def medianPicture(size):
        try:
            bluredArray = cv.medianBlur(inputImage[-1],size)
            
            bluredImg = Image.fromarray(bluredArray, "RGB")
            
            functionalAreas[2].setPixmap(imgToPixmap(bluredImg))
            
        except:
            globalFunc.logDialog("ERR: median blurring cant be proceed")
        
    def setToDefault():
        matrixSizeSlider.setValue(1)
        return None    
        
    def saveChanges():
        globalFunc.addImageDict("median")
        return None
        
    #LAYOUT 
    medianWidget = QWidget(objectName = "median")
    medianWidgetLayout = QGridLayout()
    settingBox = QBoxLayout(2)
    
    sizeOfMatrixLabel = QBoxLayout(0)
    matrixLabelText = QLabel("Median matrix size is")
    matrixLabelValue = QLabel("[2x2]")
    
    sizeOfMatrixLabel.addWidget(matrixLabelText)
    sizeOfMatrixLabel.addWidget(matrixLabelValue,0,Qt.AlignRight)
    sizeOfMatrixSet = QBoxLayout(0)
    
    matrixSizeSlider = QSlider(Qt.Horizontal, objectName = "matrixSize")
    matrixSizeSlider.setMinimum(1)
    matrixSizeSlider.setMaximum(10)
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
    medianManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Discard")
    saveBtn = QPushButton("Save")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    medianManipBtns.addWidget(discardBtn)
    medianManipBtns.addWidget(QLabel(" "))
    medianManipBtns.addWidget(saveBtn)
    
    medianWidgetLayout.addLayout(sizeOfMatrixLabel, 0 ,0)
    medianWidgetLayout.addLayout(settingBox,        1 ,0)
    medianWidgetLayout.addLayout(medianManipBtns, 2 ,0)
    
    medianWidget.setLayout(medianWidgetLayout)
    return medianWidget