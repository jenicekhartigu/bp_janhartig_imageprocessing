import re
from matplotlib.pyplot import imshow
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

selectedColorDict = {}
selectedColorPILDict = {}

def imgToPixmap(image):
    im2 = image.convert("RGBA")
    data = im2.tobytes("raw", "BGRA")
    qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap

def erosionWidgetInit(disAreas, logDisp):
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
    
        
    def iterationsSliderChange():
        sender = QObject().sender()
        if sender.objectName() == "iterations":
            erosionExecution(sender.value(),sliderMatrixSize.value())
        if sender.objectName() == "matrixSize":
            erosionExecution(sliderIterations.value(),sender.value())
                
        
    
    def buttonChange():
        erosionExecution(sliderIterations.value(),sliderMatrixSize.value())
        
    def getCheckedButton():
        return radioBtnGroup.checkedId()
    
    def erosionExecution(iterations, size):
        if getCheckedButton() == -3:
            kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(size,size))
        elif getCheckedButton() == -4:
            kernel = cv.getStructuringElement(cv.MORPH_CROSS,(size,size))
        else:
            kernel = cv.getStructuringElement(cv.MORPH_RECT,(size,size))
            
        try:    
            erodeArray = cv.erode(inputImage[-1],kernel,iterations = iterations)
            
            erodeImg = Image.fromarray(erodeArray, "RGB")
                    
            functionalAreas[2].setPixmap(imgToPixmap(erodeImg))
        except:
            globalFunc.logDialog("ERR: Erosion on image cant be proceed")
        
        
    def setToDefault():
        square.setChecked(True)
        sliderIterations.setValue(0)
        
    
    def saveChanges():
        globalFunc.addImageDict("erosion")
        
    
    #LAYOUT 
    erosionWidget = QWidget(objectName = "erosion")
    erosionWidgetLayout = QGridLayout()
    
    erosionSettingBox = QBoxLayout(2)
    
    erosionSettingBox.addWidget(QLabel("Set size of matrix for erosion"))
    
    sliderMatrixSize = QSlider()
    sliderMatrixSize = QSlider(Qt.Horizontal, objectName = "matrixSize")
    sliderMatrixSize.setMinimum(1)
    sliderMatrixSize.setMaximum(25)
    sliderMatrixSize.setTickInterval(1)
    sliderMatrixSize.setTickPosition(QSlider.TicksBelow)
    sliderMatrixSize.valueChanged.connect(iterationsSliderChange)
    
    erosionSettingBox.addWidget(sliderMatrixSize)
    
    erosionSettingBox.addWidget(QLabel("Set number of iterations for erosion"))
    
    sliderIterations = QSlider()
    sliderIterations = QSlider(Qt.Horizontal, objectName = "iterations")
    sliderIterations.setMinimum(0)
    sliderIterations.setMaximum(10)
    sliderIterations.setTickInterval(1)
    sliderIterations.setTickPosition(QSlider.TicksBelow)
    sliderIterations.valueChanged.connect(iterationsSliderChange)
    
    erosionSettingBox.addWidget(sliderIterations)
    
    erosionSettingBox.addWidget(QLabel("Choose matrix patern for erosion"))
    
    square = QRadioButton("Square",objectName = "square")
    square.clicked.connect(buttonChange)
    square.setChecked(True)
    
    ellipse = QRadioButton("Ellipse",objectName = "ellipse")
    ellipse.clicked.connect(buttonChange)
    
    cross = QRadioButton("Cross", objectName = "cross")
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
    
    erosionSettingBox.addLayout(radioBtns)
    
    #maip buttns init
    erosionManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Discard")
    saveBtn = QPushButton("Save")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    erosionManipBtns.addWidget(discardBtn)
    erosionManipBtns.addWidget(QLabel(" "))
    erosionManipBtns.addWidget(saveBtn)
    
    
    erosionWidgetLayout.addLayout(erosionSettingBox,0,0)
    erosionWidgetLayout.addWidget(QLabel(" ")      ,1,0)
    erosionWidgetLayout.addLayout(erosionManipBtns ,2,0)
    
    erosionWidgetLayout.setRowStretch(1,2)
    
    erosionWidget.setLayout(erosionWidgetLayout)
    return erosionWidget