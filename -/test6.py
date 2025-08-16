from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtCore import QPropertyAnimation, pyqtProperty, QPointF, Qt
from PyQt6.QtGui import QColor, QPainter, QBrush, QLinearGradient

class AnimatedBackgroundButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gradient_position = 0  # เริ่มต้นตำแหน่งของ gradient
        self._is_animating = False  # ติดตามสถานะแอนิเมชัน
        self.colors = [
            QColor(100, 100, 255),  # สีฟ้า
            QColor(255, 100, 255),  # สีม่วง
        ]

        # สร้างแอนิเมชันที่ให้ gradient เคลื่อนที่จากซ้ายไปขวา
        self.background_animation = QPropertyAnimation(self, b"gradientPosition")
        self.background_animation.setDuration(2500)
        self.background_animation.setStartValue(0.1)
        self.background_animation.setEndValue(0.9)
        self.background_animation.setLoopCount(-1)

        # ตั้งค่าให้ปุ่มไม่มีสีพื้นหลังหรือขอบ
        self.setStyleSheet("padding: 10px; border: none; border-radius: 30px;")  # เพิ่ม border-radius

    # สร้าง property สำหรับตำแหน่ง gradient
    @pyqtProperty(float)
    def gradientPosition(self):
        return self._gradient_position

    @gradientPosition.setter
    def gradientPosition(self, position):
        self._gradient_position = position
        self.update()  # รีเฟรชปุ่มเพื่ออัปเดต gradient

    def paintEvent(self, event):
        # สร้าง gradient
        gradient = QLinearGradient(QPointF(0, 0), QPointF(self.width(), 0))

        num_colors = len(self.colors)
        for i, color in enumerate(self.colors):
            # คำนวณตำแหน่งของแต่ละสีให้ห่างกันเท่ากัน
            pos = (self._gradient_position + i / num_colors) % 1
            gradient.setColorAt(pos, color)

        # ใช้ QPainter เพื่อวาดพื้นหลังที่ใช้ gradient
        painter = QPainter(self)
        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.PenStyle.NoPen)  # ไม่มีขอบ
        painter.drawRoundedRect(self.rect(), 10, 10)  # วาดปุ่มด้วยมุมโค้ง

        # วาดข้อความของปุ่มหลังจากวาดพื้นหลัง
        super().paintEvent(event)

    def enterEvent(self, event):
        if not self._is_animating:  # เริ่มแอนิเมชันเมื่อเมาส์ชี้ที่ปุ่ม
            self.background_animation.setStartValue(self._gradient_position)  # เริ่มจากตำแหน่งปัจจุบัน
            self.background_animation.start()
            self._is_animating = True  # ตั้งค่าสถานะแอนิเมชันเป็นกำลังทำงาน
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self._is_animating:  # หยุดแอนิเมชันเมื่อเมาส์ออกจากปุ่ม
            self.background_animation.stop()  
            # เก็บตำแหน่งปัจจุบัน
            current_position = self.gradientPosition
            self._gradient_position = current_position  # เก็บตำแหน่งปัจจุบัน
            self.update()  # อัปเดตปุ่มให้แสดง gradient ล่าสุด
            self._is_animating = False  # ตั้งค่าสถานะแอนิเมชันเป็นไม่ทำงาน
        super().leaveEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ตั้งค่าหน้าต่างหลัก
        self.setWindowTitle("Animated Background Color Moving Left to Right")
        self.setGeometry(100, 100, 300, 200)

        # สร้างปุ่มที่มีอนิเมชันพื้นหลัง
        self.button = AnimatedBackgroundButton("Hover Me", self)
        self.button.setGeometry(100, 80, 100, 40)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
