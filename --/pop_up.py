import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class PopupWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' ')
        self.setFixedSize(370, 130)
        self.import_style('style_pop_up.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()


    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    def ui(self):
        self.layout = QVBoxLayout()
        self.addWidgetsToLayout(self.layout)

        self.setLayout(self.layout)

    def addWidgetsToLayout(self,ui):

        ui.addStretch()

        self.go_back_to_sign_up_label = QLabel('Go back to sign up?')
        self.go_back_to_sign_up_label.setObjectName('go_back_to_sign_up_label')
        self.go_back_to_sign_up_label.setFixedHeight(30)

        go_back_to_sign_up_label_layout = QHBoxLayout()
        go_back_to_sign_up_label_layout.addStretch()
        go_back_to_sign_up_label_layout.addWidget(self.go_back_to_sign_up_label)
        go_back_to_sign_up_label_layout.addStretch()
        ui.addLayout(go_back_to_sign_up_label_layout)

        ui.addSpacing(20)

        self.no_button = QPushButton('No')
        self.no_button.setObjectName('no_button')
        self.no_button.setFixedSize(145,40)
        self.no_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.no_button.clicked.connect(self.reject)
        # asdawd

        no_button_layout = QHBoxLayout()
        no_button_layout.setObjectName('no_button_layout')
        # no_button_layout.setContentsMargins(0,10,0,65)
        no_button_layout.addStretch()
        no_button_layout.addWidget(self.no_button)
        # no_button_layout.addStretch()
        ui.addLayout(no_button_layout)

        no_button_layout.addSpacing(10)

        self.yes_button = QPushButton('Yes')
        self.yes_button.setObjectName('yes_button')
        self.yes_button.setFixedSize(145,40)
        self.yes_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.yes_button.setStyleSheet('''
            QPushButton{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #f203ff, stop:1 #0099ff);
            color: aliceblue;
            border-radius: 20px;
            font-family: TeX Gyre Adventor;
            font-size: 12px;
            font-weight: 900;
            }
            QPushButton:hover{
            background: #ffffff;
            color: #d83aff;
            border-radius: 20px;
            border: 2px solid #f203ff;
            font-family: TeX Gyre Adventor;
            font-size: 12px;
            font-weight: 900;
            }
        ''')
        self.yes_button.clicked.connect(self.accept)
        no_button_layout.addWidget(self.yes_button)
        no_button_layout.addStretch()

        ui.addStretch()

    def change_label(self):
        self.go_back_to_sign_up_label.setText('Go back to forgot password?')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(475, 90, 700, 650)

        popup = PopupWindow()
        popup.move(425,-700)
        result = popup.exec()
        if result:
            popup.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.close()
    sys.exit(app.exec())
