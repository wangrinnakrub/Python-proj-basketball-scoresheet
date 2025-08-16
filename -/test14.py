import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class LayoutWithBorderExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Layout with Border Example")
        self.resize(400, 300)

        # สร้าง QWidget สำหรับครอบ layout และกำหนด style
        bordered_widget = QWidget(self)
        bordered_widget.setStyleSheet("""
            QWidget {
                border: 2px solid black;
                border-radius: 8px; /* มุมโค้ง */
                background-color: #f0f0f0; /* สีพื้นหลัง */
            }
        """)

        # สร้าง layout ภายใน bordered_widget
        layout = QVBoxLayout(bordered_widget)

        # เพิ่ม widgets ใน layout
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # กำหนด layout หลักให้กับ QWidget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(bordered_widget)
        self.setLayout(main_layout)

# เริ่มโปรแกรม
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LayoutWithBorderExample()
    window.show()
    sys.exit(app.exec())
