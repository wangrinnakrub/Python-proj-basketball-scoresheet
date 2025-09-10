from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sqlite3

class Set_up_match(QMainWindow):
    switch_to_tournament_32_from_set_up_match = pyqtSignal()
    switch_to_competition_from_set_up_match = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basketball Score Sheet - Set Up Match')
        self.showMaximized()
        self.import_style('C:/Users/ASUS/OneDrive/Desktop/code/python/ED251007/project/style_zzz_set_up_match.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))

        # self.username = 'navyy'

        self.connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

        self.ui()


        QTimer.singleShot(0, self.clear_initial_focus)
        # self.installEventFilter(self)

    def clear_error_label(self):
        self.tournament_name_error_label.setText('')

    def clear_input_box(self):
        self.tournament_name_input_box.clear()

    def clear_initial_focus(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.tournament_name_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.tournament_name_input_box.clearFocus()
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    def ui(self):
        main_widget = QWidget()

        self.addWidgetsToLayout(main_widget)

        self.setCentralWidget(main_widget)

    def addWidgetsToLayout(self, parent):
        self.back_button = QPushButton(parent)
        self.back_button.setGeometry(15,10,40,40)
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_in')
        self.back_button.clicked.connect(self.switch_to_tournament_32_from_set_up_match.emit)
        self.back_button.setStyleSheet('''
            QPushButton#back_to_sign_in{
                background: transparent;
                background-color: transparent;
                border:none;
                border-radius: 20px;

            }
            QPushButton#back_to_sign_in:hover{
                background: transparent;
                background-color: rgb(226, 226, 226);
                border:none;
                border-radius: 20px;
            }''')

        self.set_up_match_label = QLabel('SET UP MATCH', parent)
        self.set_up_match_label.setObjectName('set_up_match_label')
        self.set_up_match_label.setGeometry(652, 40, 500, 50)
        self.set_up_match_label.setStyleSheet('''QLabel#set_up_match_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 40px;
        }''')

        # *-------------- select team --------------*#
        self.select_team_label = QLabel('Select teams', parent)
        self.select_team_label.setObjectName('select_team_label')
        self.select_team_label.setGeometry(675, 120, 162, 30)
        self.select_team_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.select_team_combobox = QComboBox(parent)
        self.select_team_combobox.setObjectName('select_team_combobox')
        self.select_team_combobox.setGeometry(632, 170, 250, 35)
        self.select_team_combobox.setCurrentIndex(-1)


        #*-------------- line up --------------*#

        self.team1_line_up_label = QLabel('', parent)
        self.team1_line_up_label.setObjectName('team1_line_up_label')
        self.team1_line_up_label.setGeometry(500, 250, 162, 40)
        self.team1_line_up_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vs_line_up_label = QLabel('VS', parent)
        self.vs_line_up_label.setObjectName('vs_line_up_label')
        self.vs_line_up_label.setGeometry(740, 258, 162, 40)
        self.vs_line_up_label.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.team2_line_up_label = QLabel('', parent)
        self.team2_line_up_label.setObjectName('team2_line_up_label')
        self.team2_line_up_label.setGeometry(843, 250, 162, 40)
        self.team2_line_up_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #*--------------- line up members 1 ---------------*#
        self.team1_line_up_player1_label = QLabel('', parent)
        self.team1_line_up_player1_label.setObjectName('team1_line_up_player1_label')
        self.team1_line_up_player1_label.setGeometry(500, 320, 110, 30)
        self.team1_line_up_player1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team1_line_up_player2_label = QLabel('', parent)
        self.team1_line_up_player2_label.setObjectName('team1_line_up_player2_label')
        self.team1_line_up_player2_label.setGeometry(500, 360, 110, 30)
        self.team1_line_up_player2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team1_line_up_player3_label = QLabel('', parent)
        self.team1_line_up_player3_label.setObjectName('team1_line_up_player3_label')
        self.team1_line_up_player3_label.setGeometry(500, 400, 110, 30)
        self.team1_line_up_player3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team1_line_up_player4_label = QLabel('', parent)
        self.team1_line_up_player4_label.setObjectName('team1_line_up_player4_label')
        self.team1_line_up_player4_label.setGeometry(500, 440, 110, 30)
        self.team1_line_up_player4_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team1_line_up_player5_label = QLabel('', parent)
        self.team1_line_up_player5_label.setObjectName('team1_line_up_player5_label')
        self.team1_line_up_player5_label.setGeometry(500, 480, 110, 30)
        self.team1_line_up_player5_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # * number
        self.team1_line_up_player1_number_label = QLabel('', parent)
        self.team1_line_up_player1_number_label.setObjectName('team1_line_up_player1_number_label')
        self.team1_line_up_player1_number_label.setGeometry(630, 320, 30, 30)
        self.team1_line_up_player1_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team1_line_up_player2_number_label = QLabel('', parent)
        self.team1_line_up_player2_number_label.setObjectName('team1_line_up_player2_number_label')
        self.team1_line_up_player2_number_label.setGeometry(630, 360, 30, 30)
        self.team1_line_up_player2_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team1_line_up_player3_number_label = QLabel('', parent)
        self.team1_line_up_player3_number_label.setObjectName('team1_line_up_player3_number_label')
        self.team1_line_up_player3_number_label.setGeometry(630, 400, 30, 30)
        self.team1_line_up_player3_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team1_line_up_player4_number_label = QLabel('', parent)
        self.team1_line_up_player4_number_label.setObjectName('team1_line_up_player4_number_label')
        self.team1_line_up_player4_number_label.setGeometry(630, 440, 30, 30)
        self.team1_line_up_player4_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team1_line_up_player5_number_label = QLabel('', parent)
        self.team1_line_up_player5_number_label.setObjectName('team1_line_up_player5_number_label')
        self.team1_line_up_player5_number_label.setGeometry(630, 480, 30, 30)
        self.team1_line_up_player5_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #*--------------- line up members 2 ---------------*#
        self.team2_line_up_player1_label = QLabel('', parent)
        self.team2_line_up_player1_label.setObjectName('team2_line_up_player1_label')
        self.team2_line_up_player1_label.setGeometry(843, 320, 110, 30)
        self.team2_line_up_player1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team2_line_up_player2_label = QLabel('', parent)
        self.team2_line_up_player2_label.setObjectName('team2_line_up_player2_label')
        self.team2_line_up_player2_label.setGeometry(843, 360, 110, 30)
        self.team2_line_up_player2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team2_line_up_player3_label = QLabel('', parent)
        self.team2_line_up_player3_label.setObjectName('team2_line_up_player3_label')
        self.team2_line_up_player3_label.setGeometry(843, 400, 110, 30)
        self.team2_line_up_player3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team2_line_up_player4_label = QLabel('', parent)
        self.team2_line_up_player4_label.setObjectName('team2_line_up_player4_label')
        self.team2_line_up_player4_label.setGeometry(843, 440, 110, 30)
        self.team2_line_up_player4_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team2_line_up_player5_label = QLabel('', parent)
        self.team2_line_up_player5_label.setObjectName('team2_line_up_player5_label')
        self.team2_line_up_player5_label.setGeometry(843, 480, 110, 30)
        self.team2_line_up_player5_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # * number
        self.team2_line_up_player1_number_label = QLabel('', parent)
        self.team2_line_up_player1_number_label.setObjectName('team2_line_up_player1_number_label')
        self.team2_line_up_player1_number_label.setGeometry(973, 320, 30, 30)
        self.team2_line_up_player1_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team2_line_up_player2_number_label = QLabel('', parent)
        self.team2_line_up_player2_number_label.setObjectName('team2_line_up_player2_number_label')
        self.team2_line_up_player2_number_label.setGeometry(973, 360, 30, 30)
        self.team2_line_up_player2_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team2_line_up_player3_number_label = QLabel('', parent)
        self.team2_line_up_player3_number_label.setObjectName('team2_line_up_player3_number_label')
        self.team2_line_up_player3_number_label.setGeometry(973, 400, 30, 30)
        self.team2_line_up_player3_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team2_line_up_player4_number_label = QLabel('', parent)
        self.team2_line_up_player4_number_label.setObjectName('team2_line_up_player4_number_label')
        self.team2_line_up_player4_number_label.setGeometry(973, 440, 30, 30)
        self.team2_line_up_player4_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team2_line_up_player5_number_label = QLabel('', parent)
        self.team2_line_up_player5_number_label.setObjectName('team2_line_up_player5_number_label')
        self.team2_line_up_player5_number_label.setGeometry(973, 480, 30, 30)
        self.team2_line_up_player5_number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #!-------------- select player team1 --------------*#
        self.select_team1_player1_label = QLabel('Select team 1 starting players', parent)
        self.select_team1_player1_label.setObjectName('select_team1_player1_label')
        self.select_team1_player1_label.setGeometry(140, 290, 310, 30)
        self.select_team1_player1_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.select_team1_player1_label_layout = QHBoxLayout()

        self.select_team1_player1_combobox = QComboBox(parent)
        self.select_team1_player1_combobox.setObjectName('select_team1_player1_combobox')
        self.select_team1_player1_combobox.setGeometry(183, 350, 162, 35)
        self.select_team1_player1_combobox.setCurrentIndex(-1)
        self.select_team1_player1_combobox.currentIndexChanged.connect(self.team1_player1_selected)
        self.select_team1_player1_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)


        self.select_team1_player2_combobox = QComboBox(parent)
        self.select_team1_player2_combobox.setObjectName('select_team1_player2_combobox')
        self.select_team1_player2_combobox.setGeometry(183, 410, 162, 35)
        self.select_team1_player2_combobox.setCurrentIndex(-1)
        self.select_team1_player2_combobox.currentIndexChanged.connect(self.team1_player2_selected)
        self.select_team1_player2_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)

        self.select_team1_player3_combobox = QComboBox(parent)
        self.select_team1_player3_combobox.setObjectName('select_team1_player3_combobox')
        self.select_team1_player3_combobox.setGeometry(183, 470, 162, 35)
        self.select_team1_player3_combobox.setCurrentIndex(-1)
        self.select_team1_player3_combobox.currentIndexChanged.connect(self.team1_player3_selected)
        self.select_team1_player3_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)

        self.select_team1_player4_combobox = QComboBox(parent)
        self.select_team1_player4_combobox.setObjectName('select_team1_player4_combobox')
        self.select_team1_player4_combobox.setGeometry(183, 530, 162, 35)
        self.select_team1_player4_combobox.setCurrentIndex(-1)
        self.select_team1_player4_combobox.currentIndexChanged.connect(self.team1_player4_selected)
        self.select_team1_player4_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)

        self.select_team1_player5_combobox = QComboBox(parent)
        self.select_team1_player5_combobox.setObjectName('select_team1_player5_combobox')
        self.select_team1_player5_combobox.setGeometry(183, 590, 162, 35)
        self.select_team1_player5_combobox.setCurrentIndex(-1)
        self.select_team1_player5_combobox.currentIndexChanged.connect(self.team1_player5_selected)
        self.select_team1_player5_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)


        #!-------------- select player team2 --------------*#
        self.select_team2_player1_label = QLabel('Select team 2 starting players', parent)
        self.select_team2_player1_label.setObjectName('select_team2_player1_label')
        self.select_team2_player1_label.setGeometry(1114, 290, 310, 30)
        self.select_team2_player1_label.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.select_team2_player1_combobox = QComboBox(parent)
        self.select_team2_player1_combobox.setObjectName('select_team2_player1_combobox')
        self.select_team2_player1_combobox.setGeometry(1170, 350, 162, 35)
        self.select_team2_player1_combobox.setCurrentIndex(-1)
        self.select_team2_player1_combobox.currentIndexChanged.connect(self.team2_player1_selected)
        self.select_team2_player1_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)

        self.select_team2_player2_combobox = QComboBox(parent)
        self.select_team2_player2_combobox.setObjectName('select_team2_player2_combobox')
        self.select_team2_player2_combobox.setGeometry(1170, 410, 162, 35)
        self.select_team2_player2_combobox.setCurrentIndex(-1)
        self.select_team2_player2_combobox.currentIndexChanged.connect(self.team2_player2_selected)
        self.select_team2_player2_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)

        self.select_team2_player3_combobox = QComboBox(parent)
        self.select_team2_player3_combobox.setObjectName('select_team2_player3_combobox')
        self.select_team2_player3_combobox.setGeometry(1170, 470, 162, 35)
        self.select_team2_player3_combobox.setCurrentIndex(-1)
        self.select_team2_player3_combobox.currentIndexChanged.connect(self.team2_player3_selected)
        self.select_team2_player3_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)

        self.select_team2_player4_combobox = QComboBox(parent)
        self.select_team2_player4_combobox.setObjectName('select_team2_player4_combobox')
        self.select_team2_player4_combobox.setGeometry(1170, 530, 162, 35)
        self.select_team2_player4_combobox.setCurrentIndex(-1)
        self.select_team2_player4_combobox.currentIndexChanged.connect(self.team2_player4_selected)
        self.select_team2_player4_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)

        self.select_team2_player5_combobox = QComboBox(parent)
        self.select_team2_player5_combobox.setObjectName('select_team2_player5_combobox')
        self.select_team2_player5_combobox.setGeometry(1170, 590, 162, 35)
        self.select_team2_player5_combobox.currentIndexChanged.connect(self.team2_player5_selected)
        self.select_team2_player5_combobox.setCurrentIndex(-1)
        self.select_team2_player5_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)


        #*-------------- team1 --------------*#
        self.select_team1_label = QLabel('Select team 1', parent)
        self.select_team1_label.setObjectName('select_team1_label')
        self.select_team1_label.setGeometry(135, 150, 162, 30)
        self.select_team1_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.select_team1_label.hide()


        self.select_team1_combobox = QComboBox(parent)
        self.select_team1_combobox.setObjectName('select_team1_combobox')
        self.select_team1_combobox.setGeometry(130, 210, 162, 35)
        self.select_team1_combobox.setCurrentIndex(-1)
        self.select_team1_combobox.hide()

        #*-------------- team2 --------------*#
        self.select_team2_label = QLabel('Select team 2', parent)
        self.select_team2_label.setObjectName('select_team2_label')
        self.select_team2_label.setGeometry(1225, 150, 162, 30)
        self.select_team2_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.select_team2_label.hide()

        self.select_team2_combobox = QComboBox(parent)
        self.select_team2_combobox.setObjectName('select_team2_combobox')
        self.select_team2_combobox.setGeometry(1220, 210, 162, 35)
        self.select_team2_combobox.setCurrentIndex(-1)
        self.select_team2_combobox.hide()


        self.competition_button = QPushButton('Competition', parent)
        self.competition_button.setObjectName('competition_button')
        self.competition_button.setStyleSheet('''
                                QPushButton{
                                    border-radius: 20px;
                                    border: 2px solid #2a2a2a;
                                    color: aliceblue;
                                    background: transparent;
                                    background-color: #2a2a2a;
                                    font-family: TeX Gyre Adventor;
                                    font-size: 14px;
                                    font-weight: 900;
                                }
                                QPushButton:hover{
                                    border-radius: 20px;
                                    border: 2px solid #2a2a2a;
                                    color: #2a2a2a;
                                    background: transparent;
                                    background-color: #f3f3f3;
                                    font-family: TeX Gyre Adventor;
                                    font-size: 14px;
                                    font-weight: 900;
                                }
                                        ''')
        self.competition_button.setGeometry(660, 680, 200, 40)
        self.competition_button.clicked.connect(self.switch_to_competition)

        # self.select_team1_player1_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)
        # self.select_team1_player2_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)
        # self.select_team1_player3_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)
        # self.select_team1_player4_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)
        # self.select_team1_player5_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)

        # self.select_team2_player1_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)
        # self.select_team2_player2_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)
        # self.select_team2_player3_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)
        # self.select_team2_player4_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)
        # self.select_team2_player5_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)

    def update_team1_comboboxes(self):
        # เก็บรายชื่อผู้เล่นที่ถูกเลือกแล้ว
        selected_players = [
            self.select_team1_player1_combobox.currentText(),
            self.select_team1_player2_combobox.currentText(),
            self.select_team1_player3_combobox.currentText(),
            self.select_team1_player4_combobox.currentText(),
            self.select_team1_player5_combobox.currentText()
        ]

        # อัปเดตรายชื่อในแต่ละ QComboBox
        all_players = [player[0] for player in self.cursor.execute('SELECT player_name FROM players WHERE team_id = ?', (self.team1_id,)).fetchall()]
        for combobox in [
            self.select_team1_player1_combobox,
            self.select_team1_player2_combobox,
            self.select_team1_player3_combobox,
            self.select_team1_player4_combobox,
            self.select_team1_player5_combobox
        ]:
            current_selection = combobox.currentText()
            combobox.blockSignals(True)  # ปิดสัญญาณชั่วคราวเพื่อป้องกันการเรียกฟังก์ชันซ้ำ
            combobox.clear()
            for player in all_players:
                if player not in selected_players or player == current_selection:
                    combobox.addItem(player)
            combobox.setCurrentText(current_selection)
            combobox.blockSignals(False)  # เปิดสัญญาณกลับ

    def update_team2_comboboxes(self):
        selected_players = [
            self.select_team2_player1_combobox.currentText(),
            self.select_team2_player2_combobox.currentText(),
            self.select_team2_player3_combobox.currentText(),
            self.select_team2_player4_combobox.currentText(),
            self.select_team2_player5_combobox.currentText()
        ]

        all_players = [player[0] for player in self.cursor.execute('SELECT player_name FROM players WHERE team_id = ?', (self.team2_id,)).fetchall()]
        for combobox in [
            self.select_team2_player1_combobox,
            self.select_team2_player2_combobox,
            self.select_team2_player3_combobox,
            self.select_team2_player4_combobox,
            self.select_team2_player5_combobox
        ]:
            current_selection = combobox.currentText()
            combobox.blockSignals(True)
            combobox.clear()
            for player in all_players:
                if player not in selected_players or player == current_selection:
                    combobox.addItem(player)
            combobox.setCurrentText(current_selection)
            combobox.blockSignals(False)

    def all_combobox_selected(self):
        comboboxes = [
            self.select_team_combobox,
            self.select_team1_player1_combobox,
            self.select_team1_player2_combobox,
            self.select_team1_player3_combobox,
            self.select_team1_player4_combobox,
            self.select_team1_player5_combobox,
            self.select_team2_player1_combobox,
            self.select_team2_player2_combobox,
            self.select_team2_player3_combobox,
            self.select_team2_player4_combobox,
            self.select_team2_player5_combobox
        ]

        for i, cb in enumerate(comboboxes):
            print(f"Combobox {i}: currentIndex = {cb.currentIndex()}")

        return all(cb.currentIndex() != -1 for cb in comboboxes)

    def switch_to_competition(self):
        if not self.all_combobox_selected():
            print("Not all comboboxes are selected")
            return
        else:
            self.switch_to_competition_from_set_up_match.emit()

    def check_team1_selected(self):
        index = self.select_team1_combobox.currentIndex()
        print('team1 current index in check team1 selected : ', self.select_team1_combobox.currentIndex())
        if index != -1:
            team1_selected = self.select_team1_combobox.currentText()
            print("Team selected : ", team1_selected)

            self.team1_id = self.team1_list[index][1]
            print('Updated team1 id = ', self.team1_id)

            # ล้างข้อมูลใน QComboBox ของผู้เล่น
            self.select_team1_player1_combobox.clear()
            self.select_team1_player2_combobox.clear()
            self.select_team1_player3_combobox.clear()
            self.select_team1_player4_combobox.clear()
            self.select_team1_player5_combobox.clear()

            # ดึงข้อมูลผู้เล่นจากฐานข้อมูล
            self.cursor.execute('SELECT player_name FROM players WHERE team_id = ?', (self.team1_id,))
            players = self.cursor.fetchall()
            for player in players:
                if player[0]:
                    # เพิ่มผู้เล่นใน QComboBox แต่ไม่ตั้งค่าเริ่มต้น
                    self.select_team1_player1_combobox.addItem(player[0])
                    self.select_team1_player2_combobox.addItem(player[0])
                    self.select_team1_player3_combobox.addItem(player[0])
                    self.select_team1_player4_combobox.addItem(player[0])
                    self.select_team1_player5_combobox.addItem(player[0])
                else:
                    print(f"Empty player name found: {player}")

            # ตั้งค่า QComboBox ให้ไม่มีการเลือกผู้เล่นเริ่มต้น

            self.select_team1_player1_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)
            self.select_team1_player2_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)
            self.select_team1_player3_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)
            self.select_team1_player4_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)
            self.select_team1_player5_combobox.currentIndexChanged.connect(self.update_team1_comboboxes)

            self.select_team1_player1_combobox.setCurrentIndex(-1)
            self.select_team1_player2_combobox.setCurrentIndex(-1)
            self.select_team1_player3_combobox.setCurrentIndex(-1)
            self.select_team1_player4_combobox.setCurrentIndex(-1)
            self.select_team1_player5_combobox.setCurrentIndex(-1)



            check_duplicate_team = self.check_team1_not_same()
            if check_duplicate_team == 0:
                return

            self.team1_line_up_label.setText(team1_selected)
        else:
            self.team1_line_up_label.setText('Team 1')
            print("No team selected")

    def check_team2_selected(self):
        index = self.select_team2_combobox.currentIndex()
        print('team2 current index : ', self.select_team2_combobox.currentIndex())
        if index != -1:
            team2_selected = self.select_team2_combobox.currentText()
            print("Team selected : ", team2_selected)

            self.team2_id = self.team2_list[index][1]
            print('Updated team2 id = ', self.team2_id)

            # ล้างข้อมูลใน QComboBox ของผู้เล่น
            self.select_team2_player1_combobox.clear()
            self.select_team2_player2_combobox.clear()
            self.select_team2_player3_combobox.clear()
            self.select_team2_player4_combobox.clear()
            self.select_team2_player5_combobox.clear()

            # ดึงข้อมูลผู้เล่นจากฐานข้อมูล
            self.cursor.execute('SELECT player_name FROM players WHERE team_id = ?', (self.team2_id,))
            players = self.cursor.fetchall()
            for player in players:
                if player[0]:
                    # เพิ่มผู้เล่นใน QComboBox แต่ไม่ตั้งค่าเริ่มต้น
                    self.select_team2_player1_combobox.addItem(player[0])
                    self.select_team2_player2_combobox.addItem(player[0])
                    self.select_team2_player3_combobox.addItem(player[0])
                    self.select_team2_player4_combobox.addItem(player[0])
                    self.select_team2_player5_combobox.addItem(player[0])
                else:
                    print(f"Empty player name found: {player}")

            # ตั้งค่า QComboBox ให้ไม่มีการเลือกผู้เล่นเริ่มต้น

            self.select_team2_player1_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)
            self.select_team2_player2_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)
            self.select_team2_player3_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)
            self.select_team2_player4_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)
            self.select_team2_player5_combobox.currentIndexChanged.connect(self.update_team2_comboboxes)

            self.select_team2_player1_combobox.setCurrentIndex(-1)
            self.select_team2_player2_combobox.setCurrentIndex(-1)
            self.select_team2_player3_combobox.setCurrentIndex(-1)
            self.select_team2_player4_combobox.setCurrentIndex(-1)
            self.select_team2_player5_combobox.setCurrentIndex(-1)


            check_duplicate_team = self.check_team2_not_same()
            if check_duplicate_team == 0:
                return

            self.team2_line_up_label.setText(team2_selected)
        else:
            self.team2_line_up_label.setText('Team 2')
            print("No team selected")

    def check_team1_not_same(self):
        if hasattr(self, 'team1_id') and hasattr(self, 'team2_id'):
            if self.team1_id == self.team2_id:
                print("Error in team 1 : Team 1 and Team 2 cannot be the same.")
                self.select_team1_combobox.setCurrentIndex(-1)
                return 0
            else:
                print("Teams are different.")

    def check_team2_not_same(self):
        if hasattr(self, 'team1_id') and hasattr(self, 'team2_id'):
            if self.team2_id == self.team1_id:
                print("Error in team 2 : Team 1 and Team 2 cannot be the same.")
                self.select_team2_combobox.setCurrentIndex(-1)
                return 0
            else:
                print("Teams are different.")

    def team1_player1_selected(self):
        self.team1_line_up_player1_label.setText(self.select_team1_player1_combobox.currentText())
        self.cursor.execute('SELECT player_number FROM players WHERE player_name = ?', (self.select_team1_player1_combobox.currentText(),))
        result = self.cursor.fetchone()
        if result is not None:
            player_number = result[0]
            self.team1_line_up_player1_number_label.setText(str(player_number))
        else:
            print("No player number found for the selected player.")
            self.team1_line_up_player1_number_label.setText('')
        if self.select_team1_player1_combobox.currentIndex() != -1:
            players = [
                self.select_team1_player2_combobox.currentText(),
                self.select_team1_player3_combobox.currentText(),
                self.select_team1_player4_combobox.currentText(),
                self.select_team1_player5_combobox.currentText()
            ]
            for i in players:
                if self.select_team1_player1_combobox.currentText() == i:
                    print('setting index team1 player1 to -1')
                    self.select_team1_player1_combobox.setCurrentIndex(-1)
                    return

    def team1_player2_selected(self):
        self.team1_line_up_player2_label.setText(self.select_team1_player2_combobox.currentText())
        print('team1 player2 name : ', self.select_team1_player2_combobox.currentText())
        self.cursor.execute('SELECT player_number FROM players WHERE player_name = ?', (self.select_team1_player2_combobox.currentText(),))
        result = self.cursor.fetchone()
        if result is not None:
            player_number = result[0]
            self.team1_line_up_player2_number_label.setText(str(player_number))
        else:
            print("No player number found for the selected player.")
            self.team1_line_up_player2_number_label.setText('')
        if self.select_team1_player2_combobox.currentIndex() != -1:
            players = [
                self.select_team1_player1_combobox.currentText(),
                self.select_team1_player3_combobox.currentText(),
                self.select_team1_player4_combobox.currentText(),
                self.select_team1_player5_combobox.currentText()
            ]
            for i in players:
                if self.select_team1_player2_combobox.currentText() == i:
                    print('setting index team1 player2 to -1')
                    self.select_team1_player2_combobox.setCurrentIndex(-1)
                    return

    def team1_player3_selected(self):
        self.team1_line_up_player3_label.setText(self.select_team1_player3_combobox.currentText())
        self.cursor.execute('SELECT player_number FROM players WHERE player_name = ?', (self.select_team1_player3_combobox.currentText(),))
        result = self.cursor.fetchone()
        if result is not None:
            player_number = result[0]
            self.team1_line_up_player3_number_label.setText(str(player_number))
        else:
            print("No player number found for the selected player.")
            self.team1_line_up_player3_number_label.setText('')
        if self.select_team1_player3_combobox.currentIndex() != -1:
            players = [
                self.select_team1_player1_combobox.currentText(),
                self.select_team1_player2_combobox.currentText(),
                self.select_team1_player4_combobox.currentText(),
                self.select_team1_player5_combobox.currentText()
            ]
            for i in players:
                if self.select_team1_player3_combobox.currentText() == i:
                    print('setting index team1 player3 to -1')
                    self.select_team1_player3_combobox.setCurrentIndex(-1)
                    return

    def team1_player4_selected(self):
        self.team1_line_up_player4_label.setText(self.select_team1_player4_combobox.currentText())
        self.cursor.execute('SELECT player_number FROM players WHERE player_name = ?', (self.select_team1_player4_combobox.currentText(),))
        result = self.cursor.fetchone()
        if result is not None:
            player_number = result[0]
            self.team1_line_up_player4_number_label.setText(str(player_number))
        else:
            print("No player number found for the selected player.")
            self.team1_line_up_player4_number_label.setText('')
            if self.select_team1_player4_combobox.currentIndex() != -1:
                players = [
                    self.select_team1_player1_combobox.currentText(),
                    self.select_team1_player2_combobox.currentText(),
                    self.select_team1_player3_combobox.currentText(),
                    self.select_team1_player5_combobox.currentText()
                ]
                for i in players:
                    if self.select_team1_player4_combobox.currentText() == i:
                        print('setting index team1 player4 to -1')
                        self.select_team1_player4_combobox.setCurrentIndex(-1)
                        return

    def team1_player5_selected(self):
        self.team1_line_up_player5_label.setText(self.select_team1_player5_combobox.currentText())
        self.cursor.execute('SELECT player_number FROM players WHERE player_name = ?', (self.select_team1_player5_combobox.currentText(),))
        result = self.cursor.fetchone()
        if result is not None:
            player_number = result[0]
            self.team1_line_up_player5_number_label.setText(str(player_number))
        else:
            print("No player number found for the selected player.")
            self.team1_line_up_player5_number_label.setText('')
        if self.select_team1_player5_combobox.currentIndex() != -1:
            players = [
                self.select_team1_player1_combobox.currentText(),
                self.select_team1_player2_combobox.currentText(),
                self.select_team1_player3_combobox.currentText(),
                self.select_team1_player4_combobox.currentText()
            ]
            for i in players:
                if self.select_team1_player5_combobox.currentText() == i:
                    print('setting index team1 player5 to -1')
                    self.select_team1_player5_combobox.setCurrentIndex(-1)
                    return

    def team2_player1_selected(self):
        self.team2_line_up_player1_label.setText(self.select_team2_player1_combobox.currentText())
        self.cursor.execute('SELECT player_number FROM players WHERE player_name = ?', (self.select_team2_player1_combobox.currentText(),))
        result = self.cursor.fetchone()
        if result is not None:
            player_number = result[0]
            self.team2_line_up_player1_number_label.setText(str(player_number))
        else:
            print("No player number found for the selected player.")
            self.team2_line_up_player1_number_label.setText('')
        if self.select_team2_player1_combobox.currentIndex() != -1:
            players = [
                self.select_team2_player2_combobox.currentText(),
                self.select_team2_player3_combobox.currentText(),
                self.select_team2_player4_combobox.currentText(),
                self.select_team2_player5_combobox.currentText()
            ]
            for i in players:
                if self.select_team2_player1_combobox.currentText() == i:
                    print('setting index team2 player1 to -1')
                    self.select_team2_player1_combobox.setCurrentIndex(-1)
                    return

    def team2_player2_selected(self):
        self.team2_line_up_player2_label.setText(self.select_team2_player2_combobox.currentText())
        self.cursor.execute('SELECT player_number FROM players WHERE player_name = ?', (self.select_team2_player2_combobox.currentText(),))
        result = self.cursor.fetchone()
        if result is not None:
            player_number = result[0]
            self.team2_line_up_player2_number_label.setText(str(player_number))
        else:
            print("No player number found for the selected player.")
            self.team2_line_up_player2_number_label.setText('')
        if self.select_team2_player2_combobox.currentIndex() != -1:
            players = [
                self.select_team2_player1_combobox.currentText(),
                self.select_team2_player3_combobox.currentText(),
                self.select_team2_player4_combobox.currentText(),
                self.select_team2_player5_combobox.currentText()
            ]
            for i in players:
                if self.select_team2_player2_combobox.currentText() == i:
                    print('setting index team2 player2 to -1')
                    self.select_team2_player2_combobox.setCurrentIndex(-1)
                    return

    def team2_player3_selected(self):
        self.team2_line_up_player3_label.setText(self.select_team2_player3_combobox.currentText())
        self.cursor.execute('SELECT player_number FROM players WHERE player_name = ?', (self.select_team2_player3_combobox.currentText(),))
        result = self.cursor.fetchone()
        if result is not None:
            player_number = result[0]
            self.team2_line_up_player3_number_label.setText(str(player_number))
        else:
            print("No player number found for the selected player.")
            self.team2_line_up_player3_number_label.setText('')
        if self.select_team2_player3_combobox.currentIndex() != -1:
            players = [
                self.select_team2_player1_combobox.currentText(),
                self.select_team2_player2_combobox.currentText(),
                self.select_team2_player4_combobox.currentText(),
                self.select_team2_player5_combobox.currentText()
            ]
            for i in players:
                if self.select_team2_player3_combobox.currentText() == i:
                    print('setting index team2 player3 to -1')
                    self.select_team2_player3_combobox.setCurrentIndex(-1)
                    return

    def team2_player4_selected(self):
        self.team2_line_up_player4_label.setText(self.select_team2_player4_combobox.currentText())
        self.cursor.execute('SELECT player_number FROM players WHERE player_name = ?', (self.select_team2_player4_combobox.currentText(),))
        result = self.cursor.fetchone()
        if result is not None:
            player_number = result[0]
            self.team2_line_up_player4_number_label.setText(str(player_number))
        else:
            print("No player number found for the selected player.")
            self.team2_line_up_player4_number_label.setText('')
        if self.select_team2_player4_combobox.currentIndex() != -1:
            players = [
                self.select_team2_player1_combobox.currentText(),
                self.select_team2_player2_combobox.currentText(),
                self.select_team2_player3_combobox.currentText(),
                self.select_team2_player5_combobox.currentText()
            ]
            for i in players:
                if self.select_team2_player4_combobox.currentText() == i:
                    print('setting index team2 player4 to -1')
                    self.select_team2_player4_combobox.setCurrentIndex(-1)
                    return

    def team2_player5_selected(self):
        self.team2_line_up_player5_label.setText(self.select_team2_player5_combobox.currentText())
        self.cursor.execute('SELECT player_number FROM players WHERE player_name = ?', (self.select_team2_player5_combobox.currentText(),))
        result = self.cursor.fetchone()
        if result is not None:
            player_number = result[0]
            self.team2_line_up_player5_number_label.setText(str(player_number))
        else:
            print("No player number found for the selected player.")
            self.team2_line_up_player5_number_label.setText('')
        if self.select_team2_player5_combobox.currentIndex() != -1:
            players = [
                self.select_team2_player1_combobox.currentText(),
                self.select_team2_player2_combobox.currentText(),
                self.select_team2_player3_combobox.currentText(),
                self.select_team2_player4_combobox.currentText()
            ]
            for i in players:
                if self.select_team2_player5_combobox.currentText() == i:
                    print('setting index team2 player5 to -1')
                    self.select_team2_player5_combobox.setCurrentIndex(-1)
                    return

    def _get_played_team_ids(self) -> set[int]:
        """
        คืนค่า set ของ team_id ที่เคยมีแมตช์แล้ว (ในตาราง matches)
        ถ้ามีคอลัมน์ username จะกรองตาม self.username ด้วย
        """
        played: set[int] = set()
        try:
            # ถ้า matches มีคอลัมน์ username
            self.cursor.execute("SELECT team1_id, team2_id FROM matches WHERE username = ?", (self.username,))
        except sqlite3.OperationalError:
            # เผื่อกรณีไม่มีคอลัมน์ username
            try:
                self.cursor.execute("SELECT team1_id, team2_id FROM matches")
            except sqlite3.OperationalError:
                # ยังไม่มีตาราง matches
                return played

        for t1, t2 in self.cursor.fetchall():
            if t1 is not None:
                played.add(t1)
            if t2 is not None:
                played.add(t2)
        return played


    # def get_username(self, username):
    #     self.select_team_combobox.clear()
    #     self.select_team1_combobox.clear()
    #     self.select_team2_combobox.clear()

    #     self.username = username

    #     self.cursor.execute('SELECT team_name, team_id FROM teams WHERE username = ?', (self.username,))
    #     teams = self.cursor.fetchall()


    #     self.match_pairs = []

    #     if len(teams) % 2 == 0:
    #         for i in range(0, len(teams), 2):
    #             team1_name, team1_id = teams[i]
    #             team2_name, team2_id = teams[i + 1]
    #             match_pair = f"{team1_name} vs {team2_name}"
    #             self.select_team_combobox.addItem(match_pair)
    #             self.match_pairs.append((team1_name, team1_id, team2_name, team2_id))
    #     else:
    #         print("จำนวนทีมไม่เป็นเลขคู่ ไม่สามารถจับคู่ได้")

    #     self.select_team_combobox.setCurrentIndex(-1)

    #     self.cursor.execute('SELECT team_name, team_id FROM teams WHERE username = ?', (self.username,))
    #     self.team1_list = self.cursor.fetchall()
    #     for team in self.team1_list:
    #         self.select_team1_combobox.addItem(team[0])
    #     self.team1_id = self.team1_list[0][1]

    #     self.select_team1_combobox.setCurrentIndex(-1)
    #     self.select_team1_combobox.currentIndexChanged.connect(self.check_team1_selected)
    #     print('team1 current index in get username: ',self.select_team1_combobox.currentIndex())

    #     self.cursor.execute('SELECT team_name, team_id FROM teams WHERE username = ?', (self.username,))
    #     self.team2_list = self.cursor.fetchall()
    #     for team in self.team2_list:
    #         self.select_team2_combobox.addItem(team[0])
    #     self.team2_id = self.team2_list[0][1]

    #     self.select_team2_combobox.setCurrentIndex(-1)
    #     self.select_team2_combobox.currentIndexChanged.connect(self.check_team2_selected)
    #     print('team2 current index : ',self.select_team2_combobox.currentIndex())

    #     self.select_team_combobox.currentIndexChanged.connect(self.update_selected_teams)

    def get_username(self, username):
        self.select_team_combobox.clear()
        self.select_team1_combobox.clear()
        self.select_team2_combobox.clear()

        self.username = username

        # ดึงทีมของ user ทั้งหมด
        self.cursor.execute('SELECT team_name, team_id FROM teams WHERE username = ?', (self.username,))
        teams = self.cursor.fetchall()

        # ✅ ดึงทีมที่แข่งไปแล้ว
        played_ids = self._get_played_team_ids()

        self.match_pairs = []

        # สร้างคู่ (จับเป็น 1v2, 3v4, ...) แต่ "ข้าม" ถ้ามีทีมใดในคู่นั้นแข่งแล้ว
        if len(teams) % 2 == 0:
            for i in range(0, len(teams), 2):
                team1_name, team1_id = teams[i]
                team2_name, team2_id = teams[i + 1]

                # ✅ ถ้าทีมใดทีมหนึ่งแข่งแล้ว ให้ข้าม ไม่ใส่ลง combobox
                if team1_id in played_ids or team2_id in played_ids:
                    continue

                self.select_team_combobox.addItem(f"{team1_name} vs {team2_name}")
                self.match_pairs.append((team1_name, team1_id, team2_name, team2_id))
        else:
            print("จำนวนทีมไม่เป็นเลขคู่ ไม่สามารถจับคู่ได้")

        self.select_team_combobox.setCurrentIndex(-1)

        # เติม combobox team1/2 แบบ "คัดกรองทีมที่แข่งแล้วออก"
        self.cursor.execute('SELECT team_name, team_id FROM teams WHERE username = ?', (self.username,))
        all_team1_list = self.cursor.fetchall()
        self.team1_list = [t for t in all_team1_list if t[1] not in played_ids]
        for team in self.team1_list:
            self.select_team1_combobox.addItem(team[0])
        if self.team1_list:
            self.team1_id = self.team1_list[0][1]
        self.select_team1_combobox.setCurrentIndex(-1)
        self.select_team1_combobox.currentIndexChanged.connect(self.check_team1_selected)
        print('team1 current index in get username: ', self.select_team1_combobox.currentIndex())

        self.cursor.execute('SELECT team_name, team_id FROM teams WHERE username = ?', (self.username,))
        all_team2_list = self.cursor.fetchall()
        self.team2_list = [t for t in all_team2_list if t[1] not in played_ids]
        for team in self.team2_list:
            self.select_team2_combobox.addItem(team[0])
        if self.team2_list:
            self.team2_id = self.team2_list[0][1]
        self.select_team2_combobox.setCurrentIndex(-1)
        self.select_team2_combobox.currentIndexChanged.connect(self.check_team2_selected)
        print('team2 current index : ', self.select_team2_combobox.currentIndex())

        self.select_team_combobox.currentIndexChanged.connect(self.update_selected_teams)


    def update_selected_teams(self):
        index = self.select_team_combobox.currentIndex()
        if index != -1:
            team1_name, team1_id, team2_name, team2_id = self.match_pairs[index]

            self.select_team1_combobox.setCurrentText(team1_name)
            self.select_team2_combobox.setCurrentText(team2_name)

            self.team1_id = team1_id
            self.team2_id = team2_id

            self.check_team1_selected()
            self.check_team2_selected()

    def fetch_username(self):
        return self.username

    def get_team1_info(self):
        return {
            'team1_id': self.team1_id,
            'team1_name': self.team1_line_up_label.text(),
            'team1_player1': self.team1_line_up_player1_number_label.text(),
            'team1_player2': self.team1_line_up_player2_number_label.text(),
            'team1_player3': self.team1_line_up_player3_number_label.text(),
            'team1_player4': self.team1_line_up_player4_number_label.text(),
            'team1_player5': self.team1_line_up_player5_number_label.text()
        }

    def get_team2_info(self):
        return {
            'team2_id': self.team2_id,
            'team2_name': self.team2_line_up_label.text(),
            'team2_player1': self.team2_line_up_player1_number_label.text(),
            'team2_player2': self.team2_line_up_player2_number_label.text(),
            'team2_player3': self.team2_line_up_player3_number_label.text(),
            'team2_player4': self.team2_line_up_player4_number_label.text(),
            'team2_player5': self.team2_line_up_player5_number_label.text()
        }

    def select_team_disconnect(self):
        self.select_team_combobox.currentIndexChanged.disconnect(self.update_selected_teams)

    def clear_all_combobox(self):
        self.select_team_combobox.setCurrentIndex(-1)
        self.select_team1_combobox.setCurrentIndex(-1)
        self.select_team2_combobox.setCurrentIndex(-1)

        self.select_team1_player1_combobox.setCurrentIndex(-1)
        self.select_team1_player2_combobox.setCurrentIndex(-1)
        self.select_team1_player3_combobox.setCurrentIndex(-1)
        self.select_team1_player4_combobox.setCurrentIndex(-1)
        self.select_team1_player5_combobox.setCurrentIndex(-1)

        self.select_team2_player1_combobox.setCurrentIndex(-1)
        self.select_team2_player2_combobox.setCurrentIndex(-1)
        self.select_team2_player3_combobox.setCurrentIndex(-1)
        self.select_team2_player4_combobox.setCurrentIndex(-1)
        self.select_team2_player5_combobox.setCurrentIndex(-1)


#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    set_up_match = Set_up_match()
    set_up_match.show()
    # tournament32.showMaximized()
    app.exec()
