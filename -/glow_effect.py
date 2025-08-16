from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

class GlowButtonApp(QWidget):
    def __init__(self):
        super().__init__()

        # ตั้งค่า UI
        self.setWindowTitle("Glow Effect Button")
        self.setGeometry(100, 100, 300, 200)

        # สร้างปุ่ม
        self.button = QPushButton("Glow Button", self)

        # สร้างเอฟเฟกต์เงา (Glow)
        glow_effect = QGraphicsDropShadowEffect()
        glow_effect.setBlurRadius(20)  # ความฟุ้งของแสง
        glow_effect.setColor(QColor(0, 255, 0))  # สีของ Glow (เขียว)
        glow_effect.setOffset(0, 0)  # ไม่มีการเลื่อนเงา (Glow กระจายรอบ ๆ)

        # นำเอฟเฟกต์ไปใช้กับปุ่ม
        self.button.setGraphicsEffect(glow_effect)

        # จัด Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

# Run Application
app = QApplication([])
window = GlowButtonApp()
window.show()
app.exec()
