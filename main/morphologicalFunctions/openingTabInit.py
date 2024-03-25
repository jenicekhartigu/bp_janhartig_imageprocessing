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

def openingWidgetInit(disAreas, logDisp):
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
            openingExecution(sender.value(),sliderMatrixSize.value())
        if sender.objectName() == "matrixSize":
            openingExecution(sliderIterations.value(),sender.value())
                
        return None
    
    def buttonChange():
        openingExecution(sliderIterations.value(),sliderMatrixSize.value())
    
    def getCheckedButton():
        return radioBtnGroup.checkedId()
    
    def openingExecution(iterations, size):
        if getCheckedButton() == -3:
            kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(size,size))
        elif getCheckedButton() == -4:
            kernel = cv.getStructuringElement(cv.MORPH_CROSS,(size,size))
        else:
            kernel = cv.getStructuringElement(cv.MORPH_RECT,(size,size))
        
        try:
            openingArray = cv.morphologyEx(inputImage[-1],cv.MORPH_OPEN,kernel, iterations = iterations)
            
            openingImg = Image.fromarray(openingArray, "RGB")
                    
            functionalAreas[2].setPixmap(imgToPixmap(openingImg))
        except:
            globalFunc.logDialog("ERR: Dilation on image cant be proceed")
            
        return None
        
    def setToDefault():
        square.setChecked(True)
        sliderIterations.setValue(0)
        return None
    
    def saveChanges():
        globalFunc.addImageDict("opening")
        return None
    
    #LAYOUT 
    openingWidget = QWidget(objectName = "opening")
    openingWidgetLayout = QGridLayout()
    
    openingSettingBox = QBoxLayout(2)
    
    openingSettingBox.addWidget(QLabel("Set size of matrix for opening"))
    
    sliderMatrixSize = QSlider()
    sliderMatrixSize = QSlider(Qt.Horizontal, objectName = "matrixSize")
    sliderMatrixSize.setMinimum(1)
    sliderMatrixSize.setMaximum(25)
    sliderMatrixSize.setTickInterval(1)
    sliderMatrixSize.setTickPosition(QSlider.TicksBelow)
    sliderMatrixSize.valueChanged.connect(iterationsSliderChange)
    
    openingSettingBox.addWidget(sliderMatrixSize)
    
    openingSettingBox.addWidget(QLabel("Set number of iterations for opening (erosion followed by dilation)"))
    
    sliderIterations = QSlider()
    sliderIterations = QSlider(Qt.Horizontal, objectName = "iterations")
    sliderIterations.setMinimum(0)
    sliderIterations.setMaximum(10)
    sliderIterations.setTickInterval(1)
    sliderIterations.setTickPosition(QSlider.TicksBelow)
    sliderIterations.valueChanged.connect(iterationsSliderChange)
    
    openingSettingBox.addWidget(sliderIterations)
    
    openingSettingBox.addWidget(QLabel("Choose matrix patern for opening"))
    
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
    
    openingSettingBox.addLayout(radioBtns)
    
    #maip buttns init
    openingManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Discard")
    saveBtn = QPushButton("Save")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    openingManipBtns.addWidget(discardBtn)
    openingManipBtns.addWidget(QLabel(" "))
    openingManipBtns.addWidget(saveBtn)
    
    
    openingWidgetLayout.addLayout(openingSettingBox,0,0)
    openingWidgetLayout.addWidget(QLabel(" ")      ,1,0)
    openingWidgetLayout.addLayout(openingManipBtns ,2,0)
    
    openingWidgetLayout.setRowStretch(1,2)
    
    openingWidget.setLayout(openingWidgetLayout)
    return openingWidget