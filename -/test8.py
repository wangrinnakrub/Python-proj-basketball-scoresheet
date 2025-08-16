from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QLinearGradient, QBrush, QColor, QPainter, QFont, QPen, QPixmap
from PyQt6.QtCore import Qt, QTimer, QRectF, pyqtSignal, QEvent
import sys

class GradientGlowButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.setFixedSize(230, 37)
        self.is_hovered = False
        self.gradient = QLinearGradient(0, 0, 230, 37)
        self.gradient.setColorAt(0, QColor(67, 217, 255))  # สีเริ่มต้นของไล่สี
        self.gradient.setColorAt(1, QColor(255, 86, 199))  # สีสุดท้ายของไล่สี
        self.setCursor(Qt.CursorShape.PointingHandCursor)
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

        # วาดเงาไล่สีเมื่อ hover
        if self.is_hovered:
            glow_gradient = QLinearGradient(0, 0, 230, 37)
            glow_gradient.setColorAt(0, QColor(67, 217, 255, 100))  # เงาเรืองแสงเริ่มต้นโปร่งใส
            glow_gradient.setColorAt(1, QColor(255, 86, 199, 100))  # เงาเรืองแสงสุดท้ายโปร่งใส
            painter.setBrush(QBrush(glow_gradient))
            painter.setPen(Qt.PenStyle.NoPen)
            shadow_rect = self.rect().adjusted(-5, -5, 5, 5)
            painter.drawRoundedRect(shadow_rect, 10, 10)

        # วาดพื้นหลังไล่สี
        painter.setBrush(QBrush(self.gradient))
        painter.setPen(Qt.GlobalColor.white)
        painter.drawRoundedRect(self.rect(), 10, 10)

        # วาดข้อความ
        painter.setFont(self.font())
        painter.setPen(Qt.GlobalColor.white)
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text())


class Signin_page(QMainWindow):
    # คลาสของคุณที่นี่ (ตัดส่วนที่ไม่จำเป็นออกเพื่อความกระชับ)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basketball Score Sheet - Sign In')
        self.setGeometry(360, 110, 700, 650)
        self.ui()

    def ui(self):
        self.layout = QVBoxLayout()
        self.addWidgetsToLayout(self.layout)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

    def addWidgetsToLayout(self, ui):
        # ส่วนอื่น ๆ เช่น labels, input boxes, error messages
        ui.addStretch()

        # ปุ่ม Sign In
        self.sign_in_button = GradientGlowButton('Sign In', self)
        self.sign_in_button.clicked.connect(self.check_sign_in)

        sign_in_button_layout = QHBoxLayout()
        sign_in_button_layout.addStretch()
        sign_in_button_layout.addWidget(self.sign_in_button)
        sign_in_button_layout.addStretch()
        ui.addLayout(sign_in_button_layout)

        ui.addStretch()

    def check_sign_in(self):
        # ฟังก์ชันสำหรับตรวจสอบการ sign in
        pass


# รันโปรแกรม
if __name__ == "__main__":
    app = QApplication(sys.argv)
    sign_in = Signin_page()
    sign_in.show()
    sys.exit(app.exec())
