from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton
import sys

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        button = QPushButton("Go to Page 2")
        button.clicked.connect(self.go_to_page2)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setStyleSheet("background:red;")

    def go_to_page2(self):
        self.parentWidget().setCurrentIndex(1)  # เปลี่ยนไปที่หน้า 2

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        button = QPushButton("Go to Page 1")
        button.clicked.connect(self.go_to_page1)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setStyleSheet("background:yellow;")

    def go_to_page1(self):
        self.parentWidget().setCurrentIndex(0)  # กลับไปที่หน้า 1

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # สร้าง QStackedWidget สำหรับสลับหน้า
        self.stack = QStackedWidget()

        # เพิ่มหน้าแต่ละหน้าเข้ามาใน stack
        self.page1 = Page1()
        self.page2 = Page2()
        self.stack.addWidget(self.page1)  # หน้าที่ 1
        self.stack.addWidget(self.page2)  # หน้าที่ 2

        # ตั้งค่า layout
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        # เริ่มที่หน้าที่ต้องการ (ในที่นี้คือหน้า 1)
        self.stack.setCurrentIndex(0)

# รันแอปพลิเคชันจากหน้าที่มี QStackedWidget
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
