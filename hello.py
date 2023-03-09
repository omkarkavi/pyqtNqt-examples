from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *

# Only needed for access to command line arguments
import sys


# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Calculator ")
 
        # setting geometry
        self.setGeometry(100, 100, 800, 800)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()
 
    # method for components
    def UiComponents(self):
 
        # creating a push button
        push = QPushButton("Press", self)
 
        # setting geometry to the push button
        push.setGeometry(100, 100, 120, 40)
 
        # creating a label
        label = QLabel("Hello", self)
 
        # setting geometry to the label
        label.setGeometry(100, 160, 300, 75)
 
        # setting alignment to the label
        label.setAlignment(Qt.AlignCenter)
 
        # font
        font = QFont("Deja Vu", 12)
 
        # setting font to the label
        label.setFont(font)
 
        # setting style sheet to the label
        label.setStyleSheet("QLabel"
                            "{"
                            "border : 2px solid green;"
                            "background : gray;"
                            "}")
 
        # hiding the label
        label.hide()
 
        # adding action method to the push button
        push.clicked.connect(lambda: do_something())
 
        # method called by the push button when pressed
        def do_something():
 
            # unhide the label
            label.show()
 
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# setting cursor flashtime
App.setCursorFlashTime(100)
 
# setting application object name
App.setObjectName("examples")
 
# setting application display name
App.setApplicationDisplayName("examples PyQt5")
 
# beep sound will occur when application
# is opened
#App.beep()
 
# message displayed about the Qt
#App.aboutQt()
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())








