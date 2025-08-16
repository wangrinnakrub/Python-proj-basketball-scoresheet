from PyQt6.QtCore import QPropertyAnimation, QRect, QEvent, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(340, 110, 700, 650)

        self.username_input_box = QLineEdit()
        self.username_input_box.setObjectName('username_input_box')
        self.username_input_box.setPlaceholderText('Type your username')
        self.username_input_box.setFixedSize(305, 50)

        self.password_input_box = QLineEdit()
        self.password_input_box.setObjectName('password_input_box')
        self.password_input_box.setPlaceholderText('Type your password')
        self.password_input_box.setFixedSize(305, 50)

        self.login_button = QPushButton('Login')
        self.login_button.setObjectName('login_button')
        self.login_button.setFixedSize(305, 50)

        self.setup_ui()
        self.login_button.installEventFilter(self)  # ติดตั้ง Event Filter สำหรับปุ่มasdqwd

        # สร้างตัวแปรเก็บการอ้างอิงของอนิเมชันas
        self.expand_animation = QPropertyAnimation(self.login_button, b"geometry")
        self.shrink_animation = QPropertyAnimation(self.login_button, b"geometry")

        # เก็บขนาดเดิมของปุ่ม
        self.original_rect = self.login_button.geometry()

    def setup_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(10, 10, 10, 10)

        self.addWidgetsToLayout(self.layout)
        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

    def addWidgetsToLayout(self, layout):
        layout.addWidget(self.username_input_box)
        layout.addWidget(self.password_input_box)
        layout.addWidget(self.login_button)

    def eventFilter(self, obj, event):
        if obj == self.login_button:
            if event.type() == QEvent.Type.Enter:
                self.animate_button(True)
            elif event.type() == QEvent.Type.Leave:
                self.animate_button(False)
        return super().eventFilter(obj, event)

    def animate_button(self, expand):
        if expand:
            end_rect = QRect(self.original_rect.x() + 10, self.original_rect.y() - 5, self.original_rect.width() + 20, self.original_rect.height() + 10)
            self.expand_animation.setDuration(300)  # กำหนดระยะเวลาแอนิเมชัน
            self.expand_animation.setStartValue(self.original_rect)
            self.expand_animation.setEndValue(end_rect)
            self.expand_animation.start()
        else:
            self.shrink_animation.setDuration(300)
            self.shrink_animation.setStartValue(QRect(self.original_rect.x() - 10, self.original_rect.y() - 5, self.original_rect.width() + 20, self.original_rect.height() + 10))
            self.shrink_animation.setEndValue(self.original_rect)
            self.shrink_animation.start()

if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec()
