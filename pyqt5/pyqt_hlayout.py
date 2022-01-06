import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal layout example")
        # Create a QHBoxLayout instance
        layout = QHBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Left"))
        layout.addWidget(QPushButton("Center"), 1)
        layout.addWidget(QPushButton("Right"), 2)

        # Set the layout on the application's window
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
