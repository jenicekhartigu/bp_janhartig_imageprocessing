
from PyQt5 import QtGui
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PIL import ImageQt

from graphicFunctions.rbgTabInit                import rgbWidgetInit
from graphicFunctions.hsvTabInit                import hsvWidgetInit
from graphicFunctions.ycbcrTabInit              import ycbcrWidgetInit
from graphicFunctions.grayTabInit               import grayWidgetInit

from geometricFunctions.rotateTabInit           import rotateWidgetInit
from geometricFunctions.shiftingTabInit         import shiftingWidgetInit
from geometricFunctions.perspectiveTabInit      import perspectiveWidgetInit

from thresholdingFunctions.meanThreshTabInit import meanThreshWidgetInit
from thresholdingFunctions.gaussianThreshTabInit import gaussianThreshWidgetInit
from thresholdingFunctions.convolutionTabInit    import convolutionWidgetInit
from thresholdingFunctions.averagingTabInit      import averagingWidgetInit
from thresholdingFunctions.gaussianTabInit       import gaussianWidgetInit
from thresholdingFunctions.medianTabInit         import medianWidgetInit

from morphologicalFunctions.erosionTabInit      import erosionWidgetInit
from morphologicalFunctions.dilationTabInit     import dilationWidgetInit
from morphologicalFunctions.openingTabInit      import openingWidgetInit
from morphologicalFunctions.closingTabInit      import closingWidgetInit
from morphologicalFunctions.gradientTabInit     import gradientWidgetInit
from morphologicalFunctions.tophatTabInit       import tophatWidgetInit
from morphologicalFunctions.blackhatTabInit     import blackhatWidgetInit


operationBtns = []
functionalAreas = []
logDisplay = []


def colorSpaceTabsInit():
    colorSpaceTabs = []
    rgbWidget = rgbWidgetInit(functionalAreas, logDisplay)
    hsvWidget = hsvWidgetInit(functionalAreas, logDisplay)
    ycbcrWidget = ycbcrWidgetInit(functionalAreas)
    grayWidget = grayWidgetInit(functionalAreas, logDisplay)
    
    colorSpaceTabs.append(grayWidget)
    colorSpaceTabs.append(rgbWidget)
    colorSpaceTabs.append(hsvWidget)
    colorSpaceTabs.append(ycbcrWidget)
    
    return colorSpaceTabs

def geometricTabsInit():
    geometricTabs = []
    rotateWidget = rotateWidgetInit(functionalAreas, logDisplay)
    shiftingWidget = shiftingWidgetInit(functionalAreas, logDisplay)
    perspectiveWidget = perspectiveWidgetInit(functionalAreas, logDisplay)
    
    geometricTabs.append(rotateWidget)
    geometricTabs.append(shiftingWidget)
    geometricTabs.append(perspectiveWidget)
    
    return geometricTabs

def trehsholdingTabsInit():
    trehsholdingTabs = []
    meanThreshWidget = meanThreshWidgetInit(functionalAreas, logDisplay)
    gaussianThreshWidget = gaussianThreshWidgetInit(functionalAreas, logDisplay)
    convolutionWidget = convolutionWidgetInit(functionalAreas, logDisplay)
    averagingWidget = averagingWidgetInit(functionalAreas, logDisplay)
    gausianWidget = gaussianWidgetInit(functionalAreas, logDisplay)
    medianWidget = medianWidgetInit(functionalAreas, logDisplay)
    
    trehsholdingTabs.append(meanThreshWidget)
    trehsholdingTabs.append(gaussianThreshWidget)
    trehsholdingTabs.append(convolutionWidget)
    trehsholdingTabs.append(averagingWidget)
    trehsholdingTabs.append(gausianWidget)
    trehsholdingTabs.append(medianWidget)
    return trehsholdingTabs

def morhpoTabsInit():
    morhpoTabs = []
    erosionWidget = erosionWidgetInit(functionalAreas, logDisplay)
    dilationWidget = dilationWidgetInit(functionalAreas, logDisplay)
    openingWidget = openingWidgetInit(functionalAreas, logDisplay)
    closingWidget = closingWidgetInit(functionalAreas, logDisplay)
    gradientWidget = gradientWidgetInit(functionalAreas, logDisplay)
    tophatWidget = tophatWidgetInit(functionalAreas, logDisplay)
    blackhatWidget = blackhatWidgetInit(functionalAreas, logDisplay)
    
    morhpoTabs.append(erosionWidget)
    morhpoTabs.append(dilationWidget)
    morhpoTabs.append(openingWidget)
    morhpoTabs.append(closingWidget)
    morhpoTabs.append(gradientWidget)
    morhpoTabs.append(tophatWidget)
    morhpoTabs.append(blackhatWidget)
    
    return morhpoTabs

def functionHandling(choice):
    #color spaces
    if choice == 0:
        colorSpaceTabs = colorSpaceTabsInit()
        colorSpaceTabNames = ["Gray",
                              "RGB",
                              "HSV",
                              "YCbCr"
                              ]
        
        for i in range(len(colorSpaceTabs)):
            name = colorSpaceTabNames[i]
            functionalAreas[1].addTab(colorSpaceTabs[i],name)
        
    elif choice == 1:
        geometricTabs = geometricTabsInit()
        geometricTabNames = ["Rotate",
                             "Shifting",
                             "Perspective"
                            ]
        for i in range(len(geometricTabs)):
            name = geometricTabNames[i]
            functionalAreas[1].addTab(geometricTabs[i],name)
        
    elif choice == 2:
        trehsholdingTabs = trehsholdingTabsInit()
        trehsholdingTabNames = ["Mean thresholding",
                                "Gaussian thresholding",
                                "Convolution smoothing",
                                "Averaging smoothing",
                                "Gausian smoothing",
                                "Median smoothing"
                               ]
        for i in range(len(trehsholdingTabs)):
            name = trehsholdingTabNames[i]
            functionalAreas[1].addTab(trehsholdingTabs[i],name)
            
    elif choice == 3:
        morhpoTabs = morhpoTabsInit()
        morhpoTabNames = ["Erosion",
                          "Dilation",
                          "Opening",
                          "Closing",
                          "Gradient",
                          "Top hat",
                          "Black hat"
                          ]
        for i in range(len(morhpoTabs)):
            name = morhpoTabNames[i]
            functionalAreas[1].addTab(morhpoTabs[i],name)

def graphicFuncInit(operBtns, disAreas, logDisp):
    for i in operBtns:
        operationBtns.append(i)
    for i in disAreas:
        functionalAreas.append(i)
    for i in logDisp:
        logDisplay.append(i)
        
    