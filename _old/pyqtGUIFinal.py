
import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PIL import ImageQt
from functionsGuiFinal import *

labels = []

#1st choice
colorSchemeChooseGroup = QButtonGroup()
colorSchemeChoose = []

#2nd choice
rgbColorChooseGroup = QButtonGroup()
rgbColorChoose = []
hsvColorChooseGroup = QButtonGroup()
hsvColorChoose = []
ycbcrColorChooseGroup = QButtonGroup()
ycbcrColorChoose = []
twoDimColorChoose = [rgbColorChoose,hsvColorChoose,ycbcrColorChoose]

#3rd choice
edgeNoiseChooseGroup = QButtonGroup() 
edgeNoiseChoose = []

#4th choice
binSegmentationChooseGroup = QButtonGroup()
binSegmentationChoose = []

#5th choice
morphOperationsChooseGroup = QButtonGroup()
morphOperationsChoose = []

#global vars
logChanges = ""
imageDict = {}
imageDict["hist"] = ""
checkedVars = {}

mainLayout = QGridLayout()

class MainWindow(QMainWindow):
    """Main Window."""
    
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        
        self.setWindowTitle("OpenCV functions GUI")
        
        self.initGUI()
        self.resize(800, 400)

        for i in range(len(labels)):
            labels[i].setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
    def randColor(self):
        color = QtGui.QColor(*random.sample(range(255), 3))
        return color
        
    def initGUI(self):
        self._createActions()
        self._createMenu()
        self._createToolBar()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("Input")
        label2 = QLabel('Result')
        label3 = QLabel('Functions 1')
        
        btn1 = QPushButton('Original')
        btn1.clicked.connect(self.showOriginal)
        btn2 = QPushButton('Show histogram')
        btn2.clicked.connect(self.makeHistogram)
        
        labels.append(label1)
        labels.append(label2)
        labels.append(label3)
        
        mainLayout.addWidget(labels[0], 0, 0, 1, 2)
        mainLayout.addWidget(labels[1], 0, 2, 1, 2)
        mainLayout.addWidget(labels[2], 1, 0, 1, 2)
        mainLayout.addWidget(btn1, 1, 2, 1, 1)
        mainLayout.addWidget(btn2, 1, 3, 1, 1)
        
        for i in range(len(labels)):
            labels[i].setStyleSheet("background-color: {}".format(self.randColor().name()))
        labels[2].setStyleSheet("background-color: gray")
         
        mainLayout.setRowStretch(0,3)
        mainLayout.setRowStretch(1,1)

        mainLayout.setColumnStretch(1,2)
        mainLayout.setColumnStretch(2,1)
        mainLayout.setColumnStretch(3,1)

        central_widget.setLayout(mainLayout)
        self.setLayout(mainLayout)
        self.setMinimumSize(1400, 800)
        
    def _createMenu(self):
        menuBar = self.menuBar()
        # File menu
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.saveAsAction)
        fileMenu.addAction(self.exitAction)
        
    def _createToolBar(self):
        toolbar = QToolBar("mainToolbar")
        
        self.addToolBar(toolbar)
        self.fileManipMenu = QAction("File", self)
        
        self.colorSchemeButton = QAction("Color space", self)
        self.colorSchemeButton.setEnabled(False)
        self.colorSchemeButton.triggered.connect(self.showColorScheme)
        toolbar.addAction(self.colorSchemeButton)
        
        self.twoDimColorButton = QAction("2D color choose", self)
        self.twoDimColorButton.setEnabled(False)
        self.twoDimColorButton.triggered.connect(self.show2DimColorButtonScheme)
        toolbar.addAction(self.twoDimColorButton)
        
        self.edgeNoiseFilterButton = QAction("Edge and Noise filter", self)
        self.edgeNoiseFilterButton.setEnabled(False)
        self.edgeNoiseFilterButton.triggered.connect(self.showEdgeNoiseFilterScheme)
        toolbar.addAction(self.edgeNoiseFilterButton)
        
        self.binSegButton = QAction("Binary segmentations", self)
        self.binSegButton.setEnabled(False)
        self.binSegButton.triggered.connect(self.showBinSegScheme)
        toolbar.addAction(self.binSegButton)
        
        self.morphologicalButton = QAction("Morphological operation", self)
        self.morphologicalButton.setEnabled(False)
        self.morphologicalButton.triggered.connect(self.showMorphologicalOperations)
        toolbar.addAction(self.morphologicalButton) 

    def showColorScheme(self):
        self.colorSchemeButton.setEnabled(False)
        
        radioBtn1 = QRadioButton("BGR")
        radioBtn2 = QRadioButton("GRAY")
        radioBtn3 = QRadioButton("HSV")
        radioBtn4 = QRadioButton("YCbCr")
        
        colorSchemeChoose.append(radioBtn1)
        colorSchemeChoose.append(radioBtn2)
        colorSchemeChoose.append(radioBtn3)
        colorSchemeChoose.append(radioBtn4)
        
        for i in range(len(colorSchemeChoose)):
            colorSchemeChooseGroup.addButton(colorSchemeChoose[i])
        for i in range(len(colorSchemeChoose)):
            mainLayout.addWidget(colorSchemeChoose[i], i + 2 , 0, 1, 1)   
        
        colorSchemeChooseGroup.buttonClicked.connect(self.colorSchemeChoose)
        
    def colorSchemeChoose(self):
        colorSpace = abs(colorSchemeChooseGroup.checkedId())-1
        image = ImageQt.fromqpixmap(labels[0].pixmap())
        res = self.imgToPixmap(changeColorSpace(image, colorSpace))
        imageDict["colorSpace"] = res
        checkedVars["colorSpaceArg"] = colorSchemeChoose[abs(colorSchemeChooseGroup.checkedId())-2].text()
        self.drawImage(res)
        self.twoDimColorButton.setEnabled(True)
    
    def show2DimColorButtonScheme(self):
        colorSpace = abs(colorSchemeChooseGroup.checkedId())-1
        if colorSpace == 1:
            self.showRGBchoose()
        elif colorSpace == 2:
            self.twoDimColorButton.setEnabled(False)
            self.edgeNoiseFilterButton.setEnabled(True)
            imageDict["twoDimImage"] = imageDict["colorSpace"]
        elif colorSpace == 3:
            self.showHSVchoose()
        elif colorSpace == 4:
            self.showYCBCRchoose()
        
        for i in colorSchemeChoose:
            i.setHidden(True)
            
        self.colorSchemeButton.setEnabled(False)
        
    def showRGBchoose(self):
        self.twoDimColorButton.setEnabled(False)
        
        radioBtn1 = QRadioButton("Blue")
        radioBtn2 = QRadioButton("Green")
        radioBtn3 = QRadioButton("Red")
        
        rgbColorChoose.append(radioBtn1)
        rgbColorChoose.append(radioBtn2)
        rgbColorChoose.append(radioBtn3)
        
        for i in range(len(rgbColorChoose)):
            rgbColorChooseGroup.addButton(rgbColorChoose[i])     
        for i in range(len(rgbColorChoose)):
            mainLayout.addWidget(rgbColorChoose[i], i + 2 , 1, 1, 1) 
            
        rgbColorChooseGroup.buttonClicked.connect(self.allColorChoose)

    def showHSVchoose(self):
        self.twoDimColorButton.setEnabled(False)
        
        radioBtn1 = QRadioButton("Hue")
        radioBtn2 = QRadioButton("Saturation")
        radioBtn3 = QRadioButton("Value of brightness")
        
        hsvColorChoose.append(radioBtn1)
        hsvColorChoose.append(radioBtn2)
        hsvColorChoose.append(radioBtn3)
        
        for i in range(len(hsvColorChoose)):
            hsvColorChooseGroup.addButton(hsvColorChoose[i])     
        for i in range(len(hsvColorChoose)):
            mainLayout.addWidget(hsvColorChoose[i], i + 2 , 1, 1, 1)
            
        hsvColorChooseGroup.buttonClicked.connect(self.allColorChoose)
                
    def showYCBCRchoose(self):
        self.twoDimColorButton.setEnabled(False)
        
        radioBtn1 = QRadioButton("Luminance")
        radioBtn2 = QRadioButton("Blue diff")
        radioBtn3 = QRadioButton("Red diff")
        
        ycbcrColorChoose.append(radioBtn1)
        ycbcrColorChoose.append(radioBtn2)
        ycbcrColorChoose.append(radioBtn3)
        
        for i in range(len(ycbcrColorChoose)):
            ycbcrColorChooseGroup.addButton(ycbcrColorChoose[i])     
        for i in range(len(ycbcrColorChoose)):
            mainLayout.addWidget(ycbcrColorChoose[i], i + 2 , 1, 1, 1) 
            
        ycbcrColorChooseGroup.buttonClicked.connect(self.allColorChoose)
        
    def allColorChoose(self):
        image = ImageQt.fromqpixmap(imageDict["colorSpace"])
        tempArr = [ abs(ycbcrColorChooseGroup.checkedId()),
                    abs(hsvColorChooseGroup.checkedId()),
                    abs(rgbColorChooseGroup.checkedId())]
        res = self.imgToPixmap(all2DColorSpace(image, max(tempArr)-1))
        imageDict["twoDimImage"] = res
        self.drawImage(res)
        self.twoDimColorButton.setEnabled(False)
        self.edgeNoiseFilterButton.setEnabled(True)

    def showEdgeNoiseFilterScheme(self):
        for x in twoDimColorChoose:
            for i in x:
                i.setHidden(True)
        self.edgeNoiseFilterButton.setEnabled(False)
        
        radioBtn1 = QRadioButton("Edge detect")
        radioBtn2 = QRadioButton("Tresholding - Mean")
        radioBtn3 = QRadioButton("Tresholding - Gaussian")
        
        edgeNoiseChoose.append(radioBtn1)
        edgeNoiseChoose.append(radioBtn2)
        edgeNoiseChoose.append(radioBtn3)
        
        for i in range(len(edgeNoiseChoose)):
            edgeNoiseChooseGroup.addButton(edgeNoiseChoose[i])
            
        for i in range(len(edgeNoiseChoose)):
            mainLayout.addWidget(edgeNoiseChoose[i], i + 2 , 1, 1, 1)    
                
        edgeNoiseChooseGroup.buttonClicked.connect(self.showEdgeNoiseFilterChoose)
        
    def showEdgeNoiseFilterChoose(self):
        image = ImageQt.fromqpixmap(imageDict["twoDimImage"])
        colorSpace = abs(edgeNoiseChooseGroup.checkedId())-1
        res = self.imgToPixmap(edgeNoiseFunctions(image, colorSpace))
        imageDict["edgeNoiseFilter"] = res
        self.drawImage(res)
        self.edgeNoiseFilterButton.setEnabled(False)
        self.binSegButton.setEnabled(True)
    
    def showBinSegScheme(self):
        for x in edgeNoiseChoose:
            x.setHidden(True)
                
        self.edgeNoiseFilterButton.setEnabled(False)
        
        radioBtn1 = QRadioButton("Global")
        radioBtn2 = QRadioButton("Otsu")
        
        binSegmentationChoose.append(radioBtn1)
        binSegmentationChoose.append(radioBtn2)
        
        for i in range(len(binSegmentationChoose)):
            binSegmentationChooseGroup.addButton(binSegmentationChoose[i])
            
        for i in range(len(binSegmentationChoose)):
            mainLayout.addWidget(binSegmentationChoose[i], i + 2 , 1, 1, 1)    
                
        binSegmentationChooseGroup.buttonClicked.connect(self.showBinSegChoose)
    
    def showBinSegChoose(self):
        image = ImageQt.fromqpixmap(imageDict["edgeNoiseFilter"])
        colorSpace = abs(edgeNoiseChooseGroup.checkedId())-1
        res = self.imgToPixmap(binSegFunctions(image, colorSpace))
        imageDict["binSeg"] = res
        self.drawImage(res)
        self.binSegButton.setEnabled(False)
        self.morphologicalButton.setEnabled(True)
    
    def showMorphologicalOperations(self):
        for i in binSegmentationChoose:
            i.setHidden(True)
        self.colorSchemeButton.setEnabled(False)
        
        radioBtn1 = QRadioButton("Erosion")
        radioBtn2 = QRadioButton("Diletation")
        radioBtn3 = QRadioButton("Tophat")
        radioBtn4 = QRadioButton("Blackhat")
        
        morphOperationsChoose.append(radioBtn1)
        morphOperationsChoose.append(radioBtn2)
        morphOperationsChoose.append(radioBtn3)
        morphOperationsChoose.append(radioBtn4)
        
        for i in range(len(morphOperationsChoose)):
            morphOperationsChooseGroup.addButton(morphOperationsChoose[i])
              
        for i in range(len(morphOperationsChoose)):
            mainLayout.addWidget(morphOperationsChoose[i], i + 2 , 1, 1, 1)
        
        morphOperationsChooseGroup.buttonClicked.connect(self.morphOperationChoose)
    
    def morphOperationChoose(self):
        image = ImageQt.fromqpixmap(imageDict["binSeg"])
        res = self.imgToPixmap(morphOperation(image, morphOperationsChooseGroup.checkedId()))
        imageDict['result'] = res
        self.drawImage(res)

        self.colorSchemeButton.setEnabled(True)

    def _createActions(self):
        # File Menu
        ## Open file
        self.openAction = QAction("&Open image", self)
        self.openAction.triggered.connect(self.openImage) 
        ## Save file
        self.saveAction = QAction("&Save image", self)
        ## Save file as
        self.saveAsAction = QAction("&Save image as", self)
        self.saveAsAction.triggered.connect(self.saveAsImage)
        
        self.exitAction = QAction("&Exit", self)
    
    def openImage(self):
        try:
            imagePath, _ = QFileDialog.getOpenFileName()
            pixmap = QPixmap(imagePath)
            
            labelWidth = labels[0].width()
            labelHeight = labels[0].height()
            
            pixmapWidth = pixmap.width()
            pixmapHeight = pixmap.height()
            
            pixmapRatio = pixmapHeight/pixmapWidth
            
            newHeight = int(pixmapRatio*labelWidth)
            newWidth = int(pixmapRatio*labelHeight)
            
            if (pixmapWidth > pixmapHeight):
                pixmap1 = pixmap.scaled(labelWidth,newHeight,Qt.KeepAspectRatio, Qt.FastTransformation)
            else:
                pixmap1 = pixmap.scaled(newWidth,labelHeight,Qt.KeepAspectRatio, Qt.FastTransformation)
            labels[0].setPixmap(pixmap1)
        
            self.colorSchemeButton.setEnabled(True)
            imageDict['original'] = pixmap1
        except:
            labels[1].setText("Picture is not loaded")
            imagePath = 0
        
        return imagePath
             
    def saveAsImage(self):
        pixmap = labels[1].pixmap()
        if pixmap is not None:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            filename, _ = QFileDialog.getSaveFileName(self, "Save Image", r"C:\\Users\\hartig\\Documents\\skola_21_22\\pyqt_test", "All Files (*)", options=options)
            if filename:
                with open(filename, "wb") as f:
                    f.write(pixmap)
        else:
            labels[1].setText("Picture is not loaded")
    
    def showOriginal(self):
        if "result" in imageDict:
            self.drawImage(imageDict["result"])
        elif "original" in imageDict:
            self.drawImage(imageDict["original"])
        else:
            labels[0].setText("Picture is not loaded")
    
    def makeHistogram(self):
        pixmap = imageDict[list(imageDict.keys())[-1]]
        if pixmap is not None:
            image = ImageQt.fromqpixmap(imageDict[list(imageDict.keys())[-1]])
            
            res = self.imgToPixmap(makeHist(image))
            imageDict['hist'] = res
            self.drawImage(res)
        else:
            labels[0].setText("Picture is not loaded")
        self.drawImage(imageDict["hist"])
    
    def drawImage(self ,picture):
        labels[1].setPixmap(picture)   
    
    def imgToPixmap(self, image):
        im2 = image.convert("RGBA")
        data = im2.tobytes("raw", "BGRA")
        qim = QtGui.QImage(data, image.width, image.height, QtGui.QImage.Format_ARGB32)
        pixmap = QtGui.QPixmap.fromImage(qim)
        return pixmap
    
    def drawImage(self ,picture):
        labels[1].setPixmap(picture)

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()