import sys
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.buildUI()

        # showing all the widgets
        self.show()

    # method for widgets build
    def buildUI(self):
        # creating label
        label = QLabel("Hello there", self)

        # setting geometry to label
        label.setGeometry(100, 100, 120, 40)

        # adding border to label
        label.setStyleSheet("border : 2px solid black")

        # opening window in maximized size
        self.show()


# create pyqt5 app
app = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(app.exec())