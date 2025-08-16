from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import time

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PyQt6.QtCore import Qt, QTimer

class LoadingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading Example")
        self.setGeometry(200, 200, 300, 150)

        layout = QVBoxLayout()

        self.progress = QProgressBar(self)
        self.progress.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        self.start_button = QPushButton("Start Loading", self)
        self.start_button.clicked.connect(self.start_loading)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

    def start_loading(self):
        self.progress.setValue(0)
        self.timer.start(50)  # Update every 50msasdasd

    def update_progress(self):
        value = self.progress.value()
        if value < 100:
            self.progress.setValue(value + 1)
        else:
            self.timer.stop()
            self.progress.setValue(100)

app = QApplication(sys.argv)
window = LoadingWindow()
window.show()
sys.exit(app.exec())
