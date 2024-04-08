import random
import re
import numpy as np
import matplotlib.pyplot as plt

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import cv2 as cv2

from PIL import ImageQt
from PIL import Image

from graphicFunc import *

operationBtns = []
functionalAreas = []
logDisplay = []

imageDictCache = QPixmapCache()
imageDictCache.setCacheLimit(655360)

imageDict = {}
logger = [0]

isHistSetted = []

counter = [0]
index = len(imageDict) - 1

def addImageDict(caller):
    global index
    index = index + 1
    counter[0] = counter[0] + 1
    caller = str(caller) + str(counter[0])
    print(caller)
    print(index)
    imageDict[caller] = [None]
    
    imageDictCache.insert(caller, functionalAreas[2].pixmap())
    

def randColor():
    color = QtGui.QColor(*random.sample(range(255), 3))
    return color

def logDialog(message):
    if message != logger[0]:
        
        logDisplay[1].append(message)
        logger[0] = message
    
def reinitTabDictonaries():
    rgbWidgetInit(functionalAreas, logDisplay)
    hsvWidgetInit(functionalAreas, logDisplay)
    grayWidgetInit(functionalAreas, logDisplay)
    
    rotateWidgetInit(functionalAreas, logDisplay)
    shiftingWidgetInit(functionalAreas, logDisplay)
    perspectiveWidgetInit(functionalAreas, logDisplay)
    
    convolutionWidgetInit(functionalAreas, logDisplay)
    averagingWidgetInit(functionalAreas, logDisplay)
    gaussianWidgetInit(functionalAreas, logDisplay)
    medianWidgetInit(functionalAreas, logDisplay)
    gaussianThreshWidgetInit(functionalAreas, logDisplay)
    meanThreshWidgetInit(functionalAreas, logDisplay)
    
    blackhatWidgetInit(functionalAreas, logDisplay)
    tophatWidgetInit(functionalAreas, logDisplay)
    closingWidgetInit(functionalAreas, logDisplay)
    openingWidgetInit(functionalAreas, logDisplay)
    dilationWidgetInit(functionalAreas, logDisplay)
    erosionWidgetInit(functionalAreas, logDisplay)
    gradientWidgetInit(functionalAreas, logDisplay)
    
def imgToPixmap(image):
    im2 = image.convert("RGBA")
    data = im2.tobytes("raw", "BGRA")
    qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap

# file mapin menu    
def fileManipulation():
    currentState = operationBtns[0].currentText()
    
    #open file and adding to widget
    if currentState == "Open file":
        try:
            imagePath, _ = QFileDialog.getOpenFileName()
            pixmap = QPixmap(imagePath)
            
            labelWidth = functionalAreas[2].width()
            labelHeight = functionalAreas[2].height()
            
            pixmap1 = pixmap.scaled(labelWidth,labelHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            
            functionalAreas[2].setPixmap(pixmap1)
            
            imageDictCache.clear()
            imageDict.clear()
            
            imageDict["original0"] = [None]
            imageDictCache.insert("original0", pixmap1)
            
            global index
            index = index + 1
            
            logDialog("Picture is loaded from " + imagePath)
            
            
            reinitTabDictonaries()
        except:
            logDialog("ERR: Picture cant be loaded")
        
    elif currentState == "Save as":
        # try:
            dialog = QFileDialog()
            dialog.setNameFilter("*.jpg")
            dialog.setDefaultSuffix(".jpg")
            clickedOK = dialog.exec()
            if clickedOK:
                print(functionalAreas[2].pixmap().save(dialog.selectedFiles()[0]))
                
        # except:
        #     logDialog("ERR: Picture cant be saved")
        
    elif currentState == "Exit":
        logDialog("Not implemented")
    
def helpManipulation():
    logDialog("Not implemented")

def functionSelected():
    currentState = functionalAreas[0].currentIndex()
    if currentState == 1:
        functionalAreas[1].clear()
        
        functionHandling(0)
        
    if currentState == 2:
        functionalAreas[1].clear()
        
        functionHandling(1)
        
    if currentState == 3:
        functionalAreas[1].clear()
        
        functionHandling(2)
        
    if currentState == 4:
        functionalAreas[1].clear()
        
        functionHandling(3)
        
    logDialog("Function selector: " + functionalAreas[0].currentText())
    
def showPrevious():
    try:
        global index
        if index == -1:
            print("Slovník je prázdný.")
            originalImage()
            return
        else:
            index -= 1
            findPixmapInDict(index)
            
        logDialog("Showing previous change")
                
    except:
        logDialog("ERR: Durign showHistory()")


def showNext():
    try:
        global index
        if index == len(imageDict) - 1:
            print("Dosáhli jste na poslední prvek")
            # showLast()
            return
        else:
            index += 1
            findPixmapInDict(index)
            
        logDialog("Showing next change")
    except:
        logDialog("ERR: Durign showHistory()")

    
    
def findPixmapInDict(index):
    for key in imageDict.keys():
            match = re.search(r"\d+", key)
            if index == int(match.group(0)):
                print(key)
                functionalAreas[2].setPixmap(imageDictCache.find(key))
                
                reinitTabDictonaries()
    
    
# AREA MANIP
def selectArea():
    try:
        # making openCV image
        pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
        img = cv2.cvtColor(np.array(pixmapImage), cv2.COLOR_RGB2BGR)
        
        
    except:
        logDialog("ERR: No image imported")
    
    try:
        roi = cv2.selectROI("Select area", img)
        selecetedArea = img[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
        
        newImage = cv2.cvtColor(selecetedArea, cv2.COLOR_BGR2RGB)
        imgArea = Image.fromarray(newImage)
        pixmap = imgToPixmap(imgArea)
        
        functionalAreas[2].setPixmap(pixmap)
        
        addImageDict("selectArea")
        
        reinitTabDictonaries()
    except:
        logDialog("ERR: Error during selecting area")
    
def originalImage():
    try:
        functionalAreas[2].setPixmap(imageDictCache.find("original0"))
        
        reinitTabDictonaries()
    except:
        logDialog("ERR: Original cant be showed")
        
def showLast():
    try:
        print("posledni ",imageDict.keys()[-1])
        
        
        # functionalAreas[2].setPixmap(pixmap)
    except:
        logDialog("ERR: Last cant be showed")
    

def expandImage():
    try:
        wid = functionalAreas[2].width()
        hei = functionalAreas[2].height()
        
        pixmap = functionalAreas[2].pixmap().scaled(wid,hei, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        functionalAreas[2].setPixmap(pixmap)
        
        addImageDict("expandImage")
        
        reinitTabDictonaries()
    except:
        logDialog("ERR: Image cant be expanded")
    


#HISTOGRAM MANIP        
def equalizePicture():
    sender = QObject().sender()
    senderName = sender.objectName()
    try:
        PILImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())

        if senderName == "gray":
            grayArr = np.array(PILImage)
            
            gray = cv2.cvtColor(grayArr, cv2.COLOR_BGR2GRAY)

            equalized_gray = cv2.equalizeHist(gray)

        else:

            PILImage.putalpha(1)
            r, g, b, a = PILImage.split()
            
            r_image_eq = cv2.equalizeHist(np.array(r))
            g_image_eq = cv2.equalizeHist(np.array(g))
            b_image_eq = cv2.equalizeHist(np.array(b))
            
            
            image_eq = cv2.merge((r_image_eq, g_image_eq, b_image_eq))
            
        pixmap = imgToPixmap(Image.fromarray(image_eq))
        functionalAreas[2].setPixmap(pixmap)
        addImageDict("equalized")
        
    except:
        logDialog("ERR: No image to equalize")

def initHistogramWindow():
    pixmap = showHistogram()
    
    rgbEqualBtn = QPushButton("Equalize rgb")
    grayEqualBtn = QPushButton("Equalize gray", objectName = "gray")
    
    try:
        functionalAreas[3].setPixmap(pixmap)
    except:
        labelWidth = functionalAreas[3].width()
        labelHeight = functionalAreas[3].height()
        
        if labelHeight > labelWidth:
            labelHeight = labelWidth
        else:
            labelWidth = labelHeight

        placeHolder = QPixmap(labelWidth,labelHeight)
        placeHolder.fill(QColor('#f0f0f0'))
        functionalAreas[3].setStyleSheet("border: 1px solid #d9d9d9;")
 
        
        functionalAreas[3].setPixmap(placeHolder)
        
        logDialog("ERR: No image to equalize")
        
    rgbEqualBtn.clicked.connect(equalizePicture)
    grayEqualBtn.clicked.connect(equalizePicture)    
        
    histBtnLayout = QHBoxLayout()

    histBtnLayout.addWidget(rgbEqualBtn)
    histBtnLayout.addWidget(grayEqualBtn)
    
    emptyLabel = QLabel("")
    
    if isHistSetted[0] == False:
        functionalAreas[4].addLayout(histBtnLayout)
            
        functionalAreas[4].addWidget(emptyLabel)
        isHistSetted[0] = True

    functionalAreas[4].setStretch(2, 2)
    
def drawHistogram(hist_r, hist_g, hist_b, grayScale):
    
    plt.figure(figsize=(6, 6))
    
    # Vytvoření grafu
    
    plt.plot(hist_b, color='red', label='R', linewidth=2)
    plt.plot(hist_g, color='green', label='G', linewidth=2)
    plt.plot(hist_r, color='blue', label='B', linewidth=2)

    plt.plot(grayScale, color='gray', label='Gray', linewidth=2)

    # Přidání popisků a titulu
    plt.title('Histogram barev')
    plt.xlabel('Intenzita barev')
    plt.ylabel('Počet pixelů')
    plt.legend()
    
    fig = plt.gcf()
    
    fig.canvas.draw()
    
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # opencv format
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    res = Image.fromarray(img)
    res = imgToPixmap(res)
    
    labelWidth = functionalAreas[3].width()
    labelHeight = functionalAreas[3].height()
            
    pixmap = res.scaled(labelWidth,labelHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    
    return pixmap

def showHistogram():
    reinitTabDictonaries()
    hist_r = 0
    hist_g = 0
    hist_b = 0
    
    grayScale = 0
    
    # Načtení obrázku
    try:
        pixmapImage = ImageQt.fromqpixmap(functionalAreas[2].pixmap())
        # making openCV image
        cvImg = cv2.cvtColor(np.array(pixmapImage), cv2.COLOR_RGB2BGR)
        

        # Konverze obrázku z BGR do RGB
        img_rgb = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
        img_gray = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)

        # Vytvoření histogramu pro každou složku barvy
        hist_r = cv2.calcHist([img_rgb], [0], None, [256], [0, 256])
        hist_g = cv2.calcHist([img_rgb], [1], None, [256], [0, 256])
        hist_b = cv2.calcHist([img_rgb], [2], None, [256], [0, 256])
        
        grayScale  = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
    except:
        logDialog("ERR: No image imported")
        
        
    pixmap = drawHistogram(hist_r, hist_g, hist_b, grayScale)
    
    return pixmap


def logicInit(app, operBtns,disAreas,logDisp):
    for i in operBtns:
        operationBtns.append(i)
    for i in disAreas:
        functionalAreas.append(i)
    for i in logDisp:
        logDisplay.append(i)
     
    isHistSetted.append(False)
        
    graphicFuncInit(operBtns, disAreas, logDisp)
 
    # file and help manipulation
    operationBtns[0].currentTextChanged.connect(fileManipulation)
    operationBtns[1].currentTextChanged.connect(helpManipulation)
    
    # backward and forward manipulation
    operationBtns[2].clicked.connect(showPrevious)
    operationBtns[3].clicked.connect(showNext)
    
    # next static functions
    operationBtns[4].clicked.connect(initHistogramWindow)
    
    operationBtns[5].clicked.connect(originalImage)
    
    operationBtns[6].clicked.connect(expandImage)
    
    operationBtns[7].clicked.connect(selectArea)
    
    operationBtns[8].clicked.connect(showLast)
    
    # functions and tab manipulation
    functionalAreas[0].currentTextChanged.connect(functionSelected)
    
    
    

