from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsTextItem
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
import sys


class GraphicsTextAnimation(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setWindowTitle("Graphics Text Animation")
        self.setGeometry(100, 100, 400, 300)

        # เพิ่มข้อความในฉาก
        self.text_item = QGraphicsTextItem("Animated Text!")
        self.text_item.setFont(QFont("Arial", 20))
        self.text_item.setDefaultTextColor(Qt.GlobalColor.blue)
        self.scene.addItem(self.text_item)

        # กำหนดตำแหน่งเริ่มต้น
        self.text_item.setPos(0, 100)

        # ตั้ง Timer สำหรับการเคลื่อนไหว
        self.dx = 2  # การเคลื่อนที่ในแนวนอน
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)  # 60 FPS

    def animate(self):
        # เคลื่อนไหวในแนวนอน
        new_x = self.text_item.x() + self.dx
        if new_x > 300 or new_x < 0:  # เปลี่ยนทิศทางเมื่อถึงขอบ
            self.dx = -self.dx
        self.text_item.setPos(new_x, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = GraphicsTextAnimation()
    view.show()
    sys.exit(app.exec())
