from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QGraphicsDropShadowEffect
from PyQt6.QtGui import QLinearGradient, QColor, QBrush
from PyQt6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Glowing Gradient Button Example")

        # สร้างปุ่ม
        button = QPushButton("Glowing Gradient Button", self)
        button.setGeometry(50, 50, 200, 50)

        # สร้าง gradient ไล่สีพื้นหลัง
        gradient = QLinearGradient(0, 0, 0, 1)  # ไล่สีจากบนลงล่าง
        gradient.setCoordinateMode(QLinearGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(0, 255, 255))   # สีเริ่มต้น (ฟ้า)
        gradient.setColorAt(1, QColor(0, 0, 255))     # สีปลายทาง (น้ำเงิน)

        # ตั้งค่าพื้นหลังปุ่มด้วย gradient
        palette = button.palette()
        palette.setBrush(button.backgroundRole(), QBrush(gradient))
        button.setAutoFillBackground(True)
        button.setPalette(palette)

        # เพิ่มเงาเรืองแสงให้ปุ่ม
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)            # ความเบลอของแสง
        shadow.setOffset(0, 0)              # ระยะห่างของเงา
        shadow.setColor(QColor(0, 255, 0))  # สีของแสงเรือง (เขียว)

        button.setGraphicsEffect(shadow)

        # หรือใช้ stylesheet เพื่อกำหนด gradient และการตกแต่งปุ่ม
        button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                                            stop:0 rgba(0, 255, 255, 255),
                                            stop:1 rgba(0, 0, 255, 255));
                border: 1px solid #555;
                color: white;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,
                                            stop:0 rgba(0, 255, 255, 255),
                                            stop:1 rgba(0, 150, 255, 255));
            }
        """)

        self.resize(300, 150)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
