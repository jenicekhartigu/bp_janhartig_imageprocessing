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

x1Arr = [0,0]
y1Arr = [0,0]

x2Arr = [0,0]
y2Arr = [0,0] 

point1 = [0,0]
point2 = [0,0]
point3 = [0,0]
point4 = [0,0]

actualSize = [0,0]

def imgToPixmap(image):
    im2 = image.convert("RGBA")
    data = im2.tobytes("raw", "BGRA")
    qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap

def perspectiveWidgetInit(disAreas, logDisp):
    for i in disAreas:
        functionalAreas.append(i)
        
    for i in logDisp:
        logDisplay.append(i)

    try:
        pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
        fromArray = np.asarray(pixmapImage)
        inputImage.append(fromArray)
        wid, hei, _ = fromArray.shape
        
        actualSize[0] = wid
        actualSize[1] = hei  
    except:
        globalFunc.logDialog("WARNING: No image loaded")
        
    def changeValueSlider():
        sender = QObject().sender()
        
        mask = np.zeros((actualSize[0],actualSize[1],4), np.uint8)
        
        if sender.objectName() == "sliderXT1":
            x1Arr[0] = int(sender.value())
            
        if sender.objectName() == "sliderXB1":    
            x1Arr[1]  = int(sender.value())
            
        if sender.objectName() == "sliderYL1":    
            y1Arr[0] = int(sender.value())
            
        if sender.objectName() == "sliderYR1":    
            y1Arr[1] = int(sender.value())
        
        if sender.objectName() == "sliderXT2":
            x2Arr[0] = int(sender.value())
            
        if sender.objectName() == "sliderXB2":    
            x2Arr[1]  = int(sender.value())
            
        if sender.objectName() == "sliderYL2":    
            y2Arr[0] = int(sender.value())
            
        if sender.objectName() == "sliderYR2":    
            y2Arr[1] = int(sender.value())    
            
        cv.line(mask, (x1Arr[0]+int(actualSize[1]/2), 0), (x1Arr[1]+int(actualSize[1]/2), actualSize[0]), (0, 255, 255, 255), 3)
        cv.line(mask, (0, y1Arr[0]+int(actualSize[0]/2)), (actualSize[1], y1Arr[1]+int(actualSize[0]/2)), (255, 0, 255, 255), 3)
        
        cv.line(mask, (x2Arr[0]+int(actualSize[1]/2), 0), (x2Arr[1]+int(actualSize[1]/2), actualSize[0]), (255, 255, 0, 255), 3)
        cv.line(mask, (0, y2Arr[0]+int(actualSize[0]/2)), (actualSize[1], y2Arr[1]+int(actualSize[0]/2)), (0, 0, 0, 255), 3)
        
        leftSide =      [(x1Arr[0]+int(actualSize[1]/2), 0),(x1Arr[1]+int(actualSize[1]/2), actualSize[0])]
        topSide =       [(0, y1Arr[0]+int(actualSize[0]/2)),(actualSize[1], y1Arr[1]+int(actualSize[0]/2))]
        rightSide =     [(x2Arr[0]+int(actualSize[1]/2), 0),(x2Arr[1]+int(actualSize[1]/2), actualSize[0])]
        bottomSide =    [(0, y2Arr[0]+int(actualSize[0]/2)),(actualSize[1], y2Arr[1]+int(actualSize[0]/2))]
        
        try:
            pr1, pr2, pr3, pr4 = findIntersections(leftSide,topSide,rightSide,bottomSide)
            
            point1[0], point1[1] = pr1
            point2[0], point2[1] = pr4
            point3[0], point3[1] = pr3
            point4[0], point4[1] = pr2
            
            font = cv.FONT_HERSHEY_SIMPLEX
            
            cv.circle(mask,pr1,5,(255,0,0,255),-1)
            cv.putText(mask,str(pr1),pr1,font,0.5,(0,0,0,255),1,cv.LINE_AA)
            
            cv.circle(mask,pr2,5,(255,0,0,255),-1)
            cv.putText(mask,str(pr2),pr2,font,0.5,(0,0,0,255),1,cv.LINE_AA)
            
            cv.circle(mask,pr3,5,(255,0,0,255),-1)
            cv.putText(mask,str(pr3),pr3,font,0.5,(0,0,0,255),1,cv.LINE_AA)
            
            cv.circle(mask,pr4,5,(255,0,0,255),-1)
            cv.putText(mask,str(pr4),pr4,font,0.5,(0,0,0,255),1,cv.LINE_AA)
        except:
            globalFunc.logDialog("WARNING: Intersections")
        
        mask = mask[:]
        imgMask = Image.fromarray(mask, "RGBA")
        
        img = Image.fromarray(inputImage[-1], "RGB")
        
        res = Image.composite(imgMask , img, mask = imgMask )   
        
        pixmap = imgToPixmap(res)
        
        functionalAreas[2].setPixmap(pixmap)

    def findIntersections(leftSide, topSide, rightSide, bottomSide):

        left_vec = (leftSide[1][0] - leftSide[0][0], leftSide[1][1] - leftSide[0][1])
        top_vec = (topSide[1][0] - topSide[0][0], topSide[1][1] - topSide[0][1])
        right_vec = (rightSide[1][0] - rightSide[0][0], rightSide[1][1] - rightSide[0][1])
        bottom_vec = (bottomSide[1][0] - bottomSide[0][0], bottomSide[1][1] - bottomSide[0][1])

        if left_vec == right_vec and top_vec == bottom_vec:
            globalFunc.logDialog("WARNING: Rovnobezne primky")
            raise ValueError("")

        pr1 = findIntersection(leftSide, topSide)
        pr2 = findIntersection(rightSide, bottomSide)
        pr3 = findIntersection(leftSide, bottomSide)
        pr4 = findIntersection(rightSide, topSide)

        return pr1, pr2, pr3, pr4

    def findIntersection(p1, p2):
        a1 = p1[1][1] - p1[0][1]
        b1 = p1[0][0] - p1[1][0]
        c1 = a1 * p1[0][0] + b1 * p1[0][1]

        a2 = p2[1][1] - p2[0][1]
        b2 = p2[0][0] - p2[1][0]
        c2 = a2 * p2[0][0] + b2 * p2[0][1]

        x = int((c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1))
        y = int((a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1))

        return x, y   
        
    def setToDefault():
        sliderXT1.setValue(0)
        sliderXT2.setValue(0)
        sliderXB1.setValue(0)
        sliderXB2.setValue(0)
        sliderYL1.setValue(0)
        sliderYL2.setValue(0)
        sliderYR1.setValue(0)
        sliderYR2.setValue(0)

    def tryFitToRectagle():
        try:
            pts1 = np.float32([point1,point2,point3,point4])
            pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    
            M = cv.getPerspectiveTransform(pts1,pts2)
            
            dst = cv.warpPerspective(inputImage[-1],M,(300,300))
            
            pixmap = imgToPixmap(Image.fromarray(dst, "RGB"))
            
            functionalAreas[2].setPixmap(pixmap)
        except:
            globalFunc.logDialog("ERR: Probably no image cant be fitted")
        
    def saveChanges():
        globalFunc.addImageDict("perspective")
    
    #LAYOUT 
    
    try:
        hei, wid, _ = inputImage[-1].shape
    except:
        hei = 0
        wid = 0
        
        globalFunc.logDialog("ERR: No image loaded")
        
    sliderXval = int(wid*2)
    sliderYval = int(hei*2)
    
    perspectiveWidget = QWidget(objectName = "perspective")
    perspectiveWidgetLayout = QGridLayout()
    slidersBox = QBoxLayout(2)
    
    sliderXT1 = QSlider(Qt.Horizontal, objectName = "sliderXT1")
    sliderXT1.setMinimum(-sliderXval)
    sliderXT1.setMaximum(sliderXval)
    sliderXT1.setTickInterval(100)
    sliderXT1.setTickPosition(QSlider.TicksBelow)
    sliderXT1.valueChanged.connect(changeValueSlider)
    
    sliderXB1 = QSlider(Qt.Horizontal, objectName = "sliderXB1")
    sliderXB1.setMinimum(-sliderXval)
    sliderXB1.setMaximum(sliderXval)
    sliderXB1.setTickInterval(100)
    sliderXB1.setTickPosition(QSlider.TicksBelow)
    sliderXB1.valueChanged.connect(changeValueSlider)
    
    sliderXT2 = QSlider(Qt.Horizontal, objectName = "sliderXT2")
    sliderXT2.setMinimum(-sliderXval)
    sliderXT2.setMaximum(sliderXval)
    sliderXT2.setTickInterval(100)
    sliderXT2.setTickPosition(QSlider.TicksBelow)
    sliderXT2.valueChanged.connect(changeValueSlider)
    
    sliderXB2 = QSlider(Qt.Horizontal, objectName = "sliderXB2")
    sliderXB2.setMinimum(-sliderXval)
    sliderXB2.setMaximum(sliderXval)
    sliderXB2.setTickInterval(100)
    sliderXB2.setTickPosition(QSlider.TicksBelow)
    sliderXB2.valueChanged.connect(changeValueSlider)
    
    sliderYL1 = QSlider(Qt.Horizontal, objectName = "sliderYL1")
    sliderYL1.setMinimum(-sliderYval)
    sliderYL1.setMaximum(sliderYval)
    sliderYL1.setTickInterval(100)
    sliderYL1.setTickPosition(QSlider.TicksBelow)
    sliderYL1.valueChanged.connect(changeValueSlider)
    
    sliderYR1 = QSlider(Qt.Horizontal, objectName = "sliderYR1")
    sliderYR1.setMinimum(-sliderYval)
    sliderYR1.setMaximum(sliderYval)
    sliderYR1.setTickInterval(100)
    sliderYR1.setTickPosition(QSlider.TicksBelow)
    sliderYR1.valueChanged.connect(changeValueSlider)
    
    sliderYL2 = QSlider(Qt.Horizontal, objectName = "sliderYL2")
    sliderYL2.setMinimum(-sliderYval)
    sliderYL2.setMaximum(sliderYval)
    sliderYL2.setTickInterval(100)
    sliderYL2.setTickPosition(QSlider.TicksBelow)
    sliderYL2.valueChanged.connect(changeValueSlider)
    
    sliderYR2 = QSlider(Qt.Horizontal, objectName = "sliderYR2")
    sliderYR2.setMinimum(-sliderYval)
    sliderYR2.setMaximum(sliderYval)
    sliderYR2.setTickInterval(100)
    sliderYR2.setTickPosition(QSlider.TicksBelow)
    sliderYR2.valueChanged.connect(changeValueSlider)
    
    slidersBox.addWidget(QLabel("Cyan line"))
    slidersBox.addWidget(sliderXT1)
    slidersBox.addWidget(sliderXB1)
    slidersBox.addWidget(QLabel("Magenta line"))
    slidersBox.addWidget(sliderYL1)
    slidersBox.addWidget(sliderYR1)
    slidersBox.addWidget(QLabel("Yellow line"))
    slidersBox.addWidget(sliderXT2)
    slidersBox.addWidget(sliderXB2)
    slidersBox.addWidget(QLabel("Black line"))
    slidersBox.addWidget(sliderYL2)
    slidersBox.addWidget(sliderYR2)
    
    exampleLabel = QLabel()
    size = 150
    example = np.zeros((size,size,4), np.uint8)
    cv.line(example, (size, 0), (0, 0), (255, 0, 255, 255), 50)
    cv.line(example, (0, 0), (0, size), (0, 255, 255, 255), 50)    
    cv.line(example, (0, size), (size, size), (0, 0, 0, 255), 50)
    cv.line(example, (size, size), (size, 0), (255, 255, 0, 255), 50)
    
    example = example[:]
    pixmap = imgToPixmap(Image.fromarray(example, "RGBA"))
        
    exampleLabel.setPixmap(pixmap)    
    
    slidersBox.addWidget(exampleLabel,0,Qt.AlignCenter)
    
    slidersBox.addWidget(QLabel(" "),2)
    
    #maip buttns init
    perspectiveManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Discard")
    tryFitBtn = QPushButton("Try fit")
    saveBtn = QPushButton("Save")
    
    discardBtn.clicked.connect(setToDefault)
    tryFitBtn.clicked.connect(tryFitToRectagle)
    saveBtn.clicked.connect(saveChanges)
    
    perspectiveManipBtns.addWidget(discardBtn)
    perspectiveManipBtns.addWidget(tryFitBtn)
    perspectiveManipBtns.addWidget(saveBtn)
    
    perspectiveWidgetLayout.addLayout(slidersBox,           0,0)
    perspectiveWidgetLayout.addLayout(perspectiveManipBtns, 1,0)
    
    perspectiveWidget.setLayout(perspectiveWidgetLayout)
    return perspectiveWidget