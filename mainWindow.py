from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
from windowInit import *
from globalFunc import *

app = QApplication(sys.argv)

def guiInit():
    
    win, operationBtns, displayAreas, logDisplay = windowInitGui()
    
    logicInit(app, operationBtns, displayAreas, logDisplay)
    
    win.show()
    sys.exit(app.exec_())
