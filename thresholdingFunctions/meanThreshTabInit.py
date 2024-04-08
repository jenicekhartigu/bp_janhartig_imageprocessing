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

def meanThreshWidgetInit(disAreas, logDisp):
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
        
    def matrixSize():
        meanThreshExecution(sliderMatrixSize.value())
        
        
    def meanThreshExecution(size):
        try:
            if size % 2 != 0:
                (b, g, r) = cv.split(inputImage[-1])
                
                threshRed = cv.adaptiveThreshold(r, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, size, 2)
                threshGreen = cv.adaptiveThreshold(g, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, size, 2)  
                threshBlue = cv.adaptiveThreshold(b, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, size, 2)  
                
                result = cv.merge((threshBlue, threshGreen, threshRed))
                
                threshImg = Image.fromarray(result, "RGB")
                            
                functionalAreas[2].setPixmap(imgToPixmap(threshImg))   
        except:
            globalFunc.logDialog("ERR: Adaptive thresholding blurring cant be proceed")      
        
    def setToDefault():
        sliderMatrixSize.setValue(3)
            
        
    def saveChanges():
        globalFunc.addImageDict("meanThresh")
        
        
    #LAYOUT 
    meanThreshWidget = QWidget(objectName = "meanThresh")
    meanThreshWidgetLayout = QGridLayout()
    settingBox = QBoxLayout(2)
    
    sliderLabel = QLabel("Set size of matrix for adaptive thresholding")
    
    sliderMatrixSize = QSlider()
    sliderMatrixSize = QSlider(Qt.Horizontal, objectName = "matrixSize")
    sliderMatrixSize.setMinimum(3)
    sliderMatrixSize.setMaximum(25)
    sliderMatrixSize.setTickInterval(1)
    sliderMatrixSize.setTickPosition(QSlider.TicksBelow)
    sliderMatrixSize.valueChanged.connect(matrixSize)
    
    settingBox.addWidget(sliderMatrixSize)
    
    settingBox.addWidget(QLabel(""),2)
    
    #maip buttns init
    meanThreshManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Discard")
    saveBtn = QPushButton("Save")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    meanThreshManipBtns.addWidget(discardBtn)
    meanThreshManipBtns.addWidget(QLabel(" "))
    meanThreshManipBtns.addWidget(saveBtn)
    
    meanThreshWidgetLayout.addWidget(sliderLabel, 0 ,0)
    meanThreshWidgetLayout.addLayout(settingBox,        1 ,0)
    meanThreshWidgetLayout.addLayout(meanThreshManipBtns,2 ,0)
    
    meanThreshWidget.setLayout(meanThreshWidgetLayout)
    return meanThreshWidget