import sys
from PyQt5.QtWidgets import *

app = QApplication([])
w = QWidget()
w.setGeometry(30, 30, 1000, 1000)
l = QLabel(w)
l.setText("I love programming")
w.show()
sys.exit(app.exec())

