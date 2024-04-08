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

def gaussianWidgetInit(disAreas, logDisp):
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
        
        value = 1
        
        if sender.objectName() == "matrixSize":
            if int(sender.value()) % 2 != 0:
                matrixSizeValue.setText(str(sender.value()))
                matrixSizeValue.setAlignment(Qt.AlignRight)
                matrixLabelValue.setText("[" + str(sender.value()) + "x" + str(sender.value())+"]")
                matrixLabelValue.setAlignment(Qt.AlignRight)
                value = int(sender.value())
        
        try:
            if int(sender.value()) % 2 != 0:
                value = int(matrixSizeValue.toPlainText())
                matrixSizeSlider.setValue(value) 
            
        except:
            None  
            
        gaussianPicture(value)
    
    def gaussianPicture(size):
        try:
            if size % 2 != 0:
                kernelSize = size
                bluredArray = cv.GaussianBlur(inputImage[-1],(kernelSize,kernelSize),0)
                
                bluredImg = Image.fromarray(bluredArray, "RGB")
                
                functionalAreas[2].setPixmap(imgToPixmap(bluredImg))
            
        except:
            globalFunc.logDialog("ERR: Gaussian blurring cant be proceed")
        
    def setToDefault():
        matrixSizeSlider.setValue(1)
        return None    
        
    def saveChanges():
        globalFunc.addImageDict("gaussian")
        return None
        
    #LAYOUT 
    gaussianWidget = QWidget(objectName = "gaussian")
    gaussianWidgetLayout = QGridLayout()
    settingBox = QBoxLayout(2)
    
    sizeOfMatrixLabel = QBoxLayout(0)
    matrixLabelText = QLabel("Gausian matrix size is")
    matrixLabelValue = QLabel("[5x5]")
    
    sizeOfMatrixLabel.addWidget(matrixLabelText)
    sizeOfMatrixLabel.addWidget(matrixLabelValue,0,Qt.AlignRight)
    sizeOfMatrixSet = QBoxLayout(0)
    
    matrixSizeSlider = QSlider(Qt.Horizontal, objectName = "matrixSize")
    matrixSizeSlider.setMinimum(1)
    matrixSizeSlider.setMaximum(49)
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
    
    warningLabel = QLabel("Warning\nMatrix for gaussian blurring must be odd")
    warningLabel.setAlignment(Qt.AlignCenter)
    warningLabel.setStyleSheet("border: 1px solid #ff0000;")
    
    settingBox.addLayout(sizeOfMatrixSet)
    settingBox.addWidget(warningLabel)
    settingBox.addWidget(QLabel(" "),2)
    
    #maip buttns init
    gaussianManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Discard")
    saveBtn = QPushButton("Save")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    gaussianManipBtns.addWidget(discardBtn)
    gaussianManipBtns.addWidget(QLabel(" "))
    gaussianManipBtns.addWidget(saveBtn)
    
    gaussianWidgetLayout.addLayout(sizeOfMatrixLabel, 0 ,0)
    gaussianWidgetLayout.addLayout(settingBox,        1 ,0)
    gaussianWidgetLayout.addLayout(gaussianManipBtns, 2 ,0)
    
    gaussianWidget.setLayout(gaussianWidgetLayout)
    return gaussianWidget