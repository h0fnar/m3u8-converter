from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        button_action = QAction("&M3U Converter", self)
        menu = self.menuBar()

        about_menu = menu.addMenu("&About")
        about_menu.addAction(button_action)
