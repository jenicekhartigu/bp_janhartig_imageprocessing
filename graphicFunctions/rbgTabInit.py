import re
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

def rgbWidgetInit(disAreas, logDisp):
    for i in disAreas:
        functionalAreas.append(i)
        
    for i in logDisp:
        logDisplay.append(i)

    try:
        pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
        inputImage.append(np.asarray(pixmapImage))
    except:
        logDisplay[1].append("WARNING: No image loaded")
            
    def getValueDisplayValues():
        r = int(rgbValueDisplay[0].toPlainText())
        g = int(rgbValueDisplay[1].toPlainText())
        b = int(rgbValueDisplay[2].toPlainText())
        return r, g, b
    
    def rgb_to_hex():
        r, g, b = getValueDisplayValues()
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
    def hex_to_rgb(hex):
        hex = hex.lstrip('#')
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)

        return r, g, b
    
    def getQColor():
        r, g, b = getValueDisplayValues()
        color = QColor(r,g,b)
        return color
    
    def changeValueSliders():
        sender = QObject().sender()
        senderName = sender.objectName()
        
        if senderName == "red":
            rgbValueDisplay[0].setText(str(sender.value()))
            rgbValueDisplay[0].setAlignment(Qt.AlignRight)
        if senderName == "green":
            rgbValueDisplay[1].setText(str(sender.value()))
            rgbValueDisplay[1].setAlignment(Qt.AlignRight)
        if senderName == "blue":
            rgbValueDisplay[2].setText(str(sender.value()))
            rgbValueDisplay[2].setAlignment(Qt.AlignRight)
            
        try:
            r, g, b = getValueDisplayValues()
            rgbSliders[0].setValue(r)
            rgbSliders[1].setValue(g)
            rgbSliders[2].setValue(b)
                
            hexValueDisplay.setText(rgb_to_hex())
            
            color = getQColor()
            rgbColorLabel.setStyleSheet("background-color: {}".format(color.name()))
            
            filterSettedValues()
        except:
            None
        
    def changeValueHex():
        try:
            hex = hexValueDisplay.toPlainText()
            
            h = hex.lstrip('#')
            r, g, b = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
            
            rgbSliders[0].setValue(r)
            rgbSliders[1].setValue(g)
            rgbSliders[2].setValue(b)
            
        except:
            None
            
    def changeValueTolerance():
        filterSettedValues()
        
    def filterSettedValues():
        try:
            hexName = QObject().sender().objectName()
            if re.match(r'^#[0-9a-fA-F]{6}$', hexName):
                r, g, b = hex_to_rgb(hexName)
                
            else:
                r, g, b = getValueDisplayValues()
                
            tol = toleranceSlider.value()
                
            #get cv image from functionalAreas
            original_image = inputImage[-1]
            
            mask = cv.inRange(original_image, np.array([r - tol, g - tol, b - tol]), np.array([r + tol, g + tol, b + tol]))
                
            combined_mask = mask
            combined_mask_inv = 255 - combined_mask

            combined_mask_rgb = cv.cvtColor(combined_mask_inv, cv.COLOR_GRAY2BGR)

            final = cv.max(original_image, combined_mask_rgb)
            
            img = Image.fromarray(final, "RGB")
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

    def deleteItemsOfLayout(all):
        hexName = QObject().sender().objectName()
        if all == True:
            for i in iter(selectedColorDict):
                for _ in range(selectedColorDict[i].count()):
                    colWid = selectedColorDict[i].itemAt(0).widget()
                    colWid.setParent(None)
                selectedColorDict.pop(i)
                selectedColorPILDict.pop(i)
                break
            
        for i in iter(selectedColorDict):
            boxMenuName = selectedColorDict[i].objectName()
            if hexName == boxMenuName:
                for _ in range(selectedColorDict[i].count()):
                    colWid = selectedColorDict[i].itemAt(0).widget()
                    colWid.setParent(None)
                
                selectedColorDict.pop(i)
                selectedColorPILDict.pop(i)
                break
    
    deleteItemsOfLayout(True)
    
    def addColorToList():
        #selected color layout
        actualColorName = str(hexValueDisplay.toPlainText())
        if actualColorName not in selectedColorDict.keys():
            colorPanel = QHBoxLayout(objectName = actualColorName)
            
            color = QLabel()
            actualColor = getQColor()
            color.setStyleSheet("background-color: {}".format(actualColor.name()))
        
            hexName = QLabel(actualColorName)
            
            r, g, b = getValueDisplayValues()
            rgbName = QLabel(f"R:{r} G:{g} B:{b}")
            
            tolerance = QLabel(f"Threshold {toleranceSlider.value()}")
            
            showColorBtn = QPushButton("Show selected", objectName = actualColorName)
            showColorBtn.clicked.connect(showSelectedColor)
            
            deleteLayoutBtn = QPushButton("Remove color", objectName = actualColorName)
            deleteLayoutBtn.clicked.connect(deleteItemsOfLayout)
            
            colorPanel.addWidget(color)
            colorPanel.addWidget(hexName)
            colorPanel.addWidget(rgbName)
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
        for i in range(len(rgbValueDisplay)):
            rgbSliders[i].setValue(0)
        toleranceSlider.setValue(255)
        
    def white_to_transparency(img):
        x = np.asarray(img.convert('RGBA')).copy()
        x[:, :, 3] = (255 * (x[:, :, :3] != 255).any(axis=2)).astype(np.uint8)
        return Image.fromarray(x)

    def mergeColor():
        try:
            mergedfile = None
            
            hei = functionalAreas[2].pixmap().size().height()
            wid = functionalAreas[2].pixmap().size().width()
            
            mergedfile = Image.new('RGBA', (wid, hei) , (255,255,255,0))
            
            for i in selectedColorPILDict.keys():

                selectedColorPILDict[i] = white_to_transparency(selectedColorPILDict[i])
                mergedfile.paste(selectedColorPILDict[i], (0,0), mask = selectedColorPILDict[i])
                
            if mergedfile == None:
                globalFunc.logDialog("ERR: Layers cant be merged")
            else:
                pixmap = imgToPixmap(mergedfile)
                functionalAreas[2].setPixmap(pixmap)
                globalFunc.addImageDict("rgbMerge")
        except:
            globalFunc.logDialog("ERR: During merging selected layers")
            

    #Layouts   
    rgbWidget = QWidget(objectName = "RGB")
    rgbWidgetLayout = QGridLayout()
    
    hexAndToleranceLabel = QBoxLayout(0)
    hexAndToleranceInput = QBoxLayout(0)
    
    rgbShowColorLayout = QBoxLayout(0)
    
    selectedColorsLayout = QBoxLayout(2)
    
    rgbManipBtnLayout = QBoxLayout(0)
    
    #Labels
    rLabel = QLabel("Red part")
    gLabel = QLabel("Green part")
    bLabel = QLabel("Blue part")
    
    hexValue = QLabel("Hexadecimal Value")
    toleranceValue = QLabel("Tolerance")
    
    rgbColorLabel = QLabel(" Picked color")
    addBtn = QPushButton("Add selected color")
    
    emptyLabel = QLabel("tady")
    
    #Buttons
    discardBtn = QPushButton("Discard")
    mergeBtn = QPushButton("Merge")
    
    addBtn.clicked.connect(addColorToList)
    
    discardBtn.clicked.connect(setToDefault)
    mergeBtn.clicked.connect(mergeColor)
    
    #variables
    rgbSliderNames = ["red","green","blue"]
    rgbSliders = []
    rgbValueDisplay = []
    
    for name in rgbSliderNames:
        #sliders creation
        slider = QSlider(Qt.Horizontal, objectName = name)
        slider.setMinimum(0)
        slider.setMaximum(255)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.valueChanged.connect(changeValueSliders)
        rgbSliders.append(slider)
        
        #slider value display
        valueDisplay = QTextEdit()
        valueDisplay.setText("0")
        valueDisplay.setMaximumSize(60,30)
        valueDisplay.setAlignment(Qt.AlignRight)
        valueDisplay.textChanged.connect(changeValueSliders)
        rgbValueDisplay.append(valueDisplay)
    
    #hexadecimal definition of color    
    hexValueDisplay = QTextEdit()
    hexValueDisplay.setText("#000000")
    hexValueDisplay.textChanged.connect(changeValueHex)
    hexValueDisplay.setMaximumHeight(30)
    
    # tolerance slider
    toleranceSlider = QSlider(Qt.Horizontal)
    toleranceSlider.setMinimum(0)
    toleranceSlider.setMaximum(255)
    toleranceSlider.setValue(255)
    toleranceSlider.valueChanged.connect(changeValueTolerance)
    toleranceSlider.setMaximumHeight(30)
    
    #rgb hex and tolerance widget making
    hexAndToleranceLabel.addWidget(hexValue)
    hexAndToleranceLabel.addWidget(toleranceValue)
    hexAndToleranceInput.addWidget(hexValueDisplay)
    hexAndToleranceInput.addWidget(toleranceSlider)
    
    #color adding
    rgbShowColorLayout.addWidget(rgbColorLabel)
    rgbShowColorLayout.addWidget(addBtn)
    
    #rbg manip bnts widget making
    rgbManipBtnLayout.addWidget(discardBtn)
    rgbManipBtnLayout.addWidget(QLabel(""))
    rgbManipBtnLayout.addWidget(mergeBtn)
    
    #rgb widget making
    #slidery
    rgbWidgetLayout.addWidget(rLabel, 0,0)
    rgbWidgetLayout.addWidget(rgbSliders[0], 1,0)
    rgbWidgetLayout.addWidget(rgbValueDisplay[0], 1,1)
    
    rgbWidgetLayout.addWidget(gLabel, 2,0)
    rgbWidgetLayout.addWidget(rgbSliders[1], 3,0)
    rgbWidgetLayout.addWidget(rgbValueDisplay[1], 3,1)
    
    rgbWidgetLayout.addWidget(bLabel, 4,0)
    rgbWidgetLayout.addWidget(rgbSliders[2], 5,0)
    rgbWidgetLayout.addWidget(rgbValueDisplay[2], 5,1)
    
    rgbWidgetLayout.addLayout(hexAndToleranceLabel, 6, 0,1,0)
    rgbWidgetLayout.addLayout(hexAndToleranceInput, 7, 0,1,0)
    
    rgbWidgetLayout.addLayout(rgbShowColorLayout, 8,0,1,0)
    
    #barvicky
    rgbWidgetLayout.addLayout(selectedColorsLayout, 9, 0, 1,0)
    
    rgbWidgetLayout.addWidget(emptyLabel,10,0,1,0)
    
    rgbWidgetLayout.addLayout(rgbManipBtnLayout, 11,0,1,0)
    
    rgbWidgetLayout.setRowStretch(10,2)
    
    rgbWidget.setLayout(rgbWidgetLayout)
    
    return rgbWidget