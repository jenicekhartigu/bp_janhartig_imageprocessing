from matplotlib import pyplot as plt
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

def imgToPixmap(image):
    im2 = image.convert("RGBA")
    data = im2.tobytes("raw", "BGRA")
    qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap

def grayWidgetInit(disAreas, logDisp):
    for i in disAreas:
        functionalAreas.append(i)
        
    for i in logDisp:
        logDisplay.append(i)
        
    try:
        pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
        inputImage.append(np.asarray(pixmapImage))
    except:
        globalFunc.logDialog("WARNING: Není načten obrázek")
                
    def activeColorSpace(): 
        absPosRBtn = abs(radioBtnGroup.checkedId()) - 1
        
        def disableGRAY():
            grayShowBtn.setDisabled(1)
        
        def disableRGB():
            rgbComboBox.setDisabled(1)
            rgbShowBtn.setDisabled(1)
            
        def disableHSV():
            hsvComboBox.setDisabled(1)
            hsvShowBtn.setDisabled(1)
            
        def disableYCBCR():
            ycbcrComboBox.setDisabled(1)
            ycbcrShowBtn.setDisabled(1)
            
        if absPosRBtn == 1:
            grayShowBtn.setEnabled(1)
            disableRGB()
            disableHSV()
            disableYCBCR()
            
        if absPosRBtn == 2:
            rgbComboBox.setEnabled(1)
            rgbShowBtn.setEnabled(1)
            disableGRAY()
            disableHSV()
            disableYCBCR()
            
        if absPosRBtn == 3:
            hsvComboBox.setEnabled(1)
            hsvShowBtn.setEnabled(1)
            disableRGB()
            disableGRAY()
            disableYCBCR()
            
        if absPosRBtn == 4:
            disableRGB()
            disableHSV()
            disableGRAY()
            ycbcrComboBox.setEnabled(1)
            ycbcrShowBtn.setEnabled(1)

        return absPosRBtn 

    def getActiveColorLayer():
        showSelectedColor()
        
    def setToDefault():

        return None
    
    def saveChanges():
        globalFunc.addImageDict("colorSpaceChange")
        return None
    
    def showSelectedColor():
        colorSpace = activeColorSpace()
        grayState = -1
        
        if colorSpace == 1:
            colorLayer = 0
            
        if colorSpace == 2: 
            colorLayer = rgbComboBox.currentIndex()
            
        if colorSpace == 3: 
            colorLayer = hsvComboBox.currentIndex()
            
        if colorSpace == 4: 
            colorLayer = ycbcrComboBox.currentIndex()
            
        showLayer(colorSpace, colorLayer)
        
    def checkBoxChecked():
        if trueColorShow.checkState() == 2:
            print("true")
            return True
        else:
            print("false")
            return False
     
    def showLayer(colorSpace, colorLayer):
        try:
            imageArray = inputImage[-1]
            
            if colorSpace == 1:
                # Grayscale
                layer = cv.cvtColor(imageArray, cv.COLOR_BGR2GRAY)
                
                layerImg = Image.fromarray(layer,"L")
            
            elif colorSpace == 2:
                # RGB
                layer = imageArray[:, :, colorLayer ]
                
                layerImg = Image.fromarray(layer,"L")
                
                if checkBoxChecked() == True:
                    imgRGB = cv.cvtColor(imageArray, cv.COLOR_BGR2RGB)
                    
                    b,g,r = cv.split(imgRGB)
                    k = np.zeros_like(b)
                    
                    if colorLayer == 0:
                        res = cv.merge([b,k,k])
                        
                    if colorLayer == 1:
                        res = cv.merge([k,g,k])
                
                    if colorLayer == 2:
                        res = cv.merge([k,k,r])
                        
                    layerImg = Image.fromarray(res,"RGB")
                        
                    
            
            elif colorSpace == 3:
                # HSV
                hsv_planes = cv.split(cv.cvtColor(imageArray, cv.COLOR_BGR2HSV))
                layer = hsv_planes[colorLayer]
                
                layerImg = Image.fromarray(layer,"L")
                
                if checkBoxChecked() == True:
                    imgHSV = cv.cvtColor(imageArray, cv.COLOR_BGR2HSV)
                    
                    if colorLayer == 0:
                        res = imgHSV[..., 0]
                        res = cv.applyColorMap(res, cv.COLORMAP_HSV)
                        
                        layerImg = Image.fromarray(res,"RGB")

                    if colorLayer == 1:
                        res = imgHSV[..., 1]
                        res = cv.applyColorMap(res, cv.COLORMAP_HOT)
                        
                        layerImg = Image.fromarray(res,"RGB")
                    
                    
                    
            
            elif colorSpace == 4:
                # YCbCr
                ycrcb_planes = cv.split(cv.cvtColor(imageArray, cv.COLOR_BGR2YCrCb))
                layer = ycrcb_planes[colorLayer]
                
                layerImg = Image.fromarray(layer,"L")
                
                if checkBoxChecked() == True:
                
                    # Fill Y and Cb with 128 (Y level is middle gray, and Cb is "neutralized").
                    imgYCrCB = cv.cvtColor(imageArray, cv.COLOR_BGR2YCrCb)
                    
                    if colorLayer == 2:
                        onlyCr = imgYCrCB.copy()
                        onlyCr[:, :, 0] = 128
                        onlyCr[:, :, 2] = 128
                        onlyCr_as_bgr = cv.cvtColor(onlyCr, cv.COLOR_YCrCb2BGR)  # Convert to BGR - used for display as false color
                        
                        layerImg = Image.fromarray(onlyCr_as_bgr,"RGB")
                        
                    if colorLayer == 1:
                        onlyCb = imgYCrCB.copy()
                        onlyCb[:, :, 0] = 128
                        onlyCb[:, :, 1] = 128
                        onlyCb_as_bgr = cv.cvtColor(onlyCb, cv.COLOR_YCrCb2BGR)  # Convert to BGR - used for display as false color
                        
                        layerImg = Image.fromarray(onlyCb_as_bgr,"RGB")
                        
            else:
                raise ValueError(f"Unsupported color space: {colorSpace}")
                
            functionalAreas[2].setPixmap(imgToPixmap(layerImg))
            
        except:
            globalFunc.logDialog("ERR: Není nahrán obrázek")
    
        
                
        
    #LAYOUT 
    grayWidget = QWidget(objectName = "gray")
    grayWidgetLayout = QGridLayout()
    
    verticalBoxMain = QBoxLayout(2)
    
    emptyLabel = QLabel(" ")
    
    #gray
    grayBtns = QBoxLayout(0)
    
    grayRBtn = QRadioButton("GRAY",objectName = "gray")
    grayRBtn.clicked.connect(activeColorSpace)
    
    grayShowBtn = QPushButton("Show gray")
    grayShowBtn.clicked.connect(showSelectedColor)
    
    
    grayBtns.addWidget(grayRBtn,1)
    grayBtns.addWidget(emptyLabel,1)
    grayBtns.addWidget(grayShowBtn,1)
    
    
    #rgb
    rgbBtns = QBoxLayout(0)
    
    rgbRBtn = QRadioButton("RGB")
    rgbRBtn.clicked.connect(activeColorSpace)
    
    rgbComboBox = QComboBox()
    rgbComboBoxValues= ["Red channel",
                        "Green channel",
                        "Blue channel"
                        ]
    rgbComboBox.addItems(rgbComboBoxValues)
    rgbComboBox.currentTextChanged.connect(getActiveColorLayer)
    
    
    rgbShowBtn = QPushButton("Show layer")
    rgbShowBtn.clicked.connect(showSelectedColor)
    
    rgbBtns.addWidget(rgbRBtn,1)
    rgbBtns.addWidget(rgbComboBox,1)
    rgbBtns.addWidget(rgbShowBtn,1)
    
    #hsv
    hsvBtns = QBoxLayout(0)
    hsvRBtn = QRadioButton("HSV")
    hsvRBtn.clicked.connect(activeColorSpace)
    
    hsvComboBox = QComboBox()
    hsvComboBoxValues= ["Hue channel",
                        "Saturation channel",
                        "Value channel"
                        ]
    hsvComboBox.addItems(hsvComboBoxValues)
    hsvComboBox.currentTextChanged.connect(getActiveColorLayer)
    
    hsvShowBtn = QPushButton("Show layer")
    hsvShowBtn.clicked.connect(showSelectedColor)
    
    
    hsvBtns.addWidget(hsvRBtn,1)
    hsvBtns.addWidget(hsvComboBox,1)
    hsvBtns.addWidget(hsvShowBtn,1)
    
    #ycbcr
    ycbcrBtns = QBoxLayout(0)
    ycbcrRBtn = QRadioButton("YCbCr")
    ycbcrRBtn.clicked.connect(activeColorSpace)
    
    ycbcrComboBox = QComboBox()
    ycbcrComboBoxValues= ["Y channel",
                        "Chroma blue channel",
                        "Chroma red channel"
                        ]
    ycbcrComboBox.addItems(ycbcrComboBoxValues)
    ycbcrComboBox.currentTextChanged.connect(getActiveColorLayer)
    
    ycbcrShowBtn = QPushButton("Show layer")
    ycbcrShowBtn.clicked.connect(showSelectedColor)
    
    ycbcrBtns.addWidget(ycbcrRBtn,1)
    ycbcrBtns.addWidget(ycbcrComboBox,1)
    ycbcrBtns.addWidget(ycbcrShowBtn,1)
    
    #completation
    
    radioBtnGroup = QButtonGroup()
    radioBtnGroup.addButton(grayRBtn)
    radioBtnGroup.addButton(rgbRBtn)
    radioBtnGroup.addButton(hsvRBtn)
    radioBtnGroup.addButton(ycbcrRBtn)
    
    trueColorShow = QCheckBox("Pro zobrazení pravých barev jednotlivých vrstev")
    trueColorShow.toggled.connect(checkBoxChecked)
    
    verticalBoxMain.addLayout(grayBtns)
    verticalBoxMain.addLayout(rgbBtns)
    verticalBoxMain.addLayout(hsvBtns)
    verticalBoxMain.addLayout(ycbcrBtns)
    verticalBoxMain.addWidget(trueColorShow)
    
    #empty label init
    emptyLabel = QLabel(" ")
    
    #maip buttns init
    grayManipBtns = QBoxLayout(0)
    
    discardBtn = QPushButton("Zahodit")
    saveBtn = QPushButton("Uložit")
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(saveChanges)
    
    grayManipBtns.addWidget(discardBtn)
    grayManipBtns.addWidget(emptyLabel)
    grayManipBtns.addWidget(saveBtn)
    
    #adding all thing of widget together
    grayWidgetLayout.addLayout(verticalBoxMain,        0,0,1,0)
    
    grayWidgetLayout.addWidget(emptyLabel,        1,0,1,0)
    
    grayWidgetLayout.addLayout(grayManipBtns,   2,0,1,0)
    
    grayWidgetLayout.setRowStretch(1,2)
    
    
    
    grayWidget.setLayout(grayWidgetLayout)
    
    grayRBtn.setChecked(True)
    return grayWidget