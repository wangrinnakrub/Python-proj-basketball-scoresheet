from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class GradientButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.setFixedSize(230, 37)
        self.is_hovered = False
        self.gradient = QLinearGradient(0, 0, 230, 37)
        self.gradient.setColorAt(0, QColor(67, 217, 255))  # สีเริ่มต้น
        self.gradient.setColorAt(1, QColor(255, 86, 199))  # สีสุดท้าย
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # กำหนด StyleSheet พื้นฐานasdฟหก
        self.setStyleSheet("""
            QPushButton {
                border: 2px solid #555;
                color: white;
                background-color: transparent;
                border-radius: 10px;
            }
        """)

    def enterEvent(self, event):
        self.is_hovered = True
        self.update()

    def leaveEvent(self, event):
        self.is_hovered = False
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        if self.is_hovered:
            pen = QPen(QBrush(self.gradient), 1)
            painter.setPen(pen)
        else:
            painter.fillRect(self.rect(), self.gradient)
            painter.setPen(Qt.GlobalColor.white)

        painter.setFont(self.font())
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text())
