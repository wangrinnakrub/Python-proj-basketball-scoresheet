from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # สร้างปุ่ม
        self.button = QPushButton("Hover over me!", self)
        self.button.setGeometry(100, 100, 200, 50)

        # กำหนดให้แสดง cursor เป็นรูปมือเมื่อ hover บนปุ่มqwdqwdasdsdasd
        self.button.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("Cursor Hover Example")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
