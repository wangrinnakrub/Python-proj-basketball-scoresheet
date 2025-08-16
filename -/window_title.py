from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QPushButton

class CustomTitleBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # ซ่อนไตเติ้ลบาร์แบบดั้งเดิม
        self.setGeometry(340, 110, 700, 650)
        self.setWindowTitle("Login")

        self.username_input_box = QLineEdit()
        self.username_input_box.setPlaceholderText('Type your username')
        self.username_input_box.setFixedSize(305, 50)

        self.password_input_box = QLineEdit()
        self.password_input_box.setPlaceholderText('Type your password')
        self.password_input_box.setFixedSize(305, 50)

        self.login_button = QPushButton('Login')
        self.login_button.setFixedSize(305, 50)

        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()
        self.title_bar = QHBoxLayout()
        self.title_bar.setContentsMargins(0, 0, 0, 0)
        self.title_bar.setSpacing(0)

        self.title_label = QLabel("Login")
        self.title_label.setStyleSheet("color: white; font-size: 18px;")
        self.title_bar.addWidget(self.title_label)

        self.close_button = QPushButton("X")
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("color: white; background-color: red;")
        self.title_bar.addWidget(self.close_button)

        self.layout.addLayout(self.title_bar)
        self.layout.addWidget(self.username_input_box)
        self.layout.addWidget(self.password_input_box)
        self.layout.addWidget(self.login_button)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = CustomTitleBar()
    window.show()
    app.exec()
