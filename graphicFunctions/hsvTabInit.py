
import math
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

from PIL import ImageQt


operationBtns = []
functionalAreas = []
logDisplay = []

inputImage = []

selectedColorDict = {}
selectedColorPILDict = {}

def imgToPixmap(image):
    im2 = image.convert("hsvA")
    data = im2.tobytes("raw", "BGRA")
    qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_Ahsv32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap

def hsvWidgetInit(disAreas, logDisp):
    for i in disAreas:
        functionalAreas.append(i)
        
    for i in logDisp:
        logDisplay.append(i)
    
    try:
        pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
        inputImage.append(np.asarray(pixmapImage))

    except: 
        print("no image")
        
        
    def hsv_to_rgb(hue, saturation, value):
        hue = hue / 360.0
        saturation = saturation / 100.0
        value = value / 100.0
        
        

        C = value * saturation
        X = C * (1 - abs(hue * 6 % 2 - 1))
        m = value - C

        if hue < 1 / 6:
            R, G, B = C, X, 0
        elif hue < 1 / 3:
            R, G, B = X, C, 0
        elif hue < 1 / 2:
            R, G, B = 0, C, X
        elif hue < 2 / 3:
            R, G, B = 0, X, C
        elif hue < 5 / 6:
            R, G, B = X, 0, C
        else:
            R, G, B = C, 0, X

        R = (R + m) * 255
        G = (G + m) * 255
        B = (B + m) * 255

        return int(R), int(G), int(B)
    
    def rgb_to_hsv(red, green, blue):
        red = red / 255.0
        green = green / 255.0
        blue = blue / 255.0

        Cmax = max(red, green, blue)
        Cmin = min(red, green, blue)
        delta = Cmax - Cmin

        if delta == 0:
            hue = 0
        elif Cmax == red:
            hue = (((green - blue) / delta) % 6) * 60
        elif Cmax == green:
            hue = (((blue - red) / delta) + 2) * 60
        else:
            hue = (((red - green) / delta) + 4) * 60

        if hue < 0:
            hue += 360

        if Cmax == 0:
            saturation = 0
        else:
            saturation = (delta / Cmax) * 100

        value = Cmax * 100

        return round(hue, 2), round(saturation, 2), round(value, 2)
            
    def getValueDisplayValues():
        h = int(hsvValueDisplay[0].toPlainText())
        s = int(hsvValueDisplay[1].toPlainText())
        v = int(hsvValueDisplay[2].toPlainText())
        
        rgb = hsv_to_rgb(h,s,v)
        
        r, g, b = rgb
        
        return r, g, b
    
    def hsv_to_hex():
        r, g, b = getValueDisplayValues()
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
    def hex_to_hsv(hex):
        hex = hex.lstrip('#')
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)

        return r, g, b
    
    def getQColor():
        r, g, b = getValueDisplayValues()
        color = QColor(r, g, b)
        return color
    
    def changeValueSliders():
        sender = QObject().sender()
        senderName = sender.objectName()
        
        if senderName == "hue":
            hsvValueDisplay[0].setText(str(sender.value()))
            hsvValueDisplay[0].setAlignment(Qt.AlignRight)
        if senderName == "sat":
            hsvValueDisplay[1].setText(str(sender.value()))
            hsvValueDisplay[1].setAlignment(Qt.AlignRight)
        if senderName == "value":
            hsvValueDisplay[2].setText(str(sender.value()))
            hsvValueDisplay[2].setAlignment(Qt.AlignRight)
            
 
        # try:
        #     hue, sat, value = getValueDisplayValues()
        #     hsvSliders[0].setValue(hue)
        #     hsvSliders[1].setValue(sat)
        #     hsvSliders[2].setValue(value)
    
        #     hexValueDisplay.setText(hsv_to_hex())
    
        #     color = getQColor()
        #     hsvColorLabel.setStyleSheet("background-color: {}".format(color.name()))
            
        #     filterSettedValues()
        # except:
        #     None
        
    def changeValueHex():
        try:
            hex = hexValueDisplay.toPlainText()
            
            h = hex.lstrip('#')
            hue, sat, value = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
            
            hsvSliders[0].setValue(hue)
            hsvSliders[1].setValue(sat)
            hsvSliders[2].setValue(value)
            
        except:
            None
            
    def changeValueTolerance():
        filterSettedValues()
        
    def filterSettedValues():
        try:
            hexName = QObject().sender().objectName()
            if re.match(r'^#[0-9a-fA-F]{6}$', hexName):
                hue, sat, value = hex_to_hsv(hexName)
                
            else:
                hue, sat, value = getValueDisplayValues()
                
            tol = toleranceSlider.value()
                
            #get cv image from functionalAreas
            original_image = inputImage[0]
            
            mask = cv.inRange(original_image, np.array([hue - tol, sat - tol, value - tol]), np.array([hue + tol, sat + tol, value + tol]))
                
            combined_mask = mask
            combined_mask_inv = 255 - combined_mask

            combined_mask_hsv = cv.cvtColor(combined_mask_inv, cv.COLOR_GRAY2BGR)

            final = cv.max(original_image, combined_mask_hsv)
            
            img = Image.fromarray(final, "hsv")
            pixmap = imgToPixmap(img)
            
            functionalAreas[2].setPixmap(pixmap)
        except:
            None
    
    def showSelectedColor():
        hexName = QObject().sender().objectName()
        hexValueDisplay.setText(hexName)
        
        try:
            imgFromDict = selectedColorPILDict[hexName]
            selectedColorPixmap = imgToPixmap(imgFromDict)
            
            functionalAreas[2].setPixmap(selectedColorPixmap)
            
        except:
            functionalAreas[2].setText("No loaded image")

    
    def deleteItemsOfLayout():
        hexName = QObject().sender().objectName()
        
        for i in iter(selectedColorDict):
            boxMenuName = selectedColorDict[i].objectName()
            if hexName == boxMenuName:
                for _ in range(selectedColorDict[i].count()):
                    colWid = selectedColorDict[i].itemAt(0).widget()
                    colWid.setParent(None)
                
                selectedColorDict.pop(i)
                selectedColorPILDict.pop(i)
                break
    
    def addColorToList():
        #selected color layout
        actualColorName = str(hexValueDisplay.toPlainText())
        if actualColorName not in selectedColorDict.keys():
            colorPanel = QHBoxLayout(objectName = actualColorName)
            
            color = QLabel()
            actualColor = getQColor()
            color.setStyleSheet("background-color: {}".format(actualColor.name()))
        
            hexName = QLabel(actualColorName)
            
            hue, sat, value = getValueDisplayValues()
            hsvName = QLabel(f"Hue:{hue} Sat:{sat} Val:{value}")
            
            tolerance = QLabel(f"Threshold {toleranceSlider.value()}")
            
            showColorBtn = QPushButton("Show selected", objectName = actualColorName)
            showColorBtn.clicked.connect(showSelectedColor)
            
            deleteLayoutBtn = QPushButton("Remove color", objectName = actualColorName)
            deleteLayoutBtn.clicked.connect(deleteItemsOfLayout)
            
            colorPanel.addWidget(color)
            colorPanel.addWidget(hexName)
            colorPanel.addWidget(hsvName)
            colorPanel.addWidget(tolerance)
            colorPanel.addWidget(showColorBtn)
            colorPanel.addWidget(deleteLayoutBtn)

            selectedColorsLayout.addLayout(colorPanel)
            selectedColorDict[actualColorName] = colorPanel
            
            try:
                actualImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
                selectedColorPILDict.update({actualColorName:actualImage})
            except:
                functionalAreas[2].setText("No loaded image")
                selectedColorPILDict.update({actualColorName:None})
            
        
    
    def setToDefault():
        for i in range(len(hsvValueDisplay)):
            hsvSliders[i].setValue(0)
        toleranceSlider.setValue(255)

    def filterColor():
        resultPic = None
        for i in selectedColorPILDict.keys():
            resultPic = resultPic + selectedColorPILDict[i]
            print(i, selectedColorPILDict[i])
            
        print(resultPic)
        None
            
            
    #Layouts   
    hsvWidget = QWidget(objectName = "RGB")
    hsvWidgetLayout = QGridLayout()
        
    hexAndToleranceLabel = QBoxLayout(0)
    hexAndToleranceInput = QBoxLayout(0)
    
    hsvShowColorLayout = QBoxLayout(0)
        
    selectedColorsLayout = QBoxLayout(2)
    
    hsvManipBtnLayout = QBoxLayout(0)
        
    #Labels
    hLabel = QLabel("Hue")
    sLabel = QLabel("Saturation")
    vLabel = QLabel("Value")
        
    hexValue = QLabel("Hexadecimal Value")
    toleranceValue = QLabel("Tolerance")
    
    hsvColorLabel = QLabel(" Picked color")
    addBtn = QPushButton("Add selected color")
    
    emptyLabel = QLabel("")
    
    #Buttons
    discardBtn = QPushButton("Discard")
    saveBtn = QPushButton("Save")
    
    addBtn.clicked.connect(addColorToList)
    
    discardBtn.clicked.connect(setToDefault)
    saveBtn.clicked.connect(filterColor)
    
    #variables
    hsvSliderNames = ["hue","sat","value"]
    hsvSliders = []
    hsvValueDisplay = []
    
    #setting diferetn boundries for hsv sliders
    #HUE
    hSlider = QSlider(Qt.Horizontal, objectName = "hue")
    hSlider.setMinimum(0)
    hSlider.setMaximum(355)
    hSlider.setTickPosition(QSlider.TicksBelow)
    hSlider.valueChanged.connect(changeValueSliders)
    hsvSliders.append(hSlider)
    
    # #Slider value display
    # valueDisplay = QTextEdit()
    # valueDisplay.setText("0")
    # valueDisplay.setMaximumSize(60,30)
    # valueDisplay.setAlignment(Qt.AlignRight)
    # valueDisplay.textChanged.connect(changeValueSliders)
    # hsvValueDisplay.append(valueDisplay)
    
    #SAT
    sSlider = QSlider(Qt.Horizontal, objectName = "sat")
    sSlider.setMinimum(0)
    sSlider.setMaximum(100)
    sSlider.setTickPosition(QSlider.TicksBelow)
    sSlider.valueChanged.connect(changeValueSliders)
    hsvSliders.append(sSlider)
    
    #VALUE
    
    vSlider = QSlider(Qt.Horizontal, objectName = "value")
    vSlider.setMinimum(0)
    vSlider.setMaximum(100)
    vSlider.setTickPosition(QSlider.TicksBelow)
    vSlider.valueChanged.connect(changeValueSliders)
    hsvSliders.append(vSlider)
    
    
    for _ in hsvSliderNames:
        #Slider value display
        valueDisplay = QTextEdit()
        valueDisplay.setText("0")
        valueDisplay.setMaximumSize(60,30)
        valueDisplay.setAlignment(Qt.AlignRight)
        valueDisplay.textChanged.connect(changeValueSliders)
        hsvValueDisplay.append(valueDisplay)
    
    #hexadecimal definition of color    
    hexValueDisplay = QTextEdit()
    hexValueDisplay.setText("#000000")
    hexValueDisplay.textChanged.connect(changeValueHex)
    hexValueDisplay.setMaximumHeight(30)
    
    # tolerance Slider
    toleranceSlider = QSlider(Qt.Horizontal)
    toleranceSlider.setMinimum(0)
    toleranceSlider.setMaximum(255)
    toleranceSlider.setValue(255)
    toleranceSlider.valueChanged.connect(changeValueTolerance)
    toleranceSlider.setMaximumHeight(30)
    
    #hsv hex and tolerance widget making
    hexAndToleranceLabel.addWidget(hexValue)
    hexAndToleranceLabel.addWidget(toleranceValue)
    hexAndToleranceInput.addWidget(hexValueDisplay)
    hexAndToleranceInput.addWidget(toleranceSlider)
    
    #color adding
    hsvShowColorLayout.addWidget(hsvColorLabel)
    hsvShowColorLayout.addWidget(addBtn)
    
    #rbg manip bnts widget making
    hsvManipBtnLayout.addWidget(discardBtn)
    hsvManipBtnLayout.addWidget(QLabel(""))
    hsvManipBtnLayout.addWidget(saveBtn)
    
    #hsv widget making
    #slidery
    hsvWidgetLayout.addWidget(hLabel, 0,0)
    hsvWidgetLayout.addWidget(hsvSliders[0], 1,0)
    hsvWidgetLayout.addWidget(hsvValueDisplay[0], 1,1)
    
    hsvWidgetLayout.addWidget(sLabel, 2,0)
    hsvWidgetLayout.addWidget(hsvSliders[1], 3,0)
    hsvWidgetLayout.addWidget(hsvValueDisplay[1], 3,1)
    
    hsvWidgetLayout.addWidget(vLabel, 4,0)
    hsvWidgetLayout.addWidget(hsvSliders[2], 5,0)
    hsvWidgetLayout.addWidget(hsvValueDisplay[2], 5,1)
    
    hsvWidgetLayout.addLayout(hexAndToleranceLabel, 6, 0,1,0)
    hsvWidgetLayout.addLayout(hexAndToleranceInput, 7, 0,1,0)
    
    hsvWidgetLayout.addLayout(hsvShowColorLayout, 8,0,1,0)
    
    #barvicky
    hsvWidgetLayout.addLayout(selectedColorsLayout, 9, 0, 1,0)
    
    hsvWidgetLayout.addWidget(emptyLabel,10,0,1,0)
    
    hsvWidgetLayout.addLayout(hsvManipBtnLayout, 11,0,1,0)
    
    hsvWidgetLayout.setRowStretch(10,2)
    
    hsvWidget.setLayout(hsvWidgetLayout)
    
    return hsvWidget