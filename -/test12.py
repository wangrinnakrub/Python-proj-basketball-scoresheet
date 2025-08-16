import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer, Qt


class AlphabetChanger(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.current_index = 0
        self.alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]

        # Timer for changing text
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(70)  # 500 ms = 0.5 seconds

    def init_ui(self):
        # Create a QLabel
        self.label = QLabel("A", self)
        self.label.setStyleSheet("font-size: 48px; font-weight: bold;")

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Window properties
        self.setWindowTitle("Alphabet Changer")
        self.setGeometry(100, 100, 300, 200)

    def update_label(self):
        # Update the label text
        self.label.setText(self.alphabet[self.current_index])

        # Check if it is the last character
        if self.alphabet[self.current_index] == 'W':
            self.timer.stop()
        else:
            self.current_index += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AlphabetChanger()
    window.show()
    sys.exit(app.exec())
