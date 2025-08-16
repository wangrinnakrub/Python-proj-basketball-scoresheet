import sys,sqlite3
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class AddPlayer(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' ')
        self.setMinimumSize(370, 570)
        self.import_style('style_zz_match_set_up_pop_up.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.connection = sqlite3.connect(r'C:/Users/ASUS/OneDrive/Desktop/Dabest/basketball_score_sheet.db')
        self.cursor = self.connection.cursor()
        QTimer.singleShot(0, self.clear_focus_from_all)

        self.installEventFilter(self)

    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    def clear_focus_from_all(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.player_name_input_box, self.player_number_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def ui(self):
        self.layout = QVBoxLayout()
        self.addWidgetsToLayout(self.layout)

        self.setLayout(self.layout)

    def addWidgetsToLayout(self, ui):

        # self.team_name_label = QLabel('Team name     ')
        self.team_name_label = QLabel('Team name')
        # self.team_name_label = QLabel('Team name       ')
        self.team_name_label.setObjectName('team_name_label')
        # self.team_name_label.setFixedSize(335,40)
        self.team_name_label.setFixedWidth(335)
        self.team_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.team_name_label_layout = QHBoxLayout()
        self.team_name_label_layout.addWidget(self.team_name_label)

        self.player_shirt = QPushButton('')
        self.player_shirt.setObjectName('player_shirt')
        self.player_shirt.setFixedSize(120, 170)
        self.player_shirt_layout = QHBoxLayout()
        self.player_shirt_layout.addWidget(self.player_shirt)

        self.player_name_under_shirt_label = QLabel('')
        self.player_name_under_shirt_label.setObjectName('player_name_under_shirt_label')
        # self.player_name_under_shirt_label.setFixedSize(350,40)
        self.player_name_under_shirt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.player_name_under_shirt_label_layout = QHBoxLayout()
        self.player_name_under_shirt_label_layout.addWidget(self.player_name_under_shirt_label)

        self.player_name_label = QLabel('Player name')
        self.player_name_label.setObjectName('player_name_label')
        self.player_name_label.setFixedSize(350,40)
        self.player_name_label_layout = QHBoxLayout()
        self.player_name_label_layout.addWidget(self.player_name_label)

        self.player_name_input_box = QLineEdit()
        self.player_name_input_box.setObjectName('player_name_input_box')
        self.player_name_input_box.setPlaceholderText('Type your player name')
        self.player_name_input_box.setFixedSize(305,40)
        self.player_name_input_box_layout = QHBoxLayout()
        self.player_name_input_box_layout.addWidget(self.player_name_input_box)
        self.player_name_input_box.textChanged.connect(self.player_name_under_shirt_label_real_time_change)

        self.player_number_label = QLabel('Player No.')
        self.player_number_label.setObjectName('player_number_label')
        self.player_number_label.setFixedSize(350,40)
        self.player_number_label_layout = QHBoxLayout()
        self.player_number_label_layout.addWidget(self.player_number_label)

        self.player_number_input_box = QLineEdit()
        self.player_number_input_box.setObjectName('player_number_input_box')
        self.player_number_input_box.setPlaceholderText('No.')
        self.player_number_input_box.setFixedSize(305,40)
        self.player_number_input_box_layout = QHBoxLayout()
        self.player_number_input_box_layout.addWidget(self.player_number_input_box)
        self.player_number_input_box.textChanged.connect(self.player_shirt_number_real_time_change)
        self.player_number_input_box.setValidator(QIntValidator(0, 99))

        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.setObjectName('cancel_button')
        self.cancel_button.setFixedSize(145,40)
        self.cancel_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.cancel_button.clicked.connect(self.reject)

        self.cancel_button_layout = QHBoxLayout()
        self.cancel_button_layout.setObjectName('cancel_button_layout')
        self.cancel_button_layout.addStretch()
        self.cancel_button_layout.addWidget(self.cancel_button)

        self.cancel_button_layout.addSpacing(10)

        self.ok_button = QPushButton('Ok')
        self.ok_button.setObjectName('ok_button')
        self.ok_button.setFixedSize(145,40)
        self.ok_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button_layout.addWidget(self.ok_button)
        self.cancel_button_layout.addStretch()

        ui.addStretch()
        ui.addLayout(self.team_name_label_layout)
        ui.addStretch()
        ui.addLayout(self.player_shirt_layout)
        ui.addLayout(self.player_name_under_shirt_label_layout)
        ui.addLayout(self.player_name_label_layout)
        ui.addLayout(self.player_name_input_box_layout)
        ui.addLayout(self.player_number_label_layout)
        ui.addLayout(self.player_number_input_box_layout)
        ui.addStretch()
        ui.addLayout(self.cancel_button_layout)
        ui.addStretch()

    def set_team_name_label(self, team_name):
        self.team_name_label.setText(team_name)

    def player_shirt_number_real_time_change(self):
        self.player_shirt.setText(self.player_number_input_box.text())

    def player_shirt_team1(self):
        self.player_shirt.setStyleSheet("""
            QPushButton#player_shirt {
                border-image: url('C:/pic/basketball_shirt_yellow_purple.png') 0 0 0 0 stretch stretch;
                color: #612ca4;

            }
        """)
        self.player_name_under_shirt_label.setStyleSheet("""
            QLabel#player_name_under_shirt_label{
                color: #612ca4;
                font-family: TeX Gyre Adventor;
                font-size: 27px;
                font-weight: 900;
            }
        """)

    def player_shirt_team2(self):
        self.player_shirt.setStyleSheet("""
            QPushButton#player_shirt {
                border-image: url('C:/pic/basketball_shirt_black_red.png') 0 0 0 0 stretch stretch;
                color: #c80000;
            }
        """)
        self.player_name_under_shirt_label.setStyleSheet("""
            QLabel#player_name_under_shirt_label{
                color: #c80000;
                font-family: TeX Gyre Adventor;
                font-size: 27px;
                font-weight: 900;
            }
        """)

    def player_name_under_shirt_label_real_time_change(self):
        self.player_name_under_shirt_label.setText(self.player_name_input_box.text())

    def get_player_shirt(self):
        return self.player_shirt

    def get_player_shirt_style(self):
        return self.player_shirt.setStyleSheet()

    def get_player_name_under_shirt_label(self):
        return self.player_name_under_shirt_label

    def get_player_name_under_shirt_label_style(self):
        return self.player_name_under_shirt_label.styleSheet()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(280, 90, 700, 650)

        show_popup_button = QPushButton("Show Popup", self)
        show_popup_button.clicked.connect(self.show_popup)
        show_popup_button.resize(show_popup_button.sizeHint())
        show_popup_button.move(150, 120)

    def show_popup(self):
        popup = AddPlayer()
        popup.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
