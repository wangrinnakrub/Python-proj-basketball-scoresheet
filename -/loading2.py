from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QPen, QColor, QFont
import sys

class LoadingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Enhanced Loading Example")
        self.setGeometry(200, 200, 300, 300)
        self.setStyleSheet("background-color: #2E2E2E;")  # Dark background

        # Initialize variables for progress and timerasdqwdasd
        self.progress_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        # Layout for Start button
        layout = QVBoxLayout()
        self.start_button = QPushButton("Start Loading")
        self.start_button.setStyleSheet("background-color: #5E81AC; color: white; font-size: 14px;")
        self.start_button.clicked.connect(self.start_loading)
        layout.addWidget(self.start_button)
        layout.setAlignment(self.start_button, Qt.AlignmentFlag.AlignBottom)

        self.setLayout(layout)

    def start_loading(self):
        self.progress_value = 0
        self.timer.start(25)  # Update every 50msasd

    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += 1
            self.update()  # Repaint the widget to update progress
        else:
            self.timer.stop()

    def paintEvent(self, event):
        # Setup QPainter for custom circular progress bar
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Background Circle
        pen = QPen(QColor("#595f6b"), 15)
        painter.setPen(pen)
        painter.drawEllipse(50, 50, 100, 100)

        # Progress Circle
        pen.setColor(QColor("#38b1d3"))
        painter.setPen(pen)
        painter.drawArc(50, 50, 100, 100, (90 * 16),int( -self.progress_value * 3.6 * 16))

        # Progress Text
        painter.setPen(QColor("#E5E9F0"))
        painter.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignHCenter, f"{self.progress_value}%")

app = QApplication(sys.argv)
window = LoadingWindow()
window.show()
sys.exit(app.exec())
