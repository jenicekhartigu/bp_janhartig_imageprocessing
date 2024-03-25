# -*- coding: utf-8 -*-
import sys

import tools

from PyQt5 import *
from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
################################################################################
## Form generated from reading UI file 'firstGUIshotiMVahg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
temp = ""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(946, 703)
        self.actionOpen_image = QAction(MainWindow)
        self.actionOpen_image.setObjectName(u"actionOpen_image")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 941, 651))
        self._2 = QGridLayout(self.gridLayoutWidget)
        self._2.setSpacing(1)
        self._2.setObjectName(u"_2")
        self._2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self._2.setContentsMargins(1, 1, 1, 1)
        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self._2.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self._2.addWidget(self.pushButton_5, 0, 4, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self._2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer_4, 0, 7, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer_3, 0, 10, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer_2, 0, 11, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer_5, 0, 6, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self._2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self._2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer_6, 0, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer, 0, 9, 1, 1)

        self.functions = QTabWidget(self.gridLayoutWidget)
        self.functions.setObjectName(u"functions")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 291, 591))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayoutWidget_2 = QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 281, 181))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalSlider_2 = QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(1)

        self.verticalLayout_2.addWidget(self.horizontalSlider_2)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalSlider = QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(1)

        self.verticalLayout_2.addWidget(self.horizontalSlider)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalSlider_3 = QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(1)

        self.verticalLayout_2.addWidget(self.horizontalSlider_3)

        self.horizontalLayoutWidget_3 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 480, 281, 81))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_3.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_3.addWidget(self.pushButton_11)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayoutWidget_2 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 480, 281, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.verticalLayoutWidget_3 = QWidget(self.tab_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 281, 181))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.horizontalSlider_4 = QSlider(self.verticalLayoutWidget_3)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(1)

        self.verticalLayout_3.addWidget(self.horizontalSlider_4)

        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalSlider_5 = QSlider(self.verticalLayoutWidget_3)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setOrientation(1)

        self.verticalLayout_3.addWidget(self.horizontalSlider_5)

        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.horizontalSlider_6 = QSlider(self.verticalLayoutWidget_3)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        self.horizontalSlider_6.setOrientation(1)

        self.verticalLayout_3.addWidget(self.horizontalSlider_6)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayoutWidget = QWidget(self.tab_9)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-4, -1, 281, 571))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.functions.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_3 = QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(0, 0, 281, 591))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.functions.addTab(self.tab_2, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.functions.addTab(self.tab_7, "")

        self._2.addWidget(self.functions, 2, 0, 1, 4)

        self.widget = QWidget(self.gridLayoutWidget)
        self.widget.setObjectName(u"widget")

        self._2.addWidget(self.widget, 2, 10, 2, 2)

        self.widget_3 = QWidget(self.gridLayoutWidget)
        self.widget_3.setObjectName(u"widget_3")

        self._2.addWidget(self.widget_3, 2, 4, 1, 6)

        self._2.setRowStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 946, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_image)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExit)
        def _openImage():
            temp = tools.openImage()
            p = self.widget.palette()
            p.setColor(self.widget.backgroundRole(), Qt.red)
            self.widget.setPalette(p)
        
        def _Save_as():
            tools.vypis(temp)
            
        self.actionOpen_image.triggered.connect(_openImage) 
        
            
        self.actionSave_as.triggered.connect(_Save_as) 
        
        self.retranslateUi(MainWindow)

        self.functions.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_image.setText(QCoreApplication.translate("MainWindow", u"Open image", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Original", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"<--", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"-->", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"RGB", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hue", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Saturation", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"HSV", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"YCbCr", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Gray", None))
        self.functions.setTabText(self.functions.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"ColorSpace", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.functions.setTabText(self.functions.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.functions.setTabText(self.functions.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Strana", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

def runUI():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
    
runUI()