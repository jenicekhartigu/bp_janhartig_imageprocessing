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

def adaptiveThreshWidgetInit(disAreas, logDisp):
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
        adaptiveThreshExecution(sliderMatrixSize.value())
        
        
    def adaptiveThreshExecution(size):
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
        globalFunc.addImageDict("adaptiveThresh")
        
        
    #LAYOUT 
    adaptiveThreshWidget = QWidget(objectName = "adaptiveThresh")
    adaptiveThreshWidgetLayout = QGridLayout()
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
    
    settingBox.addWidget(QLabel("empty"),2)
    
    #maip buttns init
    adaptiveThreshManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Discard")
    saveBtn = QPushButton("Save")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    adaptiveThreshManipBtns.addWidget(discardBtn)
    adaptiveThreshManipBtns.addWidget(QLabel(" "))
    adaptiveThreshManipBtns.addWidget(saveBtn)
    
    adaptiveThreshWidgetLayout.addWidget(sliderLabel, 0 ,0)
    adaptiveThreshWidgetLayout.addLayout(settingBox,        1 ,0)
    adaptiveThreshWidgetLayout.addLayout(adaptiveThreshManipBtns,2 ,0)
    
    adaptiveThreshWidget.setLayout(adaptiveThreshWidgetLayout)
    return adaptiveThreshWidget