from PyQt5 import QtWidgets, uic
import sys


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi("example.ui", self)

        self.button = self.findChild(QtWidgets.QPushButton, 'mainbutton')  # Find the button
        self.button.clicked.connect(self.button_clicked)  # function pointer

        self.show()

    def button_clicked(self):
        # This is executed when the button is clicked
        print('My button was clicked')


app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec_()
