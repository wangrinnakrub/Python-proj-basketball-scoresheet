import sys
from PyQt6.QtCore import Qt, QPropertyAnimation, pyqtProperty
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from PyQt6.QtGui import QPainter, QColor


class CircleAnimationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._radius = 0  # เริ่มต้นด้วยวงกลมขนาดเล็ก
        self.color = QColor(0, 0, 0, 128)  # สีดำโปร่งใส

    @pyqtProperty(int)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # วาดวงกลมตรงกลางหน้าจอ
        center_x = self.width() // 2
        center_y = self.height() // 2
        painter.setBrush(self.color)
        painter.setPen(Qt.PenStyle.NoPen)  # ไม่ใช้เส้นขอบ
        painter.drawEllipse(center_x - self._radius, center_y - self._radius, self._radius * 2, self._radius * 2)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Circle Transition Animation")
        self.setGeometry(100, 100, 400, 300)

        # QStackedWidget สำหรับเปลี่ยนหน้า
        self.stacked_widget = QStackedWidget(self)

        # หน้า 2
        self.page2 = QWidget()
        page2_layout = QVBoxLayout(self.page2)
        self.next_button = QPushButton("Next to Page 1", self.page2)
        page2_layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # หน้า 1
        self.page1 = QWidget()
        page1_layout = QVBoxLayout(self.page1)
        page1_layout.addWidget(QPushButton("Page 1 Button"), alignment=Qt.AlignmentFlag.AlignCenter)

        # เพิ่มหน้าลงใน QStackedWidget
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page1)

        # Layout หลัก
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # วิดเจ็ตสำหรับอนิเมชัน
        self.animation_widget = CircleAnimationWidget(self)
        self.animation_widget.hide()

        # เชื่อมปุ่มกับฟังก์ชัน
        self.next_button.clicked.connect(self.start_animation)

    def start_animation(self):
        # เตรียมการอนิเมชัน
        self.animation_widget.show()
        self.animation_widget.setGeometry(self.rect())  # ครอบคลุมหน้าจอ

        # คำนวณรัศมีสูงสุด (ใหญ่ที่สุดที่ครอบคลุม
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
