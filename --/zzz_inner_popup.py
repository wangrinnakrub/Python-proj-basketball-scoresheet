import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class InnerPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' ')
        self.setFixedSize(370, 130)
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

    def ui(self):
        self.layout = QVBoxLayout()
        self.addWidgetsToLayout(self.layout)

        self.setLayout(self.layout)

    def addWidgetsToLayout(self,ui):

        ui.addStretch()

        self.notification_label = QLabel('Initial Text', self)
        self.notification_label.setObjectName('notification_label')
        self.notification_label.setStyleSheet('''
                    QLabel#notification_label{
                        font-family: Tex Gyre Adventor;
                        color: #313131;
                        font-size: 17px;
                        font-weight: bold;
                    }
                                                    ''')
        self.notification_label.setFixedHeight(30)

        notification_label_layout = QHBoxLayout()
        notification_label_layout.addStretch()
        notification_label_layout.addWidget(self.notification_label)
        notification_label_layout.addStretch()
        ui.addLayout(notification_label_layout)

        ui.addSpacing(20)

        self.no_button = QPushButton('Ok')
        self.no_button.setObjectName('no_button')
        self.no_button.setStyleSheet('''
            *{
                background-color: #f3f3f3;
            }
            #no_button{
                border-radius: 20px;
                color: aliceblue;
                background-color: #2f2f2f;
                font-family: TeX Gyre Adventor;
                font-size: 12px;
                font-weight: 900;
            }
            #no_button:hover{
                border-radius: 20px;
                border: 2px solid #2b2b2b;
                color: #1a1a1a;
                background-color: #f3f3f3;
                font-family: TeX Gyre Adventor;
                font-size: 12px;
                font-weight: 900;
            }

        ''')
        self.no_button.setFixedSize(145,40)
        self.no_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.no_button.clicked.connect(self.accept)

        no_button_layout = QHBoxLayout()
        no_button_layout.setObjectName('no_button_layout')
        # no_button_layout.setContentsMargins(0,10,0,65)
        no_button_layout.addStretch()
        no_button_layout.addWidget(self.no_button)
        no_button_layout.addStretch()
        ui.addLayout(no_button_layout)

        ui.addStretch()

    def change_label_to(self,text):
        self.notification_label.setText(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(475, 90, 700, 650)

        popup = InnerPopup()
        popup.move(450,250)
        result = popup.exec()
        if result:
            popup.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.close()
    sys.exit(app.exec())
