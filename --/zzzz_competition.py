from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sqlite3
from zzz_set_up_match import *
from datetime import datetime


class start_stop_timer(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.play_icon = 'C:\pic\play.png'
        self.stop_icon = 'C:\pic\stop.png'

        self.file_name = self.play_icon

        self.setFixedSize(74,74)
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(115,115))
        self.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    border-radius: 37px;
                    background: #2f2f2f;
                    margin: 0;
                    padding: 0;
                }}
                """)

        self.clicked.connect(self.on_button_clicked)

    def get_current_icon(self):
        return self.file_name

    def set_play_icon(self):
        self.file_name = self.play_icon
        self.setFixedSize(74,74)
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(115,115))
        self.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    border-radius: 37px;
                    background: #2f2f2f;
                    margin: 0;
                    padding: 0;
                }}
                """)

    def set_stop_icon(self):
        self.file_name = self.stop_icon
        self.setFixedSize(74,74)
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(115,115))
        self.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    border-radius: 37px;
                    background: #2f2f2f;
                    margin: 0;
                    padding: 0;
                }}
                """)

    def on_button_clicked(self):
        print(f"Button clicked! {self.file_name}")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("Left mouse button pressed!")
        super().mousePressEvent(event)

    def enterEvent(self, event):
        self.setFixedSize(74,74)
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(115,115))
        self.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    border-radius: 37px;
                    background: black;
                    margin: 0;
                    padding: 0;
                }}
                """)

        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setFixedSize(74,74)
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(115,115))
        self.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    border-radius: 37px;
                    background: #2f2f2f;
                    margin: 0;
                    padding: 0;
                }}
                """)

        super().leaveEvent(event)


class reset_game(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.play_icon = 'C:/pic/reset_icon.png'
        self.stop_icon = 'C:/pic/reset_icon.png'

        self.file_name = self.play_icon

        self.setFixedSize(74,74)
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(130,130))
        self.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    border-radius: 37px;
                    background: #ff9900;
                    margin: 0;
                    padding: 0;
                }}
                """)



        self.clicked.connect(self.on_button_clicked)

    def get_current_icon(self):
        return self.file_name

    def set_play_icon(self):
        self.file_name = self.play_icon
        self.setFixedSize(74,74)
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(130,130))
        self.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    border-radius: 37px;
                    background: #ff9900;
                    margin: 0;
                    padding: 0;
                }}
                """)

    def set_stop_icon(self):
        self.file_name = self.stop_icon
        self.setFixedSize(74,74)
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(130,130))
        self.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    border-radius: 37px;
                    background: #ff9900;
                    margin: 0;
                    padding: 0;
                }}
                """)

    def on_button_clicked(self):
        print(f"Button clicked! {self.file_name}")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("Left mouse button pressed!")
        super().mousePressEvent(event)

    def enterEvent(self, event):
        self.setFixedSize(74,74)
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(130,130))
        self.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    border-radius: 37px;
                    background: #dd8400;
                    margin: 0;
                    padding: 0;
                }}
                """)

        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setFixedSize(74,74)
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(130,130))
        self.setStyleSheet(f"""
                QPushButton {{
                    border: none;
                    border-radius: 37px;
                    background: #ff9900;
                    margin: 0;
                    padding: 0;
                }}
                """)

        super().leaveEvent(event)


class Competition(QMainWindow):
    switch_to_match_set_up_from_competition = pyqtSignal()
    switch_to_tournament_32_from_competition = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basketball Score Sheet - Set Up Match')
        self.showMaximized()
        self.import_style('C:/Users/ASUS/OneDrive/Desktop/code/python/ED251007/project/style_zzzz_competition.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))

        self.total_score_team1 = 0
        self.total_score_team2 = 0

        self.team1 = 00
        self.team2 = 00
        self.period = 1

        self.connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

        self.sub_mode_active = False
        self.selected_player_in = None
        self.selected_player_out = None
        self.timer_running = False
        self.current_time = 1 * 20

        self.starting_players_team1 = []
        self.starting_players_team2 = []

        self.substitution_history_team1 = []
        self.substitution_history_team2 = []

        self.foul_mode_active = False
        self.selected_foul_team = None

        self.foul_history_team1 = {}
        self.foul_history_team2 = {}

        self.period_winners = []

        self.ui()

        QTimer.singleShot(0, self.clear_initial_focus)

        # self.load_player_numbers(self.username)
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
        self.back_button.clicked.connect(self.switch_to_match_set_up_from_competition.emit)
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

        self.go_to_tournament32_button = QPushButton("Go to Tournament 32", parent)
        self.go_to_tournament32_button.setObjectName("go_to_tournament32_button")
        self.go_to_tournament32_button.setGeometry(1340, 20, 180, 40)  # กำหนดตำแหน่งและขนาดของปุ่ม
        self.go_to_tournament32_button.setStyleSheet('''
            QPushButton#go_to_tournament32_button {
                background: #00d527;
                color: white;
                border: 2px solid #00d527;
                border-radius: 20px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 16px;
            }
            QPushButton#go_to_tournament32_button:hover {
                background: #00ac1f;
                color: #ffffff;
                border: 2px solid #00d527;
            }
        ''')
        self.go_to_tournament32_button.clicked.connect(self.switch_to_tournament_32_from_competition.emit)
        self.go_to_tournament32_button.hide()

        # self.competition_label = QLabel('KKU GAME', parent)
        self.competition_label = QLabel('COMPETITION', parent)
        self.competition_label.setObjectName('competition_label')
        self.competition_label.setGeometry(550, 40, 400, 50)
        self.competition_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.competition_label.setStyleSheet('''QLabel#competition_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 40px;
        }''')

        self.team1_line_up_label = QLabel('Team1', parent)
        self.team1_line_up_label.setObjectName('team1_line_up_label')
        self.team1_line_up_label.setGeometry(100, 60, 162, 40)
        self.team1_line_up_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team2_line_up_label = QLabel('Team2', parent)
        self.team2_line_up_label.setObjectName('team2_line_up_label')
        self.team2_line_up_label.setGeometry(1245, 60, 162, 40)
        self.team2_line_up_label.setAlignment(Qt.AlignmentFlag.AlignCenter)




        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.time_label = QLabel('Time', parent)
        self.time_label.setObjectName('time_label')
        self.time_label.setGeometry(668, 100, 162, 40)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet('''QLabel#time_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')

        self.time_minute = QLabel('00', parent)
        self.time_minute.setGeometry(450, 50, 400, 300)
        self.time_minute.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_minute.setStyleSheet('''
                                         font-size: 150px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #ff2525;
                                         ''')

        self.time_colon = QLabel(':', parent)
        self.time_colon.setGeometry(550, 45, 400, 300)
        self.time_colon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_colon.setStyleSheet('''
                                            font-size: 150px;
                                            font-weight: bold;
                                            font-family: DS-Digital;
                                            color: #ff2525;
                                            ''')

        self.time_second = QLabel('20', parent)
        self.time_second.setGeometry(650, 50, 400, 300)
        self.time_second.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_second.setStyleSheet('''
                                         font-size: 150px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #ff2525;
                                         ''')

        self.period_label = QLabel('Period', parent)
        self.period_label.setObjectName('period_label')
        self.period_label.setGeometry(668, 270, 162, 40)
        self.period_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_label.setStyleSheet('''QLabel#period_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')

        self.period_number = QLabel('1', parent)
        self.period_number.setGeometry(550, 190, 400, 300)
        self.period_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_number.setStyleSheet('''
                                         font-size: 70px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #ff2525;
                                         ''')

        self.score_team1 = QLabel('0', parent)
        self.score_team1.setGeometry(250, 120, 400, 300)
        self.score_team1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_team1.setStyleSheet('''
                                         font-size: 150px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #00d527;
                                         ''')

        self.score_team2 = QLabel('0', parent)
        self.score_team2.setGeometry(850, 120, 400, 300)
        self.score_team2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_team2.setStyleSheet('''
                                         font-size: 150px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #00d527;
                                         ''')

        self.score_team1.hide()
        self.score_team2.hide()

        self.score_team1_all = QLabel('0', parent)
        self.score_team1_all.setGeometry(250, 120, 400, 300)
        self.score_team1_all.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_team1_all.setStyleSheet('''
                                         font-size: 150px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #00d527;
                                         ''')

        self.score_team2_all = QLabel('0', parent)
        self.score_team2_all.setGeometry(850, 120, 400, 300)
        self.score_team2_all.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_team2_all.setStyleSheet('''
                                         font-size: 150px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #00d527;
                                         ''')



        self.foul_team1 = QLabel('Foul', parent)
        self.foul_team1.setObjectName('foul_team1')
        self.foul_team1.setGeometry(560, 270, 162, 40)
        self.foul_team1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.foul_team1.setStyleSheet('''QLabel#foul_team1{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')

        self.foul_team1_number = QLabel('0', parent)
        self.foul_team1_number.setGeometry(440, 190, 400, 300)
        self.foul_team1_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.foul_team1_number.setStyleSheet('''
                                         font-size: 70px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #0023e8;
                                         ''')

        self.foul_team2 = QLabel('Foul', parent)
        self.foul_team2.setObjectName('foul_team2')
        self.foul_team2.setGeometry(774, 270, 162, 40)
        self.foul_team2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.foul_team2.setStyleSheet('''QLabel#foul_team2{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')

        self.foul_team2_number = QLabel('0', parent)
        self.foul_team2_number.setGeometry(657, 190, 400, 300)
        self.foul_team2_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.foul_team2_number.setStyleSheet('''
                                         font-size: 70px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #0023e8;
                                         ''')

        self.timer_button = start_stop_timer(parent)
        self.timer_button.setObjectName('timer_button')
        self.timer_button.setGeometry(715, 392, 400, 300)
        self.timer_button.clicked.connect(self.timer_button_clicked)

        self.reset_button = reset_game(parent)
        self.reset_button.setObjectName('reset_button')
        self.reset_button.setGeometry(715, 484, 400, 300)
        self.reset_button.clicked.connect(self.reset_values)

        self.foul_team1_button = QPushButton(parent)
        self.foul_team1_button.setObjectName('foul_team1_button')
        self.foul_team1_button.setText('Foul')
        self.foul_team1_button.setGeometry(597, 400, 90, 35)
        self.foul_team1_button.clicked.connect(lambda: self.increment_foul("team1"))
        self.foul_team1_button.setStyleSheet('''
            QPushButton#foul_team1_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#foul_team1_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_team2_button = QPushButton(parent)
        self.foul_team2_button.setObjectName('foul_team2_button')
        self.foul_team2_button.setText('Foul')
        self.foul_team2_button.setGeometry(815, 400, 90, 35)
        self.foul_team2_button.clicked.connect(lambda: self.increment_foul("team2"))
        self.foul_team2_button.setStyleSheet('''
            QPushButton#foul_team2_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#foul_team2_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')


        self.score_1_team1_button = QPushButton(parent)
        self.score_1_team1_button.setObjectName('score_1_team1_button')
        self.score_1_team1_button.setText('1')
        self.score_1_team1_button.setGeometry(405, 400, 90, 35)
        self.score_1_team1_button.clicked.connect(lambda: self.increment_score("team1", 1))
        self.score_1_team1_button.setStyleSheet('''
            QPushButton#score_1_team1_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#score_1_team1_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.score_2_team1_button = QPushButton(parent)
        self.score_2_team1_button.setObjectName('score_2_team1_button')
        self.score_2_team1_button.setText('2')
        self.score_2_team1_button.setGeometry(405, 445, 90, 35)
        self.score_2_team1_button.clicked.connect(lambda: self.increment_score("team1", 2))
        self.score_2_team1_button.setStyleSheet('''
            QPushButton#score_2_team1_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#score_2_team1_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.score_3_team1_button = QPushButton(parent)
        self.score_3_team1_button.setObjectName('score_3_team1_button')
        self.score_3_team1_button.setText('3')
        self.score_3_team1_button.setGeometry(405, 490, 90, 35)
        self.score_3_team1_button.clicked.connect(lambda: self.increment_score("team1", 3))
        self.score_3_team1_button.setStyleSheet('''
            QPushButton#score_3_team1_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#score_3_team1_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')


        self.score_1_team2_button = QPushButton(parent)
        self.score_1_team2_button.setObjectName('score_1_team2_button')
        self.score_1_team2_button.setText('1')
        self.score_1_team2_button.setGeometry(1007, 400, 90, 35)
        self.score_1_team2_button.clicked.connect(lambda: self.increment_score("team2", 1))
        self.score_1_team2_button.setStyleSheet('''
            QPushButton#score_1_team2_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#score_1_team2_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.score_2_team2_button = QPushButton(parent)
        self.score_2_team2_button.setObjectName('score_2_team2_button')
        self.score_2_team2_button.setText('2')
        self.score_2_team2_button.setGeometry(1007, 445, 90, 35)
        self.score_2_team2_button.clicked.connect(lambda: self.increment_score("team2", 2))
        self.score_2_team2_button.setStyleSheet('''
            QPushButton#score_2_team2_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#score_2_team2_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')


        self.score_3_team2_button = QPushButton(parent)
        self.score_3_team2_button.setObjectName('score_3_team2_button')
        self.score_3_team2_button.setText('3')
        self.score_3_team2_button.setGeometry(1007, 490, 90, 35)
        self.score_3_team2_button.clicked.connect(lambda: self.increment_score("team2", 3))
        self.score_3_team2_button.setStyleSheet('''
            QPushButton#score_3_team2_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#score_3_team2_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')


        self.timeout_team1_button = QPushButton(parent)
        self.timeout_team1_button.setObjectName('timeout_team1_button')
        self.timeout_team1_button.setText('Time out')
        self.timeout_team1_button.setGeometry(597, 445, 90, 35)
        self.timeout_team1_button.clicked.connect(lambda: self.timeout("team1"))
        self.timeout_team1_button.setStyleSheet('''
            QPushButton#timeout_team1_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#timeout_team1_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.timeout_team1_label = QLabel('5', parent)
        self.timeout_team1_label.setGeometry(525, 446, 50, 30)
        self.timeout_team1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeout_team1_label.setStyleSheet('''
                                         font-size: 32px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #ff2525;
                                         ''')
        self.timeout_team1_label.hide()

        self.timeout_team1_count = QLabel('0/2', parent)
        self.timeout_team1_count.setGeometry(524, 446, 50, 30)
        self.timeout_team1_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeout_team1_count.setStyleSheet('''
                                         font-size: 30px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #black;
                                         ''')
        self.team1_mode = QLabel('', parent)
        self.team1_mode.setObjectName('team1_mode')
        self.team1_mode.setGeometry(100, 130, 162, 40)
        self.team1_mode.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.team1_mode.setStyleSheet('''QLabel#team1_mode{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')

        self.team2_mode = QLabel('', parent)
        self.team2_mode.setObjectName('team2_mode')
        self.team2_mode.setGeometry(1245, 130, 162, 40)
        self.team2_mode.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.team2_mode.setStyleSheet('''QLabel#team2_mode{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')




        self.sub_team1_button = QPushButton(parent)
        self.sub_team1_button.setObjectName('sub_team1_button')
        self.sub_team1_button.setText('Sub')
        self.sub_team1_button.setGeometry(597, 490, 90, 35)
        self.sub_team1_button.clicked.connect(lambda: self.sub_mode("team1"))
        self.sub_team1_button.setStyleSheet('''
            QPushButton#sub_team1_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#sub_team1_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.timeout_team2_button = QPushButton(parent)
        self.timeout_team2_button.setObjectName('timeout_team2_button')
        self.timeout_team2_button.setText('Time out')
        self.timeout_team2_button.setGeometry(815, 445, 90, 35)
        self.timeout_team2_button.clicked.connect(lambda: self.timeout("team2"))
        self.timeout_team2_button.setStyleSheet('''
            QPushButton#timeout_team2_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#timeout_team2_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.timeout_team2_label = QLabel('5', parent)
        self.timeout_team2_label.setGeometry(930, 446, 50, 30)
        self.timeout_team2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeout_team2_label.setStyleSheet('''
                                         font-size: 32px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #ff2525;
                                         ''')
        self.timeout_team2_label.hide()

        self.timeout_team2_count = QLabel('0/2', parent)
        self.timeout_team2_count.setGeometry(930, 446, 50, 30)
        self.timeout_team2_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeout_team2_count.setStyleSheet('''
                                         font-size: 30px;
                                         font-weight: bold;
                                         font-family: DS-Digital;
                                         color: #black;
                                         ''')

        self.sub_team2_button = QPushButton(parent)
        self.sub_team2_button.setObjectName('sub_team2_button')
        self.sub_team2_button.setText('Sub')
        self.sub_team2_button.setGeometry(815, 490, 90, 35)
        self.sub_team2_button.clicked.connect(lambda: self.sub_mode("team2"))
        self.sub_team2_button.setStyleSheet('''
            QPushButton#sub_team2_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#sub_team2_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')


        self.player1_team1 = QPushButton(parent)
        self.player1_team1.setObjectName('player1_team1')
        self.player1_team1.setText('1')
        self.player1_team1.setGeometry(100, 200, 162, 40)
        self.player1_team1.setStyleSheet('''
            QPushButton#player1_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player1_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_player1_team1 = QLabel(parent)
        self.foul_player1_team1.setObjectName('foul_player1_team1')
        self.foul_player1_team1.setText('0')
        self.foul_player1_team1.setGeometry(10, 200, 80, 40)
        self.foul_player1_team1.setStyleSheet('''
            QLabel#foul_player1_team1{
                color: blue;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_player1_team1.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.player2_team1 = QPushButton(parent)
        self.player2_team1.setObjectName('player2_team1')
        self.player2_team1.setText('2')
        self.player2_team1.setGeometry(100, 255, 162, 40)
        self.player2_team1.setStyleSheet('''
            QPushButton#player2_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player2_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_player2_team1 = QLabel(parent)
        self.foul_player2_team1.setObjectName('foul_player2_team1')
        self.foul_player2_team1.setText('0')
        self.foul_player2_team1.setGeometry(10, 255, 80, 40)
        self.foul_player2_team1.setStyleSheet('''
            QLabel#foul_player2_team1{
                color: blue;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_player2_team1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.player3_team1 = QPushButton(parent)
        self.player3_team1.setObjectName('player3_team1')
        self.player3_team1.setText('3')
        self.player3_team1.setGeometry(100, 310, 162, 40)
        self.player3_team1.setStyleSheet('''
            QPushButton#player3_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player3_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_player3_team1 = QLabel(parent)
        self.foul_player3_team1.setObjectName('foul_player3_team1')
        self.foul_player3_team1.setText('0')
        self.foul_player3_team1.setGeometry(10, 310, 80, 40)
        self.foul_player3_team1.setStyleSheet('''
            QLabel#foul_player3_team1{
                color: blue;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_player3_team1.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.player4_team1 = QPushButton(parent)
        self.player4_team1.setObjectName('player4_team1')
        self.player4_team1.setText('4')
        self.player4_team1.setGeometry(100, 365, 162, 40)
        self.player4_team1.setStyleSheet('''
            QPushButton#player4_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player4_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_player4_team1 = QLabel(parent)
        self.foul_player4_team1.setObjectName('foul_player4_team1')
        self.foul_player4_team1.setText('0')
        self.foul_player4_team1.setGeometry(10, 365, 80, 40)
        self.foul_player4_team1.setStyleSheet('''
            QLabel#foul_player4_team1{
                color: blue;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_player4_team1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.player5_team1 = QPushButton(parent)
        self.player5_team1.setObjectName('player5_team1')
        self.player5_team1.setText('5')
        self.player5_team1.setGeometry(100, 420, 162, 40)
        self.player5_team1.setStyleSheet('''
            QPushButton#player5_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player5_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_player5_team1 = QLabel(parent)
        self.foul_player5_team1.setObjectName('foul_player5_team1')
        self.foul_player5_team1.setText('0')
        self.foul_player5_team1.setGeometry(10, 420, 80, 40)
        self.foul_player5_team1.setStyleSheet('''
            QLabel#foul_player5_team1{
                color: blue;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_player5_team1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.player1_team2 = QPushButton(parent)
        self.player1_team2.setObjectName('player1_team2')
        self.player1_team2.setText('1')
        self.player1_team2.setGeometry(1250, 200, 162, 40)
        self.player1_team2.setStyleSheet('''
            QPushButton#player1_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player1_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_player1_team2 = QLabel(parent)
        self.foul_player1_team2.setObjectName('foul_player1_team2')
        self.foul_player1_team2.setText('0')
        self.foul_player1_team2.setGeometry(1422, 200, 80, 40)
        self.foul_player1_team2.setStyleSheet('''
            QLabel#foul_player1_team2{
                color: blue;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_player1_team2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.player2_team2 = QPushButton(parent)
        self.player2_team2.setObjectName('player2_team2')
        self.player2_team2.setText('2')
        self.player2_team2.setGeometry(1250, 255, 162, 40)
        self.player2_team2.setStyleSheet('''
            QPushButton#player2_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player2_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_player2_team2 = QLabel(parent)
        self.foul_player2_team2.setObjectName('foul_player2_team2')
        self.foul_player2_team2.setText('0')
        self.foul_player2_team2.setGeometry(1422, 255, 80, 40)
        self.foul_player2_team2.setStyleSheet('''
            QLabel#foul_player2_team2{
                color: blue;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_player2_team2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.player3_team2 = QPushButton(parent)
        self.player3_team2.setObjectName('player3_team2')
        self.player3_team2.setText('3')
        self.player3_team2.setGeometry(1250, 310, 162, 40)
        self.player3_team2.setStyleSheet('''
            QPushButton#player3_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player3_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_player3_team2 = QLabel(parent)
        self.foul_player3_team2.setObjectName('foul_player3_team2')
        self.foul_player3_team2.setText('0')
        self.foul_player3_team2.setGeometry(1422, 310, 80, 40)
        self.foul_player3_team2.setStyleSheet('''
            QLabel#foul_player3_team2{
                color: blue;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_player3_team2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.player4_team2 = QPushButton(parent)
        self.player4_team2.setObjectName('player4_team2')
        self.player4_team2.setText('4')
        self.player4_team2.setGeometry(1250, 365, 162, 40)
        self.player4_team2.setStyleSheet('''
            QPushButton#player4_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player4_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_player4_team2 = QLabel(parent)
        self.foul_player4_team2.setObjectName('foul_player4_team2')
        self.foul_player4_team2.setText('0')
        self.foul_player4_team2.setGeometry(1422, 365, 80, 40)
        self.foul_player4_team2.setStyleSheet('''
            QLabel#foul_player4_team2{
                color: blue;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_player4_team2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.player5_team2 = QPushButton(parent)
        self.player5_team2.setObjectName('player5_team2')
        self.player5_team2.setText('5')
        self.player5_team2.setGeometry(1250, 420, 162, 40)
        self.player5_team2.setStyleSheet('''
            QPushButton#player5_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player5_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.foul_player5_team2 = QLabel(parent)
        self.foul_player5_team2.setObjectName('foul_player5_team2')
        self.foul_player5_team2.setText('0')
        self.foul_player5_team2.setGeometry(1422, 420, 80, 40)
        self.foul_player5_team2.setStyleSheet('''
            QLabel#foul_player5_team2{
                color: blue;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_player5_team2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.player6_team1 = QPushButton(parent)
        self.player6_team1.setObjectName('player6_team1')
        self.player6_team1.setText('6')
        self.player6_team1.setGeometry(20, 550, 162, 40)
        self.player6_team1.setStyleSheet('''
            QPushButton#player6_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player6_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player6_team1.hide()

        self.player7_team1 = QPushButton(parent)
        self.player7_team1.setObjectName('player7_team1')
        self.player7_team1.setText('7')
        self.player7_team1.setGeometry(20, 600, 162, 40)
        self.player7_team1.setStyleSheet('''
            QPushButton#player7_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player7_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player7_team1.hide()

        self.player8_team1 = QPushButton(parent)
        self.player8_team1.setObjectName('player8_team1')
        self.player8_team1.setText('8')
        self.player8_team1.setGeometry(20, 650, 162, 40)
        self.player8_team1.setStyleSheet('''
            QPushButton#player8_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player8_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player8_team1.hide()

        self.player9_team1 = QPushButton(parent)
        self.player9_team1.setObjectName('player9_team1')
        self.player9_team1.setText('9')
        self.player9_team1.setGeometry(192, 550, 162, 40)
        self.player9_team1.setStyleSheet('''
            QPushButton#player9_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player9_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player9_team1.hide()

        self.player10_team1 = QPushButton(parent)
        self.player10_team1.setObjectName('player10_team1')
        self.player10_team1.setText('10')
        self.player10_team1.setGeometry(192, 600, 162, 40)
        self.player10_team1.setStyleSheet('''
            QPushButton#player10_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player10_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player10_team1.hide()

        self.player11_team1 = QPushButton(parent)
        self.player11_team1.setObjectName('player11_team1')
        self.player11_team1.setText('11')
        self.player11_team1.setGeometry(192, 650, 162, 40)
        self.player11_team1.setStyleSheet('''
            QPushButton#player11_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player11_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player11_team1.hide()

        self.player12_team1 = QPushButton(parent)
        self.player12_team1.setObjectName('player12_team1')
        self.player12_team1.setText('12')
        self.player12_team1.setGeometry(105, 700, 162, 40)
        self.player12_team1.setStyleSheet('''
            QPushButton#player12_team1{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player12_team1:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player12_team1.hide()

        self.player6_team2 = QPushButton(parent)
        self.player6_team2.setObjectName('player6_team2')
        self.player6_team2.setText('6')
        self.player6_team2.setGeometry(1180, 550, 162, 40)
        self.player6_team2.setStyleSheet('''
            QPushButton#player6_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player6_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player6_team2.hide()

        self.player7_team2 = QPushButton(parent)
        self.player7_team2.setObjectName('player7_team2')
        self.player7_team2.setText('7')
        self.player7_team2.setGeometry(1180, 600, 162, 40)
        self.player7_team2.setStyleSheet('''
            QPushButton#player7_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player7_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player7_team2.hide()

        self.player8_team2 = QPushButton(parent)
        self.player8_team2.setObjectName('player8_team2')
        self.player8_team2.setText('8')
        self.player8_team2.setGeometry(1180, 650, 162, 40)
        self.player8_team2.setStyleSheet('''
            QPushButton#player8_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player8_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player8_team2.hide()

        self.player9_team2 = QPushButton(parent)
        self.player9_team2.setObjectName('player9_team2')
        self.player9_team2.setText('9')
        self.player9_team2.setGeometry(1350, 550, 162, 40)
        self.player9_team2.setStyleSheet('''
            QPushButton#player9_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player9_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player9_team2.hide()

        self.player10_team2 = QPushButton(parent)
        self.player10_team2.setObjectName('player10_team2')
        self.player10_team2.setText('10')
        self.player10_team2.setGeometry(1350, 600, 162, 40)
        self.player10_team2.setStyleSheet('''
            QPushButton#player10_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player10_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player10_team2.hide()

        self.player11_team2 = QPushButton(parent)
        self.player11_team2.setObjectName('player11_team2')
        self.player11_team2.setText('11')
        self.player11_team2.setGeometry(1350, 650, 162, 40)
        self.player11_team2.setStyleSheet('''
            QPushButton#player11_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player11_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player11_team2.hide()

        self.player12_team2 = QPushButton(parent)
        self.player12_team2.setObjectName('player12_team2')
        self.player12_team2.setText('12')
        self.player12_team2.setGeometry(1270, 700, 162, 40)
        self.player12_team2.setStyleSheet('''
            QPushButton#player12_team2{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#player12_team2:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.player12_team2.hide()

        self.team1_in_game = QLabel(parent)
        self.team1_in_game.setObjectName('team1_in_game')
        self.team1_in_game.setText('6')
        self.team1_in_game.setGeometry(120, 480, 162, 40)
        self.team1_in_game.setStyleSheet('''
            QLabel#team1_in_game{
                background: transparent;
                color: #ff2525;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 25px;
            }''')
        self.team1_in_game.hide()

        self.team1_exchange_icon = QPushButton(parent)
        self.team1_exchange_icon.setObjectName('team1_exchange_icon')
        self.team1_exchange_icon.setGeometry(153, 475, 60, 50)
        self.team1_exchange_icon.setStyleSheet('''
            QPushButton#team1_exchange_icon{
                border-image: url("C:/pic/exchange_icon.png");
            }''')
        self.team1_exchange_icon.hide()

        self.team1_out_game = QLabel(parent)
        self.team1_out_game.setObjectName('team1_out_game')
        self.team1_out_game.setText('6')
        self.team1_out_game.setGeometry(230, 480, 162, 40)
        self.team1_out_game.setStyleSheet('''
            QLabel#team1_out_game{
                background: transparent;
                color: #ff2525;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 25px;
            }''')
        self.team1_out_game.hide()

        self.team2_in_game = QLabel(parent)
        self.team2_in_game.setObjectName('team2_in_game')
        self.team2_in_game.setText('6')
        self.team2_in_game.setGeometry(1275, 480, 162, 40)
        self.team2_in_game.setStyleSheet('''
            QLabel#team2_in_game{
                background: transparent;
                color: #ff2525;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 25px;
            }''')
        self.team2_in_game.hide()

        self.team2_exchange_icon = QPushButton(parent)
        self.team2_exchange_icon.setObjectName('team2_exchange_icon')
        self.team2_exchange_icon.setGeometry(1303, 475, 60, 50)
        self.team2_exchange_icon.setStyleSheet('''
            QPushButton#team2_exchange_icon{
                border-image: url("C:/pic/exchange_icon.png");
            }''')
        self.team2_exchange_icon.hide()

        self.team2_out_game = QLabel(parent)
        self.team2_out_game.setObjectName('team2_out_game')
        self.team2_out_game.setText('6')
        self.team2_out_game.setGeometry(1380, 480, 162, 40)
        self.team2_out_game.setStyleSheet('''
            QLabel#team2_out_game{
                background: transparent;
                color: #ff2525;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 25px;
            }''')
        self.team2_out_game.hide()



        self.player1_team1.clicked.connect(lambda: self.check_player_click("player1_team1"))
        self.player2_team1.clicked.connect(lambda: self.check_player_click("player2_team1"))
        self.player3_team1.clicked.connect(lambda: self.check_player_click("player3_team1"))
        self.player4_team1.clicked.connect(lambda: self.check_player_click("player4_team1"))
        self.player5_team1.clicked.connect(lambda: self.check_player_click("player5_team1"))

        self.player6_team1.clicked.connect(lambda: self.check_player_click("player6_team1"))
        self.player7_team1.clicked.connect(lambda: self.check_player_click("player7_team1"))
        self.player8_team1.clicked.connect(lambda: self.check_player_click("player8_team1"))
        self.player9_team1.clicked.connect(lambda: self.check_player_click("player9_team1"))
        self.player10_team1.clicked.connect(lambda: self.check_player_click("player10_team1"))
        self.player11_team1.clicked.connect(lambda: self.check_player_click("player11_team1"))
        self.player12_team1.clicked.connect(lambda: self.check_player_click("player12_team1"))


        self.player1_team2.clicked.connect(lambda: self.check_player_click("player1_team2"))
        self.player2_team2.clicked.connect(lambda: self.check_player_click("player2_team2"))
        self.player3_team2.clicked.connect(lambda: self.check_player_click("player3_team2"))
        self.player4_team2.clicked.connect(lambda: self.check_player_click("player4_team2"))
        self.player5_team2.clicked.connect(lambda: self.check_player_click("player5_team2"))

        self.player6_team2.clicked.connect(lambda: self.check_player_click("player6_team2"))
        self.player7_team2.clicked.connect(lambda: self.check_player_click("player7_team2"))
        self.player8_team2.clicked.connect(lambda: self.check_player_click("player8_team2"))
        self.player9_team2.clicked.connect(lambda: self.check_player_click("player9_team2"))
        self.player10_team2.clicked.connect(lambda: self.check_player_click("player10_team2"))
        self.player11_team2.clicked.connect(lambda: self.check_player_click("player11_team2"))
        self.player12_team2.clicked.connect(lambda: self.check_player_click("player12_team2"))

        self.period_1_final_label = QLabel('Period', parent)
        self.period_1_final_label.setObjectName('period_1_final_label')
        self.period_1_final_label.setGeometry(400, 580, 162, 40)
        self.period_1_final_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_1_final_label.setStyleSheet('''QLabel#period_1_final_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_1_final_label.hide()

        self.period_2_final_label = QLabel('Period', parent)
        self.period_2_final_label.setObjectName('period_2_final_label')
        self.period_2_final_label.setGeometry(570, 580, 162, 40)
        self.period_2_final_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_2_final_label.setStyleSheet('''QLabel#period_2_final_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_2_final_label.hide()

        self.period_3_final_label = QLabel('Period', parent)
        self.period_3_final_label.setObjectName('period_3_final_label')
        self.period_3_final_label.setGeometry(777, 580, 162, 40)
        self.period_3_final_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_3_final_label.setStyleSheet('''QLabel#period_3_final_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_3_final_label.hide()

        self.period_4_final_label = QLabel('Period', parent)
        self.period_4_final_label.setObjectName('period_4_final_label')
        self.period_4_final_label.setGeometry(947, 580, 162, 40)
        self.period_4_final_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_4_final_label.setStyleSheet('''QLabel#period_4_final_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_4_final_label.hide()

        self.period_1_final_number = QLabel('1', parent)
        self.period_1_final_number.setObjectName('period_1_final_number')
        self.period_1_final_number.setGeometry(400, 610, 162, 40)
        self.period_1_final_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_1_final_number.setStyleSheet('''QLabel#period_1_final_number{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_1_final_number.hide()

        self.period_2_final_number = QLabel('2', parent)
        self.period_2_final_number.setObjectName('period_2_final_number')
        self.period_2_final_number.setGeometry(570, 610, 162, 40)
        self.period_2_final_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_2_final_number.setStyleSheet('''QLabel#period_2_final_number{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_2_final_number.hide()

        self.period_3_final_number = QLabel('3', parent)
        self.period_3_final_number.setObjectName('period_3_final_number')
        self.period_3_final_number.setGeometry(777, 610, 162, 40)
        self.period_3_final_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_3_final_number.setStyleSheet('''QLabel#period_3_final_number{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_3_final_number.hide()

        self.period_4_final_number = QLabel('4', parent)
        self.period_4_final_number.setObjectName('period_4_final_number')
        self.period_4_final_number.setGeometry(947, 610, 162, 40)
        self.period_4_final_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_4_final_number.setStyleSheet('''QLabel#period_4_final_number{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_4_final_number.hide()

        self.period_1_final_colon = QLabel(':', parent)
        self.period_1_final_colon.setObjectName('period_1_final_colon')
        self.period_1_final_colon.setGeometry(400, 640, 162, 40)
        self.period_1_final_colon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_1_final_colon.setStyleSheet('''QLabel#period_1_final_colon{
            background: transparent;
            color: black;
            font-family: DS - Digital;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_1_final_colon.hide()

        self.period_2_final_colon = QLabel(':', parent)
        self.period_2_final_colon.setObjectName('period_2_final_colon')
        self.period_2_final_colon.setGeometry(570, 640, 162, 40)
        self.period_2_final_colon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_2_final_colon.setStyleSheet('''QLabel#period_2_final_colon{
            background: transparent;
            color: black;
            font-family: DS - Digital;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_2_final_colon.hide()

        self.period_3_final_colon = QLabel(':', parent)
        self.period_3_final_colon.setObjectName('period_3_final_colon')
        self.period_3_final_colon.setGeometry(777, 640, 162, 40)
        self.period_3_final_colon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_3_final_colon.setStyleSheet('''QLabel#period_3_final_colon{
            background: transparent;
            color: black;
            font-family: DS - Digital;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_3_final_colon.hide()

        self.period_4_final_colon = QLabel(':', parent)
        self.period_4_final_colon.setObjectName('period_4_final_colon')
        self.period_4_final_colon.setGeometry(947, 640, 162, 40)
        self.period_4_final_colon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_4_final_colon.setStyleSheet('''QLabel#period_4_final_colon{
            background: transparent;
            color: black;
            font-family: DS - Digital;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.period_4_final_colon.hide()

        self.period_1_team1_final_score = QLabel('000', parent)
        self.period_1_team1_final_score.setObjectName('period_1_team1_final_score')
        self.period_1_team1_final_score.setGeometry(360, 642, 162, 40)
        self.period_1_team1_final_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_1_team1_final_score.setStyleSheet('''QLabel#period_1_team1_final_score{
            background: transparent;
            color: black;
            font-family: DS-Digital;
            font-weight: 780;
            font-size: 40px;
        }''')
        self.period_1_team1_final_score.hide()

        self.period_1_team2_final_score = QLabel('000', parent)
        self.period_1_team2_final_score.setObjectName('period_1_team2_final_score')
        self.period_1_team2_final_score.setGeometry(440, 642, 162, 40)
        self.period_1_team2_final_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_1_team2_final_score.setStyleSheet('''QLabel#period_1_team2_final_score{
            background: transparent;
            color: black;
            font-family: DS-Digital;
            font-weight: 780;
            font-size: 40px;
        }''')
        self.period_1_team2_final_score.hide()

        self.period_2_team1_final_score = QLabel('000', parent)
        self.period_2_team1_final_score.setObjectName('period_2_team1_final_score')
        self.period_2_team1_final_score.setGeometry(530, 642, 162, 40)
        self.period_2_team1_final_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_2_team1_final_score.setStyleSheet('''QLabel#period_2_team1_final_score{
            background: transparent;
            color: black;
            font-family: DS-Digital;
            font-weight: 780;
            font-size: 40px;
        }''')
        self.period_2_team1_final_score.hide()

        self.period_2_team2_final_score = QLabel('000', parent)
        self.period_2_team2_final_score.setObjectName('period_2_team2_final_score')
        self.period_2_team2_final_score.setGeometry(610, 642, 162, 40)
        self.period_2_team2_final_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_2_team2_final_score.setStyleSheet('''QLabel#period_2_team2_final_score{
            background: transparent;
            color: black;
            font-family: DS-Digital;
            font-weight: 780;
            font-size: 40px;
        }''')
        self.period_2_team2_final_score.hide()

        self.period_3_team1_final_score = QLabel('000', parent)
        self.period_3_team1_final_score.setObjectName('period_3_team1_final_score')
        self.period_3_team1_final_score.setGeometry(735, 642, 162, 40)
        self.period_3_team1_final_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_3_team1_final_score.setStyleSheet('''QLabel#period_3_team1_final_score{
            background: transparent;
            color: black;
            font-family: DS-Digital;
            font-weight: 780;
            font-size: 40px;
        }''')
        self.period_3_team1_final_score.hide()

        self.period_3_team2_final_score = QLabel('000', parent)
        self.period_3_team2_final_score.setObjectName('period_3_team2_final_score')
        self.period_3_team2_final_score.setGeometry(820, 642, 162, 40)
        self.period_3_team2_final_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_3_team2_final_score.setStyleSheet('''QLabel#period_3_team2_final_score{
            background: transparent;
            color: black;
            font-family: DS-Digital;
            font-weight: 780;
            font-size: 40px;
        }''')
        self.period_3_team2_final_score.hide()

        self.period_4_team1_final_score = QLabel('000', parent)
        self.period_4_team1_final_score.setObjectName('period_4_team1_final_score')
        self.period_4_team1_final_score.setGeometry(905, 642, 162, 40)
        self.period_4_team1_final_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_4_team1_final_score.setStyleSheet('''QLabel#period_4_team1_final_score{
            background: transparent;
            color: black;
            font-family: DS-Digital;
            font-weight: 780;
            font-size: 40px;
        }''')
        self.period_4_team1_final_score.hide()

        self.period_4_team2_final_score = QLabel('000', parent)
        self.period_4_team2_final_score.setObjectName('period_4_team2_final_score')
        self.period_4_team2_final_score.setGeometry(990, 642, 162, 40)
        self.period_4_team2_final_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.period_4_team2_final_score.setStyleSheet('''QLabel#period_4_team2_final_score{
            background: transparent;
            color: black;
            font-family: DS-Digital;
            font-weight: 780;
            font-size: 40px;
        }''')
        self.period_4_team2_final_score.hide()


        self.winner = QLabel('WINNER', parent)
        self.winner.setObjectName('winner')
        self.winner.setGeometry(673, 690, 162, 40)
        self.winner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.winner.setStyleSheet('''QLabel#winner{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.winner.hide()

        self.winner_name = QLabel('WINNER_name', parent)
        self.winner_name.setObjectName('winner_name')
        self.winner_name.setGeometry(673, 730, 162, 40)
        self.winner_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.winner_name.setStyleSheet('''QLabel#winner_name{
            background: transparent;
            color: #00d527;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.winner_name.hide()


    def update_foul_labels(self):
        # ทีม 1: ปุ่มตัวจริง 1-5
        for slot_name in ["player1_team1", "player2_team1", "player3_team1", "player4_team1", "player5_team1"]:
            btn = self.findChild(QPushButton, slot_name)
            lbl = self.findChild(QLabel, f"foul_{slot_name}")  # ชื่อ label = 'foul_' + ชื่อปุ่ม
            if btn and lbl:
                number = btn.text()
                count = self.foul_history_team1.get(number, 0)
                lbl.setText(str(count))

        # ทีม 2: ปุ่มตัวจริง 1-5
        for slot_name in ["player1_team2", "player2_team2", "player3_team2", "player4_team2", "player5_team2"]:
            btn = self.findChild(QPushButton, slot_name)
            lbl = self.findChild(QLabel, f"foul_{slot_name}")
            if btn and lbl:
                number = btn.text()
                count = self.foul_history_team2.get(number, 0)
                lbl.setText(str(count))

    def get_team_name(self, team_id):
        """
        ดึงชื่อทีมจาก team_id
        :param team_id: รหัสของทีม
        :return: ชื่อทีม (team_name) หรือ None หากไม่พบ
        """
        connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        cursor = connection.cursor()

        cursor.execute("""
            SELECT team_name
            FROM teams
            WHERE team_id = ?
        """, (team_id,))
        result = cursor.fetchone()

        connection.close()

        if result:
            return result[0]  # คืนค่าชื่อทีม
        else:
            return None  # หากไม่พบ team_id

    def update_match_winner(self, match_id, winner):
        """
        อัปเดตผู้ชนะในตาราง matches โดยใช้ match_id
        :param match_id: รหัสของแมตช์
        :param winner: ชื่อของทีมที่ชนะ (Team 1, Team 2 หรือ Draw)
        """
        connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE matches
            SET winner = ?
            WHERE match_id = ?
        """, (winner, match_id))

        connection.commit()
        connection.close()

        print(f"✅ Updated winner for match_id {match_id}: {winner}")

    # def calculate_final_winner(self):
    #     team1_wins = self.period_winners.count("Team 1")
    #     team2_wins = self.period_winners.count("Team 2")

    #     if team1_wins > team2_wins:
    #         final_winner = self.get_team_name(self.team1_id)  # ดึงชื่อทีมจาก team1_id
    #         self.update_match_winner(self.match_id, final_winner)
    #     elif team2_wins > team1_wins:
    #         final_winner = self.get_team_name(self.team2_id)  # ดึงชื่อทีมจาก team2_id
    #         self.update_match_winner(self.match_id, final_winner)
    #     else:
    #         final_winner = "Draw"

    #     # แสดงผลผู้ชนะใน UI
    #     self.winner.show()
    #     if final_winner == "Draw":
    #         self.winner_name.setText("Draw")
    #         self.winner_name.setStyleSheet('''QLabel#winner_name{
    #             background: transparent;
    #             color: #ff2525;
    #             font-family: Saira Condensed;
    #             font-weight: 780;
    #             font-size: 20px;
    #         }''')
    #     else:
    #         self.winner_name.setText(final_winner)
    #         self.winner_name.setStyleSheet('''QLabel#winner_name{
    #             background: transparent;
    #             color: #00d527;
    #             font-family: Saira Condensed;
    #             font-weight: 780;
    #             font-size: 20px;
    #         }''')
    #     self.winner_name.show()

    #     print(f"Final Winner: {final_winner}")
    #     QMessageBox.information(self, "Final Winner", f"The final winner is: {final_winner}")
    #     self.go_to_tournament32_button.show()

    def calculate_final_winner(self):
        """
        ตัดสินผู้ชนะจากผลของ period สุดท้ายเท่านั้น
        - ถ้า period สุดท้าย Team 1 ชนะ -> บันทึกชื่อทีม 1
        - ถ้า period สุดท้าย Team 2 ชนะ -> บันทึกชื่อทีม 2
        - ถ้าเสมอ -> Draw
        """
        # เผื่อกรณี edge case ยังไม่มีการบันทึก winner ของช่วงก่อนหน้า
        if not self.period_winners:
            # fallback จากสกอร์ปัจจุบันในจอ
            t1 = int(self.score_team1.text())
            t2 = int(self.score_team2.text())
            last_period_winner = "Team 1" if t1 > t2 else ("Team 2" if t2 > t1 else "Draw")
        else:
            # ผู้ชนะของ period สุดท้าย
            last_period_winner = self.period_winners[-1]

        if last_period_winner == "Team 1":
            final_winner = self.get_team_name(self.team1_id)
            self.update_match_winner(self.match_id, final_winner)
        elif last_period_winner == "Team 2":
            final_winner = self.get_team_name(self.team2_id)
            self.update_match_winner(self.match_id, final_winner)
        else:
            final_winner = "Draw"

        # อัปเดต UI
        self.winner.show()
        if final_winner == "Draw":
            self.winner_name.setText("Draw")
            self.winner_name.setStyleSheet('''QLabel#winner_name{
                background: transparent;
                color: #ff2525;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        else:
            self.winner_name.setText(final_winner)
            self.winner_name.setStyleSheet('''QLabel#winner_name{
                background: transparent;
                color: #00d527;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.winner_name.show()

        print(f"Final Winner (by last period): {final_winner}")
        QMessageBox.information(self, "Final Winner", f"The final winner is: {final_winner}")
        self.go_to_tournament32_button.show()


    def show_period_summary(self):
        if self.period == 1:
            self.period_1_final_label.show()
            self.period_1_final_number.show()
            self.period_1_final_colon.show()
            self.period_1_team1_final_score.setText(self.score_team1_all.text())
            self.period_1_team2_final_score.setText(self.score_team2_all.text())
            self.period_1_team1_final_score.show()
            self.period_1_team2_final_score.show()

            team1_score = self.score_team1_all.text()
            team2_score = self.score_team2_all.text()
            if team1_score > team2_score:
                period_winner = "Team 1"
            elif team2_score > team1_score:
                period_winner = "Team 2"
            self.insert_score(self.match_id, self.period, team1_score, team2_score, period_winner)

        elif self.period == 2:
            self.period_2_final_label.show()
            self.period_2_final_number.show()
            self.period_2_final_colon.show()
            self.period_2_team1_final_score.setText(self.score_team1_all.text())
            self.period_2_team2_final_score.setText(self.score_team2_all.text())
            self.period_2_team1_final_score.show()
            self.period_2_team2_final_score.show()

            team1_score = self.score_team1_all.text()
            team2_score = self.score_team2_all.text()
            if team1_score > team2_score:
                period_winner = "Team 1"
            elif team2_score > team1_score:
                period_winner = "Team 2"
            self.insert_score(self.match_id, self.period, team1_score, team2_score, period_winner)

        elif self.period == 3:
            self.period_3_final_label.show()
            self.period_3_final_number.show()
            self.period_3_final_colon.show()
            self.period_3_team1_final_score.setText(self.score_team1_all.text())
            self.period_3_team2_final_score.setText(self.score_team2_all.text())
            self.period_3_team1_final_score.show()
            self.period_3_team2_final_score.show()

            team1_score = self.score_team1_all.text()
            team2_score = self.score_team2_all.text()
            if team1_score > team2_score:
                period_winner = "Team 1"
            elif team2_score > team1_score:
                period_winner = "Team 2"
            self.insert_score(self.match_id, self.period, team1_score, team2_score, period_winner)

        elif self.period == 4:
            self.period_4_final_label.show()
            self.period_4_final_number.show()
            self.period_4_final_colon.show()
            self.period_4_team1_final_score.setText(self.score_team1_all.text())
            self.period_4_team2_final_score.setText(self.score_team2_all.text())
            self.period_4_team1_final_score.show()
            self.period_4_team2_final_score.show()

            team1_score = self.score_team1_all.text()
            team2_score = self.score_team2_all.text()
            if team1_score > team2_score:
                period_winner = "Team 1"
            elif team2_score > team1_score:
                period_winner = "Team 2"
            elif team2_score == team1_score:
                period_winner = "Draw"
            self.insert_score(self.match_id, self.period, team1_score, team2_score, period_winner)

        team1_score = int(self.score_team1.text())
        team2_score = int(self.score_team2.text())
        if team1_score > team2_score:
            winner = "Team 1"
            if self.period == 1:
                self.period_1_team1_final_score.setStyleSheet('''QLabel#period_1_team1_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
            elif self.period == 2:
                self.period_2_team1_final_score.setStyleSheet('''QLabel#period_2_team1_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
            elif self.period == 3:
                self.period_3_team1_final_score.setStyleSheet('''QLabel#period_3_team1_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
            elif self.period == 4:
                self.period_4_team1_final_score.setStyleSheet('''QLabel#period_4_team1_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
        elif team2_score > team1_score:
            winner = "Team 2"
            if self.period == 1:
                self.period_1_team2_final_score.setStyleSheet('''QLabel#period_1_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
            elif self.period == 2:
                self.period_2_team2_final_score.setStyleSheet('''QLabel#period_2_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
            elif self.period == 3:
                self.period_3_team2_final_score.setStyleSheet('''QLabel#period_3_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
            elif self.period == 4:
                self.period_4_team2_final_score.setStyleSheet('''QLabel#period_4_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
        else:
            winner = "Draw"
            if self.period == 1:
                self.period_1_team1_final_score.setStyleSheet('''QLabel#period_1_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
                self.period_1_team2_final_score.setStyleSheet('''QLabel#period_1_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
            elif self.period == 2:
                self.period_2_team1_final_score.setStyleSheet('''QLabel#period_2_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
                self.period_2_team2_final_score.setStyleSheet('''QLabel#period_2_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
            elif self.period == 3:
                self.period_3_team1_final_score.setStyleSheet('''QLabel#period_3_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
                self.period_3_team2_final_score.setStyleSheet('''QLabel#period_3_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
            elif self.period == 4:
                self.period_4_team1_final_score.setStyleSheet('''QLabel#period_4_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')
                self.period_4_team2_final_score.setStyleSheet('''QLabel#period_4_team2_final_score{
                    background: transparent;
                    color: #00d527;
                    font-family: DS-Digital;
                    font-weight: 780;
                    font-size: 40px;
                }''')

        self.period_winners.append(winner)

        print(f"Period {self.period} Winner: {winner}")
        print(f"Period Winners: {self.period_winners}")

    # def load_player_numbers(self, username, team1_info, team2_info):
    #     self.cursor.execute('SELECT team_id FROM teams WHERE username = ?', (username,))
    #     teams = self.cursor.fetchall()

    #     if len(teams) < 2:
    #         QMessageBox.warning(self, "Error", "Not enough teams found for this username.")
    #         return

    #     team1_id, team2_id = teams[0][0], teams[1][0]
    #     self.team1_id, self.team2_id = team1_id, team2_id

    #     self.cursor.execute('SELECT player_number FROM players WHERE team_id = ?', (team1_id,))
    #     team1_players = [player[0] for player in self.cursor.fetchall()]

    #     self.cursor.execute('SELECT player_number FROM players WHERE team_id = ?', (team2_id,))
    #     team2_players = [player[0] for player in self.cursor.fetchall()]

    #     print(f"Team 1 Players: {team1_players}")
    #     print(f"Team 2 Players: {team2_players}")

    #     self.starting_players_team1 = team1_players[:5]
    #     self.starting_players_team2 = team2_players[:5]

    #     self.reserve_players_team1 = team1_players[5:]
    #     self.reserve_players_team2 = team2_players[5:]

    #     print(f"Starting players for Team 1: {self.starting_players_team1}")
    #     print(f"Reserve players for Team 1: {self.reserve_players_team1}")
    #     print(f"Starting players for Team 2: {self.starting_players_team2}")
    #     print(f"Reserve players for Team 2: {self.reserve_players_team2}")

    #     self.team1_buttons = [
    #         self.player1_team1, self.player2_team1, self.player3_team1,
    #         self.player4_team1, self.player5_team1
    #     ]
    #     for button, player in zip(self.team1_buttons, self.starting_players_team1):
    #         button.setText(str(player))

    #     self.reserve_buttons_team1 = [
    #         self.player6_team1, self.player7_team1, self.player8_team1,
    #         self.player9_team1, self.player10_team1, self.player11_team1, self.player12_team1
    #     ]
    #     for button, player in zip(self.reserve_buttons_team1, self.reserve_players_team1):
    #         print(f"Setting button {button.objectName()} to player {player}")
    #         button.setText(str(player))

    #     self.team2_buttons = [
    #         self.player1_team2, self.player2_team2, self.player3_team2,
    #         self.player4_team2, self.player5_team2
    #     ]
    #     for button, player in zip(self.team2_buttons, self.starting_players_team2):
    #         button.setText(str(player))

    #     self.reserve_buttons_team2 = [
    #         self.player6_team2, self.player7_team2, self.player8_team2,
    #         self.player9_team2, self.player10_team2, self.player11_team2, self.player12_team2
    #     ]
    #     for button, player in zip(self.reserve_buttons_team2, self.reserve_players_team2):
    #         print(f"Setting button {button.objectName()} to player {player}")
    #         button.setText(str(player))

    #     self.update_foul_labels()


def load_player_numbers(self, team1_info: dict, team2_info: dict):
    # 1) เก็บ team_id
    self.team1_id = team1_info['team1_id']
    self.team2_id = team2_info['team2_id']

    # 2) ตั้งชื่อทีมให้ label ในหน้า competition (เปลี่ยนชื่อ widget ให้ตรงของจริง)
    if hasattr(self, 'team1_name_label'):
        self.team1_name_label.setText(str(team1_info.get('team1_name', '')))
    if hasattr(self, 'team2_name_label'):
        self.team2_name_label.setText(str(team2_info.get('team2_name', '')))

    # 3) ดึงรายชื่อเบอร์ทั้งหมดของแต่ละทีมจาก DB (ไว้ทำสำรอง/ตัวสำรอง)
    def fetch_all_numbers(team_id: int):
        self.cursor.execute('SELECT player_number FROM players WHERE team_id = ?', (team_id,))
        return [str(r[0]) for r in self.cursor.fetchall()]

    all_t1 = fetch_all_numbers(self.team1_id)
    all_t2 = fetch_all_numbers(self.team2_id)

    # 4) ตัวจริง 5 คนให้ “ใช้ค่าที่ส่งมา” ก่อน ถ้าไม่ครบ 5 ให้เติมจาก DB
    starters_t1_from_info = [
        str(team1_info.get(f'team1_player{i}', '')).strip() for i in range(1, 6)
    ]
    starters_t2_from_info = [
        str(team2_info.get(f'team2_player{i}', '')).strip() for i in range(1, 6)
    ]

    def build_starters(all_numbers: list[str], starters_from_info: list[str]) -> list[str]:
        chosen = [n for n in starters_from_info if n and n != '0']
        # เติมให้ครบ 5 จากเบอร์ที่เหลือในทีม
        for n in all_numbers:
            if len(chosen) == 5:
                break
            if n not in chosen:
                chosen.append(n)
        # ถ้ายังไม่ครบ (ทีมมีผู้เล่นน้อย) ให้เติมช่องว่าง
        while len(chosen) < 5:
            chosen.append('')
        return chosen[:5]

    starters_t1 = build_starters(all_t1, starters_t1_from_info)
    starters_t2 = build_starters(all_t2, starters_t2_from_info)

    # 5) ตัวสำรอง = ทั้งทีมลบตัวจริง (คงลำดับจาก DB)
    reserves_t1 = [n for n in all_t1 if n not in set(starters_t1)]
    reserves_t2 = [n for n in all_t2 if n not in set(starters_t2)]

    self.starting_players_team1 = starters_t1
    self.starting_players_team2 = starters_t2
    self.reserve_players_team1 = reserves_t1
    self.reserve_players_team2 = reserves_t2

    # 6) ตั้งค่าปุ่มตัวจริงทีม 1
    team1_starter_buttons = [
        self.player1_team1, self.player2_team1, self.player3_team1,
        self.player4_team1, self.player5_team1
    ]
    for btn, num in zip(team1_starter_buttons, starters_t1):
        btn.setText(str(num))

    # ปุ่มตัวสำรองทีม 1
    team1_reserve_buttons = [
        self.player6_team1, self.player7_team1, self.player8_team1,
        self.player9_team1, self.player10_team1, self.player11_team1, self.player12_team1
    ]
    for btn, num in zip(team1_reserve_buttons, reserves_t1):
        btn.setText(str(num))
    for btn in team1_reserve_buttons[len(reserves_t1):]:
        btn.setText('')  # เคลียร์ถ้าไม่มีผู้เล่นพอ

    # 7) ตั้งค่าปุ่มตัวจริงทีม 2
    team2_starter_buttons = [
        self.player1_team2, self.player2_team2, self.player3_team2,
        self.player4_team2, self.player5_team2
    ]
    for btn, num in zip(team2_starter_buttons, starters_t2):
        btn.setText(str(num))

    # ปุ่มตัวสำรองทีม 2
    team2_reserve_buttons = [
        self.player6_team2, self.player7_team2, self.player8_team2,
        self.player9_team2, self.player10_team2, self.player11_team2, self.player12_team2
    ]
    for btn, num in zip(team2_reserve_buttons, reserves_t2):
        btn.setText(str(num))
    for btn in team2_reserve_buttons[len(reserves_t2):]:
        btn.setText('')

    # 8) อัปเดตฟาวล์หรือส่วนอื่น ๆ ต่อ
    self.update_foul_labels()



    def check_player_click(self, player_name):
        if self.foul_mode_active:
            if self.selected_foul_team == "team1" and player_name in [
                "player1_team1", "player2_team1", "player3_team1", "player4_team1", "player5_team1"
            ]:
                self.record_foul("team1", player_name)
            elif self.selected_foul_team == "team2" and player_name in [
                "player1_team2", "player2_team2", "player3_team2", "player4_team2", "player5_team2"
            ]:
                self.record_foul("team2", player_name)
            else:
                print(f"Invalid player selection for {self.selected_foul_team}.")
        elif self.sub_mode_active:
            button = self.findChild(QPushButton, player_name)
            if not button:
                return

            if player_name in ["player1_team1", "player2_team1", "player3_team1", "player4_team1", "player5_team1"]:
                if self.selected_player_out is None:
                    self.selected_player_out = player_name
                    print(f"{player_name} selected as OUT player for Team 1.")
                    self.team1_in_game.setText(button.text())
                    self.team1_in_game.show()
            elif player_name in ["player6_team1", "player7_team1", "player8_team1", "player9_team1", "player10_team1", "player11_team1", "player12_team1"]:
                if self.selected_player_in is None:
                    self.selected_player_in = player_name
                    print(f"{player_name} selected as IN player for Team 1.")
                    self.team1_out_game.setText(button.text())
                    self.team1_out_game.show()
            elif player_name in ["player1_team2", "player2_team2", "player3_team2", "player4_team2", "player5_team2"]:
                if self.selected_player_out is None:
                    self.selected_player_out = player_name
                    print(f"{player_name} selected as OUT player for Team 2.")
                    self.team2_in_game.setText(button.text())
                    self.team2_in_game.show()
            elif player_name in ["player6_team2", "player7_team2", "player8_team2", "player9_team2", "player10_team2", "player11_team2", "player12_team2"]:
                if self.selected_player_in is None:
                    self.selected_player_in = player_name
                    print(f"{player_name} selected as IN player for Team 2.")
                    self.team2_out_game.setText(button.text())
                    self.team2_out_game.show()


            if self.selected_player_in and self.selected_player_out:
                print(f"Substitution complete: IN -> {self.selected_player_in}, OUT -> {self.selected_player_out}")
                self.swap_player_numbers()
                self.exit_sub_mode()
                # self.insert_substitution(self.match_id, self.team_id, self.selected_player_out, self.selected_player_in, )
        else:
            print(f"{player_name} clicked outside of sub_mode.")

    def sub_mode(self, team):
        if self.sub_mode_active:
            self.exit_sub_mode()
            self.team1_exchange_icon.hide()
            self.team2_exchange_icon.hide()
            self.team1_mode.setText("Pause")
            self.team1_mode.setStyleSheet('''QLabel#team1_mode{
                background: transparent;
                color: black;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
            self.team2_mode.setText("Pause")
            self.team2_mode.setStyleSheet('''QLabel#team2_mode{
                background: transparent;
                color: black;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        else:
            self.sub_mode_active = True
            self.selected_player_in = None
            self.selected_player_out = None
            if team == "team1":
                self.sub_mode_active = True
                self.selected_player_in = None
                self.selected_player_out = None
                self.team1_mode.setText("Sub")
                self.team1_mode.setStyleSheet('''QLabel#team1_mode{
                    background: transparent;
                    color: #ff2525;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                self.sub_team1_button.setStyleSheet('''QPushButton#sub_team1_button{
                        background: #ff2525;
                        color: #ffffff;
                        border: none;
                        border-radius: 10px;
                        font-family: Saira Condensed;
                        font-weight: 780;
                        font-size: 20px;
                }''')
                self.timer.stop()
                self.timer_running = False
                self.timer_button.set_play_icon()

                self.player6_team1.show()
                self.player7_team1.show()
                self.player8_team1.show()
                self.player9_team1.show()
                self.player10_team1.show()
                self.player11_team1.show()
                self.player12_team1.show()

                self.team1_exchange_icon.show()

            elif team == "team2":
                self.sub_mode_active = True
                self.selected_player_in = None
                self.selected_player_out = None
                self.team2_mode.setText("Sub")
                self.team2_mode.setStyleSheet('''QLabel#team2_mode{
                    background: transparent;
                    color: #ff2525;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                self.sub_team2_button.setStyleSheet('''
                    QPushButton#sub_team2_button{
                        background: #ff2525;
                        color: #ffffff;
                        border: none;
                        border-radius: 10px;
                        font-family: Saira Condensed;
                        font-weight: 780;
                        font-size: 20px;
                    }
                ''')
                self.timer.stop()
                self.timer_running = False
                self.timer_button.set_play_icon()

                self.player6_team2.show()
                self.player7_team2.show()
                self.player8_team2.show()
                self.player9_team2.show()
                self.player10_team2.show()
                self.player11_team2.show()
                self.player12_team2.show()

                self.team2_exchange_icon.show()

    def exit_sub_mode(self):
        self.sub_mode_active = False
        self.team1_mode.setText("")

        self.team2_mode.setText("")

        self.player6_team1.hide()
        self.player7_team1.hide()
        self.player8_team1.hide()
        self.player9_team1.hide()
        self.player10_team1.hide()
        self.player11_team1.hide()
        self.player12_team1.hide()
        self.player6_team2.hide()
        self.player7_team2.hide()
        self.player8_team2.hide()
        self.player9_team2.hide()
        self.player10_team2.hide()
        self.player11_team2.hide()
        self.player12_team2.hide()

        self.sub_team1_button.setStyleSheet('''
            QPushButton#sub_team1_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#sub_team1_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.sub_team2_button.setStyleSheet('''
            QPushButton#sub_team2_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#sub_team2_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

    def swap_player_numbers(self):
        if self.selected_player_in and self.selected_player_out:
            button_in = self.findChild(QPushButton, self.selected_player_in)
            button_out = self.findChild(QPushButton, self.selected_player_out)

            if button_in and button_out:
                button_in_text = button_in.text()
                button_out_text = button_out.text()

                button_in.setText(button_out_text)
                button_out.setText(button_in_text)

                minutes, seconds = self.format_time(self.current_time)
                time_str = f"{minutes:02d}:{seconds:02d}"

                if "team1" in self.selected_player_in or "team1" in self.selected_player_out:
                    self.substitution_history_team1.append({
                        "period": self.period,
                        "time": time_str,
                        "out": button_out_text,
                        "in": button_in_text
                    })
                elif "team2" in self.selected_player_in or "team2" in self.selected_player_out:
                    self.substitution_history_team2.append({
                        "period": self.period,
                        "time": time_str,
                        "out": button_out_text,
                        "in": button_in_text
                    })
                if "team1" in self.selected_player_in or "team1" in self.selected_player_out:
                    team_id = self.team1_id
                elif "team2" in self.selected_player_in or "team2" in self.selected_player_out:
                    team_id = self.team2_id

                print(f"Swapped numbers: {self.selected_player_in} -> {button_in_text}, {self.selected_player_out} -> {button_out_text}")
                print(f"Team 1 Substitution History: {self.substitution_history_team1}")
                print(f"Team 2 Substitution History: {self.substitution_history_team2}")
                self.insert_substitution(self.match_id, team_id, self.selected_player_out, self.selected_player_in, time_str)
                self.update_foul_labels()

    def timeout(self, team):
        minutes, seconds = self.format_time(self.current_time)
        time_str = f"{minutes:02d}:{seconds:02d}"
        if team == "team1":
            team_id = self.team1_id
            self.insert_timeout(self.match_id, team_id, time_str)
        elif team == "team2":
            team_id = self.team2_id
            self.insert_timeout(self.match_id, team_id, time_str)

        if self.period <= 3:
            max_timeouts = 2
        else:
            max_timeouts = 3

        if team == "team1":
            current_timeouts = int(self.timeout_team1_count.text().split('/')[0])
            if current_timeouts < max_timeouts:
                self.team1_mode.setText("Timeout")
                self.team1_mode.setStyleSheet('''QLabel#team1_mode{
                    background: transparent;
                    color: #ff2525;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                self.team2_mode.setText("Timeout")
                self.team2_mode.setStyleSheet('''QLabel#team2_mode{
                    background: transparent;
                    color: #ff2525;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                self.timer.stop()
                self.timer_button.set_play_icon()
                self.timer_button.setEnabled(True)
                self.timeout_team1_count.hide()
                self.timeout_team1_label.show()

                self.sub_team1_button.setEnabled(True)
                self.sub_team2_button.setEnabled(True)

                self.timeout_team1_remaining = int(self.timeout_team1_label.text())
                self.timeout_team1_before = self.timeout_team1_remaining
                self.timeout_team1_timer = QTimer(self)
                self.timeout_team1_timer.timeout.connect(lambda: self.update_timeout("team1"))
                self.timeout_team1_timer.start(1000)
                self.timeout_team2_button.setEnabled(False)
                self.timeout_team1_button.setStyleSheet('''
                    QPushButton#timeout_team1_button{
                        background: #ff2525;
                        color: #ffffff;
                        border: none;
                        border-radius: 10px;
                        font-family: Saira Condensed;
                        font-weight: 780;
                        font-size: 20px;
                    }''')

                current_timeouts += 1
                self.timeout_team1_count.setText(f"{current_timeouts}/{max_timeouts}")
            else:
                QMessageBox.warning(self, "Timeout", f"Team 1 has already used all {max_timeouts} timeouts for this period.")

        elif team == "team2":
            current_timeouts = int(self.timeout_team2_count.text().split('/')[0])
            if current_timeouts < max_timeouts:
                self.team1_mode.setText("Timeout")
                self.team1_mode.setStyleSheet('''QLabel#team1_mode{
                    background: transparent;
                    color: #ff2525;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                self.team2_mode.setText("Timeout")
                self.team2_mode.setStyleSheet('''QLabel#team2_mode{
                    background: transparent;
                    color: #ff2525;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                self.timer.stop()
                self.timer_button.set_play_icon()
                self.timer_button.setEnabled(True)
                self.timeout_team2_count.hide()
                self.timeout_team2_label.show()

                self.sub_team1_button.setEnabled(True)
                self.sub_team2_button.setEnabled(True)

                self.timeout_team2_remaining = int(self.timeout_team2_label.text())
                self.timeout_team2_before = self.timeout_team2_remaining
                self.timeout_team2_timer = QTimer(self)
                self.timeout_team2_timer.timeout.connect(lambda: self.update_timeout("team2"))
                self.timeout_team2_timer.start(1000)
                self.timeout_team1_button.setEnabled(False)
                self.timeout_team2_button.setStyleSheet('''
                    QPushButton#timeout_team2_button{
                        background: #ff2525;
                        color: #ffffff;
                        border: none;
                        border-radius: 10px;
                        font-family: Saira Condensed;
                        font-weight: 780;
                        font-size: 20px;
                    }''')

                current_timeouts += 1
                self.timeout_team2_count.setText(f"{current_timeouts}/{max_timeouts}")
            else:
                QMessageBox.warning(self, "Timeout", f"Team 2 has already used all {max_timeouts} timeouts for this period.")

    def change_period(self):
        if self.period < 4:
            self.show_period_summary()  # แสดงข้อมูลของ period ที่จบลง
            self.period += 1
            self.period_number.setText(str(self.period))

            self.reset_values()
            self.timer_button.set_play_icon()
        else:
            self.show_period_summary()
            self.calculate_final_winner()
            QMessageBox.information(self, "Game Over", "The game has ended.")
            self.timer_button.set_play_icon()

    def update_timeout(self, team):
        if team == "team1":
            if self.timeout_team1_remaining > 0:
                self.timeout_team1_remaining -= 1
                self.timeout_team1_label.setText(str(self.timeout_team1_remaining))
                self.timer_button.setEnabled(False)
            else:
                self.timeout_team1_timer.stop()
                self.timer_running = False
                self.timeout_team1_label.hide()
                self.timeout_team1_count.show()
                self.timeout_team1_label.setText(str(self.timeout_team1_before))
                self.timeout_team1_button.setStyleSheet('''
                    QPushButton#timeout_team1_button{
                        background: #ffffff;
                        color: black;
                        border: none;
                        border-radius: 10px;
                        font-family: Saira Condensed;
                        font-weight: 780;
                        font-size: 20px;
                    }
                    QPushButton#timeout_team1_button:hover{
                        background: #b2b2b2;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-family: Saira Condensed;
                        font-weight: 780;
                        font-size: 20px;
                    }''')
                self.team1_mode.setText("Pause")
                self.team1_mode.setStyleSheet('''QLabel#team1_mode{
                    background: transparent;
                    color: black;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                self.team2_mode.setText("Pause")
                self.team2_mode.setStyleSheet('''QLabel#team2_mode{
                    background: transparent;
                    color: black;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                QMessageBox.information(self, "Timeout", "Team 1 timeout has ended.")
                self.timeout_team2_button.setEnabled(True)

                self.timer_button.setEnabled(True)
                self.sub_team1_button.setEnabled(True)
                self.sub_team2_button.setEnabled(True)


        elif team == "team2":
            if self.timeout_team2_remaining > 0:
                self.timeout_team2_remaining -= 1
                self.timeout_team2_label.setText(str(self.timeout_team2_remaining))
                self.timer_button.setEnabled(False)
            else:
                self.timeout_team2_timer.stop()
                self.timer_running = False
                self.timeout_team2_label.hide()
                self.timeout_team2_count.show()
                self.timeout_team2_label.setText(str(self.timeout_team2_before))
                self.timeout_team2_button.setStyleSheet('''
                    QPushButton#timeout_team2_button{
                        background: #ffffff;
                        color: black;
                        border: none;
                        border-radius: 10px;
                        font-family: Saira Condensed;
                        font-weight: 780;
                        font-size: 20px;
                    }
                    QPushButton#timeout_team2_button:hover{
                        background: #b2b2b2;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-family: Saira Condensed;
                        font-weight: 780;
                        font-size: 20px;
                    }''')
                self.team1_mode.setText("Pause")
                self.team1_mode.setStyleSheet('''QLabel#team1_mode{
                    background: transparent;
                    color: black;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                self.team2_mode.setText("Pause")
                self.team2_mode.setStyleSheet('''QLabel#team2_mode{
                    background: transparent;
                    color: black;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                QMessageBox.information(self, "Timeout", "Team 2 timeout has ended.")
                self.timeout_team1_button.setEnabled(True)

                self.timer_button.setEnabled(True)
                self.sub_team1_button.setEnabled(True)
                self.sub_team2_button.setEnabled(True)

    def increment_score(self, team, points):
        if team == "team1":
            self.total_score_team1 += points
            self.score_team1.setText(str(self.total_score_team1))
            self.score_team1_all.setText(str(self.total_score_team1))
        elif team == "team2":
            self.total_score_team2 += points
            self.score_team2.setText(str(self.total_score_team2))
            self.score_team2_all.setText(str(self.total_score_team2))

    def record_foul(self, team, player_name):
        player_number = self.findChild(QPushButton, player_name).text()
        if team == "team1":
            if player_number not in self.foul_history_team1:
                self.foul_history_team1[player_number] = 0
            self.foul_history_team1[player_number] += 1
            current_foul = int(self.foul_team1_number.text())
            self.foul_team1_number.setText(str(current_foul + 1))
            if current_foul + 1 > 4:
                self.foul_team1_number.setStyleSheet('''
                    font-size: 70px;
                    font-weight: bold;
                    font-family: DS-Digital;
                    color: #ff2525;
                ''')
        elif team == "team2":
            if player_number not in self.foul_history_team2:
                self.foul_history_team2[player_number] = 0
            self.foul_history_team2[player_number] += 1
            current_foul = int(self.foul_team2_number.text())
            self.foul_team2_number.setText(str(current_foul + 1))
            if current_foul + 1 > 4:
                self.foul_team2_number.setStyleSheet('''
                    font-size: 70px;
                    font-weight: bold;
                    font-family: DS-Digital;
                    color: #ff2525;
                ''')

        self.foul_mode_active = False
        self.foul_team1_button.setStyleSheet('''
            QPushButton#foul_team1_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#foul_team1_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.foul_team2_button.setStyleSheet('''
            QPushButton#foul_team2_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#foul_team2_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.team1_mode.setText("Pause")
        self.team1_mode.setStyleSheet('''QLabel#team1_mode{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.team2_mode.setText("Pause")
        self.team2_mode.setStyleSheet('''QLabel#team2_mode{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 20px;
        }''')
        self.selected_foul_team = None
        print(f"Foul recorded: {team} - Player {player_number}")
        print(f"Team 1 Foul History: {self.foul_history_team1}")
        print(f"Team 2 Foul History: {self.foul_history_team2}")
        minutes, seconds = self.format_time(self.current_time)
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.insert_foul(self.match_id, team, player_number, time_str)
        self.update_foul_labels()

    def increment_foul(self, team):
        if self.foul_mode_active:
            self.foul_mode_active = False
            self.selected_foul_team = None
            self.team1_mode.setText("Pause")
            self.team1_mode.setStyleSheet('''QLabel#team1_mode{
                background: transparent;
                color: black;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
            self.team2_mode.setText("Pause")
            self.team2_mode.setStyleSheet('''QLabel#team2_mode{
                background: transparent;
                color: black;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
            self.foul_team1_button.setStyleSheet('''
                QPushButton#foul_team1_button{
                    background: #ffffff;
                    color: black;
                    border: none;
                    border-radius: 10px;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }
                QPushButton#foul_team1_button:hover{
                    background: #b2b2b2;
                    color: white;
                    border: none;
                    border-radius: 10px;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
            self.foul_team2_button.setStyleSheet('''
                QPushButton#foul_team2_button{
                    background: #ffffff;
                    color: black;
                    border: none;
                    border-radius: 10px;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }
                QPushButton#foul_team2_button:hover{
                    background: #b2b2b2;
                    color: white;
                    border: none;
                    border-radius: 10px;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
            print("Foul mode deactivated.")

        else:
            self.foul_mode_active = True
            self.selected_foul_team = team
            if team == "team1":
                self.team1_mode.setText("Foul")
                self.team1_mode.setStyleSheet('''QLabel#team1_mode{
                    background: transparent;
                    color: #0023e8;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                self.foul_team1_button.setStyleSheet('''
                    QPushButton#foul_team1_button{
                        background: #0023e8;
                        color: #ffffff;
                        border: none;
                        border-radius: 10px;
                        font-family: Saira Condensed;
                        font-weight: 780;
                        font-size: 20px;
                    }''')
            elif team == "team2":
                self.team2_mode.setText("Foul")
                self.team2_mode.setStyleSheet('''QLabel#team2_mode{
                    background: transparent;
                    color: #0023e8;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
                self.foul_team2_button.setStyleSheet('''
                    QPushButton#foul_team2_button{
                        background: #0023e8;
                        color: #ffffff;
                        border: none;
                        border-radius: 10px;
                        font-family: Saira Condensed;
                        font-weight: 780;
                        font-size: 20px;
                    }''')
            print(f"Foul mode activated for {team}. Please select a player.")

    def reset_values(self):
        self.current_time = 1 * 20
        self.time_minute.setText("00")
        self.time_second.setText("20")

        self.score_team1.setText("0")
        self.score_team2.setText("0")

        self.foul_team1_number.setText("0")
        self.foul_team2_number.setText("0")

        self.foul_team1_number.setStyleSheet('''
                        font-size: 70px;
                        font-weight: bold;
                        font-family: DS-Digital;
                        color: #0023e8;
                        ''')

        self.foul_team2_number.setStyleSheet('''
                        font-size: 70px;
                        font-weight: bold;
                        font-family: DS-Digital;
                        color: #0023e8;
                        ''')

        self.sub_team1_button.setStyleSheet('''
            QPushButton#sub_team1_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#sub_team1_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')
        self.sub_team2_button.setStyleSheet('''
            QPushButton#sub_team2_button{
                background: #ffffff;
                color: black;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }
            QPushButton#sub_team2_button:hover{
                background: #b2b2b2;
                color: white;
                border: none;
                border-radius: 10px;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 20px;
            }''')

        self.team1_mode.setText('')
        self.team2_mode.setText('')

        if self.period <= 3:
            self.timeout_team1_count.setText("0/2")
            self.timeout_team2_count.setText("0/2")
        else:
            self.timeout_team1_count.setText("0/3")
            self.timeout_team2_count.setText("0/3")

        self.timeout_team1_label.hide()
        self.timeout_team2_label.hide()
        self.timeout_team1_count.show()
        self.timeout_team2_count.show()

        self.stop_timer()

        self.timer_button.set_play_icon()

        print(f"Values for period {self.period} have been reset!")

        self.update_foul_labels()

    def timer_button_clicked(self):
        if self.period == 1:
            self.insert_match(self.username, self.team1_id, self.team2_id)
        status = self.timer_button.get_current_icon()
        if status == self.timer_button.play_icon:
            self.timer_button.set_stop_icon()
            self.start_timer()
            self.team1_in_game.hide()
            self.team1_out_game.hide()
            self.team1_exchange_icon.hide()
            self.team2_in_game.hide()
            self.team2_out_game.hide()
            self.team2_exchange_icon.hide()
            self.sub_team1_button.setEnabled(False)
            self.sub_team2_button.setEnabled(False)
            self.timer_running = True
            self.team1_mode.setText("Play")
            self.team1_mode.setStyleSheet('''QLabel#team1_mode{
                background: transparent;
                color: #00d527;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 22px;
            }''')
            self.team2_mode.setText("Play")
            self.team2_mode.setStyleSheet('''QLabel#team2_mode{
                background: transparent;
                color: #00d527;
                font-family: Saira Condensed;
                font-weight: 780;
                font-size: 22px;
            }''')
        else:
            self.timer_button.set_play_icon()
            self.stop_timer()
            self.team1_mode.setText("Pause")
            self.team1_mode.setStyleSheet('''QLabel#team1_mode{
                    background: transparent;
                    color: black;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
            self.team2_mode.setText("Pause")
            self.team2_mode.setStyleSheet('''QLabel#team2_mode{
                    background: transparent;
                    color: black;
                    font-family: Saira Condensed;
                    font-weight: 780;
                    font-size: 20px;
                }''')
            self.timer_running = False
            self.sub_team1_button.setEnabled(True)
            self.sub_team2_button.setEnabled(True)

    def start_timer(self):
        if not self.timer_running:
            self.timer.start(1000)
            self.timer_running = True

            self.sub_team1_button.setEnabled(False)
            self.sub_team2_button.setEnabled(False)

    def stop_timer(self):
        self.timer.stop()
        self.timer_running = False

    def update_timer(self):
        if self.current_time > 0:
            self.current_time -= 1
            minutes, seconds = self.format_time(self.current_time)

            self.time_minute.setText(f"{minutes:02d}")  # อัปเดตนาที
            self.time_second.setText(f"{seconds:02d}")  # อัปเดตวินาที
        else:
            self.timer.stop()
            self.timer_running = False
            QMessageBox.information(self, "Period Ended", f"Period {self.period} has ended.")
            self.change_period()

    @staticmethod
    def format_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return minutes, seconds

    def get_username(self,username,team1_info,team2_info):
        self.username = username
        self.load_player_numbers(team1_info,team2_info)

    # def set_initial_players(self, team1_info, team2_info):
    #     # ตั้งค่าผู้เล่นเริ่มต้น 5 คนของทีม 1
    #     team1_starting_players = [
    #         team1_info['team1_player1'],
    #         team1_info['team1_player2'],
    #         team1_info['team1_player3'],
    #         team1_info['team1_player4'],
    #         team1_info['team1_player5']
    #     ]
    #     self.starting_players_team1 = team1_starting_players

    #     # ตั้งค่าปุ่มผู้เล่นเริ่มต้น 5 คนแรกของทีม 1
    #     team1_buttons = [
    #         self.player1_team1, self.player2_team1, self.player3_team1,
    #         self.player4_team1, self.player5_team1
    #     ]
    #     for button, player_number in zip(team1_buttons, team1_starting_players):
    #         button.setText(player_number)

    #     # ตั้งค่าปุ่มตัวสำรอง 7 คนที่เหลือของทีม 1
    #     team1_reserve_players = [str(i) for i in range(1, 13) if str(i) not in team1_starting_players]
    #     reserve_buttons_team1 = [
    #         self.player6_team1, self.player7_team1, self.player8_team1,
    #         self.player9_team1, self.player10_team1, self.player11_team1, self.player12_team1
    #     ]
    #     for button, player_number in zip(reserve_buttons_team1, team1_reserve_players):
    #         button.setText(player_number)

    #     # ตั้งค่าผู้เล่นเริ่มต้น 5 คนของทีม 2
    #     team2_starting_players = [
    #         team2_info['team2_player1'],
    #         team2_info['team2_player2'],
    #         team2_info['team2_player3'],
    #         team2_info['team2_player4'],
    #         team2_info['team2_player5']
    #     ]
    #     self.starting_players_team2 = team2_starting_players

    #     # ตั้งค่าปุ่มผู้เล่นเริ่มต้น 5 คนแรกของทีม 2
    #     team2_buttons = [
    #         self.player1_team2, self.player2_team2, self.player3_team2,
    #         self.player4_team2, self.player5_team2
    #     ]
    #     for button, player_number in zip(team2_buttons, team2_starting_players):
    #         button.setText(player_number)

    #     # ตั้งค่าปุ่มตัวสำรอง 7 คนที่เหลือของทีม 2
    #     team2_reserve_players = [str(i) for i in range(1, 13) if str(i) not in team2_starting_players]
    #     reserve_buttons_team2 = [
    #         self.player6_team2, self.player7_team2, self.player8_team2,
    #         self.player9_team2, self.player10_team2, self.player11_team2, self.player12_team2
    #     ]
    #     for button, player_number in zip(reserve_buttons_team2, team2_reserve_players):
    #         button.setText(player_number)

    #     print(f"Team 1 Starting Players: {self.starting_players_team1}")
    #     print(f"Team 2 Starting Players: {self.starting_players_team2}")

    def set_initial_players(self, team1_info, team2_info):
        """
        ตั้งค่าผู้เล่นเริ่มต้น 5 คนแรกและตัวสำรอง 7 คนที่เหลือสำหรับทั้งสองทีม
        :param team1_info: ข้อมูลผู้เล่นของทีม 1 (dict)
        :param team2_info: ข้อมูลผู้เล่นของทีม 2 (dict)
        """
        # ตั้งค่าผู้เล่นเริ่มต้น 5 คนของทีม 1
        team1_starting_players = [
            team1_info['team1_player1'],
            team1_info['team1_player2'],
            team1_info['team1_player3'],
            team1_info['team1_player4'],
            team1_info['team1_player5']
        ]
        self.starting_players_team1 = team1_starting_players

        # ตั้งค่าปุ่มผู้เล่นเริ่มต้น 5 คนแรกของทีม 1
        team1_buttons = [
            self.player1_team1, self.player2_team1, self.player3_team1,
            self.player4_team1, self.player5_team1
        ]
        for button, player_number in zip(team1_buttons, team1_starting_players):
            button.setText(player_number)

        # ตั้งค่าปุ่มตัวสำรอง 7 คนที่เหลือของทีม 1
        team1_reserve_players = [
            player for player in team1_info['all_players'] if player not in team1_starting_players
        ]
        reserve_buttons_team1 = [
            self.player6_team1, self.player7_team1, self.player8_team1,
            self.player9_team1, self.player10_team1, self.player11_team1, self.player12_team1
        ]
        for button, player_number in zip(reserve_buttons_team1, team1_reserve_players):
            button.setText(player_number)

        # ตั้งค่าผู้เล่นเริ่มต้น 5 คนของทีม 2
        team2_starting_players = [
            team2_info['team2_player1'],
            team2_info['team2_player2'],
            team2_info['team2_player3'],
            team2_info['team2_player4'],
            team2_info['team2_player5']
        ]
        self.starting_players_team2 = team2_starting_players

        team2_buttons = [
            self.player1_team2, self.player2_team2, self.player3_team2,
            self.player4_team2, self.player5_team2
        ]
        for button, player_number in zip(team2_buttons, team2_starting_players):
            button.setText(player_number)

        team2_reserve_players = [
            player for player in team2_info['all_players'] if player not in team2_starting_players
        ]
        reserve_buttons_team2 = [
            self.player6_team2, self.player7_team2, self.player8_team2,
            self.player9_team2, self.player10_team2, self.player11_team2, self.player12_team2
        ]
        for button, player_number in zip(reserve_buttons_team2, team2_reserve_players):
            button.setText(player_number)

        print(f"Team 1 Starting Players: {self.starting_players_team1}")
        print(f"Team 1 Reserve Players: {team1_reserve_players}")
        print(f"Team 2 Starting Players: {self.starting_players_team2}")
        print(f"Team 2 Reserve Players: {team2_reserve_players}")

    def insert_match(self, username, team1_id, team2_id):
        print(f"\n\n\nUsername: {username}, Team 1 ID: {team1_id}, Team 2 ID: {team2_id}\n\n\n")
        match_id = max(team1_id, team2_id)  # ใช้ค่า team_id ที่มากที่สุดเป็น match_id
        match_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ตรวจสอบว่า match_id นี้มีอยู่ในฐานข้อมูลแล้วหรือยัง
        self.cursor.execute("SELECT match_id FROM matches WHERE match_id = ?", (match_id,))
        existing_match = self.cursor.fetchone()

        if existing_match:
            print(f"Error: Match ID {match_id} already exists!")
            return None  # หยุดการทำงาน ถ้ามี match_id นี้แล้ว

        # บันทึกแมทช์ลงฐานข้อมูล
        self.cursor.execute("""
            INSERT INTO matches (match_id, username, match_date, team1_id, team2_id)
            VALUES (?, ?, ?, ?, ?)""",
            (match_id, username, match_date, team1_id, team2_id)
        )

        self.connection.commit()
        self.match_id = match_id  # กำหนด match_id ให้กับแมทช์นี้
        print(f"Match started with ID: {self.match_id}")

        return match_id  # คืนค่า match_id ที่ถูกกำหนด

    def insert_substitution(self, match_id, team_id, player_out, player_in, time):
        period = self.period
        connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO substitutions (match_id, team_id, player_out, player_in, time, period)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (match_id, team_id, player_out, player_in, time, period)
        )

        connection.commit()
        connection.close()

    def insert_foul(self, match_id, team, player_id, time):
        period = self.period
        connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO fouls (match_id, team, player_id, time, period)
            VALUES (?, ?, ?, ?, ?)""",
            (match_id, team, player_id, time, period)
        )

        connection.commit()
        connection.close()

    def insert_timeout(self, match_id, team_id, time):
        period = self.period
        connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO timeouts (match_id, team_id, time, period)
            VALUES (?, ?, ?, ?)""",
            (match_id, team_id, time, period)
        )

        connection.commit()
        connection.close()

    def insert_score(self,match_id, period, team1_score, team2_score, period_winner):
        connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO scores (match_id, period, team1_score, team2_score, period_winner)
            VALUES (?, ?, ?, ?, ?)""",
            (match_id, period, team1_score, team2_score, period_winner)
        )

        connection.commit()
        connection.close()



#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    competition = Competition()
    competition.show()
    app.exec()
