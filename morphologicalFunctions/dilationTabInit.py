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

def dilationWidgetInit(disAreas, logDisp):
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
            dilationExecution(sender.value(),sliderMatrixSize.value())
        if sender.objectName() == "matrixSize":
            dilationExecution(sliderIterations.value(),sender.value())
                
        return None
    
    def buttonChange():
        dilationExecution(sliderIterations.value(),sliderMatrixSize.value())
    
    def getCheckedButton():
        return radioBtnGroup.checkedId()
    
    def dilationExecution(iterations, size):
        if getCheckedButton() == -3:
            kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(size,size))
        elif getCheckedButton() == -4:
            kernel = cv.getStructuringElement(cv.MORPH_CROSS,(size,size))
        else:
            kernel = cv.getStructuringElement(cv.MORPH_RECT,(size,size))
        
        try:
            # dilateArray = cv.dilate(inputImage[-1],kernel,iterations = iterations)
            dilateArray = cv.dilate(inputImage[-1],kernel,iterations= iterations)
            
            dilateImg = Image.fromarray(dilateArray, "RGB")
                    
            functionalAreas[2].setPixmap(imgToPixmap(dilateImg))
        except:
            globalFunc.logDialog("ERR: Dilation on image cant be proceed")
            
        return None
        
    def setToDefault():
        square.setChecked(True)
        sliderIterations.setValue(0)
        return None
    
    def saveChanges():
        globalFunc.addImageDict("dilation")
        return None
    
    #LAYOUT 
    dilationWidget = QWidget(objectName = "dilation")
    dilationWidgetLayout = QGridLayout()
    
    dilationSettingBox = QBoxLayout(2)
    
    dilationSettingBox.addWidget(QLabel("Set size of matrix for dilation"))
    
    sliderMatrixSize = QSlider()
    sliderMatrixSize = QSlider(Qt.Horizontal, objectName = "matrixSize")
    sliderMatrixSize.setMinimum(1)
    sliderMatrixSize.setMaximum(50)
    sliderMatrixSize.setTickInterval(1)
    sliderMatrixSize.setTickPosition(QSlider.TicksBelow)
    sliderMatrixSize.valueChanged.connect(iterationsSliderChange)
    
    dilationSettingBox.addWidget(sliderMatrixSize)
    
    dilationSettingBox.addWidget(QLabel("Set number of iterations for dilation"))
    
    sliderIterations = QSlider()
    sliderIterations = QSlider(Qt.Horizontal, objectName = "iterations")
    sliderIterations.setMinimum(0)
    sliderIterations.setMaximum(20)
    sliderIterations.setTickInterval(1)
    sliderIterations.setTickPosition(QSlider.TicksBelow)
    sliderIterations.valueChanged.connect(iterationsSliderChange)
    
    dilationSettingBox.addWidget(sliderIterations)
    
    dilationSettingBox.addWidget(QLabel("Choose matrix patern for dilation"))
    
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
    
    dilationSettingBox.addLayout(radioBtns)
    
    #maip buttns init
    dilationManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Discard")
    saveBtn = QPushButton("Save")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    dilationManipBtns.addWidget(discardBtn)
    dilationManipBtns.addWidget(QLabel(" "))
    dilationManipBtns.addWidget(saveBtn)
    
    
    dilationWidgetLayout.addLayout(dilationSettingBox,0,0)
    dilationWidgetLayout.addWidget(QLabel(" ")      ,1,0)
    dilationWidgetLayout.addLayout(dilationManipBtns ,2,0)
    
    dilationWidgetLayout.setRowStretch(1,2)
    
    dilationWidget.setLayout(dilationWidgetLayout)
    return dilationWidget