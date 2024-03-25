# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firstGUIshotwrpDQX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

import random
import sys

from PyQt5 import *
from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(946, 703)
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
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer_3, 0, 10, 1, 1)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer, 0, 9, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer_5, 0, 6, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self._2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self._2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.widget = QWidget(self.gridLayoutWidget)
        self.widget.setObjectName(u"widget")

        self._2.addWidget(self.widget, 2, 9, 2, 3)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self._2.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self._2.addWidget(self.pushButton_5, 0, 4, 1, 1)

        self.widget_3 = QWidget(self.gridLayoutWidget)
        self.widget_3.setObjectName(u"widget_3")

        self._2.addWidget(self.widget_3, 2, 3, 1, 6)

        self.functions = QTabWidget(self.gridLayoutWidget)
        self.functions.setObjectName(u"functions")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 221, 591))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.functions.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_3 = QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(0, 0, 221, 591))
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

        self._2.addWidget(self.functions, 2, 0, 1, 3)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self._2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer_4, 0, 7, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer_2, 0, 11, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._2.addItem(self.horizontalSpacer_6, 0, 5, 1, 1)

        self._2.setRowStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 946, 26))
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

        self.retranslateUi(MainWindow)

        self.functions.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Original", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"<--", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"RGB", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"HSV", None))
        self.functions.setTabText(self.functions.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"ColorSpaces", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"RGB", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"HSV", None))
        self.functions.setTabText(self.functions.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.functions.setTabText(self.functions.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Strana", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"-->", None))
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