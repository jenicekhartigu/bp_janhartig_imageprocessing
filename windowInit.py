from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import sys

operationBtns = []
functionalAreas = []
logDisplay = []

# Init basic buttons of GUI
def operationBtnsLayoutInit():
    operationBtnsLayout = QBoxLayout(2)
    
    emptyLabel = QLabel()
    
    #file manip
    tempComboFile = QComboBox()
    tempListFileManip = ["File manip",
                         "Open file",
                         "Save as",
                         "Exit",
                         ]
    tempComboFile.addItems(tempListFileManip) 

    #help manip
    tempComboHelp = QComboBox()
    tempListHelpManip = ["Help things",
                         "Help",
                         "List of functions"
                         ]
    tempComboHelp.addItems(tempListHelpManip)
    
    operationBtns.append(tempComboFile)
    operationBtns.append(tempComboHelp)
    
    #manip buttons
    btnTextArr = ["<",
                  ">",
                  "Histogram",
                  "Original",
                  "Expand image",
                  "Select area",
                  "Last saved"
                  ]
    
    for option in range(len(btnTextArr)):
        tempBtn = QPushButton(btnTextArr[option])
        operationBtns.append(tempBtn)
        
    fileBtnsLayout = QBoxLayout(0)
    fileBtnsLayout.addWidget(operationBtns[0],1)
    fileBtnsLayout.addWidget(operationBtns[1],1)
    fileBtnsLayout.addWidget(emptyLabel,5)
    
    secondRowBtns = QBoxLayout(0)
    
    forwbackBtnsLayout = QBoxLayout(0)
    
    forwbackBtnsLayout.addWidget(operationBtns[5]) #orig
    forwbackBtnsLayout.addWidget(operationBtns[2])
    forwbackBtnsLayout.addWidget(operationBtns[3])
    forwbackBtnsLayout.addWidget(operationBtns[8]) #last saved
    
    graphicBtnsLayout = QBoxLayout(0)
    
    graphicBtnsLayout.addWidget(operationBtns[7]) #select
    graphicBtnsLayout.addWidget(operationBtns[6]) #expand
    graphicBtnsLayout.addWidget(operationBtns[4]) #hist
    
    
    secondRowBtns.addLayout(forwbackBtnsLayout,2)
    secondRowBtns.addLayout(graphicBtnsLayout,3)
    secondRowBtns.addWidget(emptyLabel,2)
    
    #widget making  
    operationBtnsLayout.addLayout(fileBtnsLayout)
    operationBtnsLayout.addLayout(secondRowBtns)
    
          
    return operationBtnsLayout

def functionsAreaLayoutInit():
    functionsAreaLayout = QVBoxLayout()
    
    tempLabel1 = QLabel("List of functions:")
    tempFunChoiceCombo = QComboBox()
    graphicFunctions = ["Chose method",
                        "Color selection",
                        "Geometric operations",
                        "Thresholding & smoothing",
                        "Morphological transformation",
                        ]
    
    tempFunChoiceCombo.addItems(graphicFunctions)
    
    tempLabel2 = QLabel("Settings of functions:")
    tempFunSettingsTabWidget = QTabWidget()
    
    functionalAreas.append(tempFunChoiceCombo)
    functionalAreas.append(tempFunSettingsTabWidget)
    
    functionsAreaLayout.addWidget(tempLabel1)
    functionsAreaLayout.addWidget(tempFunChoiceCombo)
    functionsAreaLayout.addWidget(tempLabel2)
    functionsAreaLayout.addWidget(tempFunSettingsTabWidget)
    
    return functionsAreaLayout

def mainPicAreaLayoutInit():
    tempLabel = QLabel()
    tempLabel.setAlignment(Qt.AlignCenter)
    tempLabel.setStyleSheet("border: 1px solid #d9d9d9;")
    
    functionalAreas.append(tempLabel)
    return tempLabel

def histogramAreaLayoutInit():
    histogramAreaLayout = QVBoxLayout()
    
    testLabel = QLabel()
    histogramAreaLayout.addWidget(testLabel)
    
    functionalAreas.append(testLabel)
    functionalAreas.append(histogramAreaLayout)
    
    return histogramAreaLayout
# Init main labels of GUI
def displayAreasLayoutInit():
    displayAreasLayout = QBoxLayout(0)
    
    #adding functional part
    
    functionsArea = functionsAreaLayoutInit()
    picArea = mainPicAreaLayoutInit()
    histogramArea = histogramAreaLayoutInit()
     
    displayAreasLayout.addLayout(functionsArea, 4)
    displayAreasLayout.addWidget(picArea,       6)
    displayAreasLayout.addLayout(histogramArea, 4)
    
    return displayAreasLayout

# Init last row of GUI
def logDisplayLayoutInit():
    logDisplayLayout = QBoxLayout(0)
    
    tempCmd = QTextEdit()
    emptyLabel = QLabel()
    
    logDisplay.append(emptyLabel)
    logDisplay.append(tempCmd)
    logDisplay.append(emptyLabel)
    
    logDisplayLayout.addWidget(emptyLabel,4)
    logDisplayLayout.addWidget(tempCmd, 6)
    logDisplayLayout.addWidget(emptyLabel,4)
    
    return logDisplayLayout

# Init of layouts
def windowLayout():
    baseLayout = QGridLayout()
    
    operationLayout = operationBtnsLayoutInit()
    displayAreasLayout = displayAreasLayoutInit()
    logDisplayLayout = logDisplayLayoutInit()
    
    baseLayout.addLayout(operationLayout,    1, 0)
    baseLayout.addLayout(displayAreasLayout, 2, 0)
    baseLayout.addLayout(logDisplayLayout,   3, 0)

    baseLayout.setRowStretch(2,9)
    baseLayout.setRowStretch(3,1)

    return baseLayout

# Whole GUI init and send of variables
def windowInitGui():
    win = QWidget()
    
    win.showMaximized()
    win.setWindowTitle("BP")
    
    winLayout = windowLayout()
    
    win.setLayout(winLayout)

    return win, operationBtns, functionalAreas, logDisplay

def addTabsToWidget(choice):
    print(choice)
    



