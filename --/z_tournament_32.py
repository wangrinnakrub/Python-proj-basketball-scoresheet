from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sqlite3
import math


class tournament32(QMainWindow):
    switch_to_main_window = pyqtSignal()
    switch_to_create_team_from_tournament_32_ = pyqtSignal(str, int)
    switch_to_set_up_match_from_tournament_32 = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basketball Score Sheet - Tournament 32')
        self.showMaximized()
        self.import_style('style_tournament_32.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()
        self.created_teams = set()

        QTimer.singleShot(0, self.clear_initial_focus)
        self.installEventFilter(self)

        self.connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

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

    # *---------- layout ---------- #
    def ui(self):
        main_widget = QWidget()
        self.addWidgetsToLayout(main_widget)
        self.setCentralWidget(main_widget)

    # *---------- widget ---------- #
    def addWidgetsToLayout(self, parent):

        self.back_button = QPushButton(parent)
        self.back_button.setGeometry(15,10,40,40)
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_in')
        self.back_button.clicked.connect(self.switch_to_main_window.emit)
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


        # self.tournament_name_label = QLabel('Tournament Name', parent)
        self.tournament_name_label = QLabel('TOURNAMENT NAME', parent)
        self.tournament_name_label.setObjectName('tournament_name_label')
        self.tournament_name_label.setGeometry(570, 40, 400, 50)
        self.tournament_name_label.setStyleSheet('''QLabel#tournament_name_label{
            background: transparent;
            color: black;
            font-family: Saira Condensed;
            font-weight: 780;
            font-size: 40px;
        }''')
        self.tournament_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tournament_name_input_box = QLineEdit(parent)
        self.tournament_name_input_box.setPlaceholderText('Type your tournament name')
        self.tournament_name_input_box.setObjectName('tournament_name_input_box')
        self.tournament_name_input_box.setGeometry(670, 100, 200, 40)
        self.tournament_name_input_box.setStyleSheet('''
            QLineEdit#tournament_name_input_box{

                padding-left: 18px;
                color: #767676;
                background: transparent;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #dcdcdc;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }
            QLineEdit#tournament_name_input_box:hover,QLineEdit#tournament_name_input_box:focus:hover{

                padding-left: 18px;
                background: transparent;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #ff56c7 !important;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }

            QLineEdit#tournament_name_input_box:focus{

                border-color: #2a2a2a;

            }

            QLineEdit#tournament_name_input_box::placeholder{

                padding-left: 18px;
                color: #dedede;
                background: transparent;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
              team1_add_player_button  border-left: transparent;
                border-right: transparent;
                border-color: #dcdcdc;
                font-family: TeX Gyre Adventor;
                font-weight: 620;
            }''')
        self.tournament_name_input_box.textChanged.connect(self.tournament_name_input_box_check_none)

        # self.tournament_name_error_label = QLabel('Please enter tournament name',parent)
        self.tournament_name_error_label = QLabel('',parent)
        self.tournament_name_error_label.setObjectName('tournament_name_error_label')
        self.tournament_name_error_label.setGeometry(693, 140, 170, 30)
        self.tournament_name_error_label.setStyleSheet('''
            QLabel#tournament_name_error_label{
                background: transparent;
                color: #ff4343;
            }''')

        self.trophy = QPushButton(parent)
        self.trophy.setGeometry(644, 295, 250, 250)
        self.trophy.setIcon(QIcon(r'C:\pic\trophy.png'))
        self.trophy.setIconSize(QSize(200,200))
        self.trophy.setObjectName('trophy')
        self.trophy.setStyleSheet('''
            QPushButton#trophy{
                background: transparent;
                }''')

        # * ------------------- create team button ------------------- * #
        self.create_team1_button = QPushButton('', parent)
        self.create_team1_button.setObjectName('create_team1_button')
        self.create_team1_button.setGeometry(47, 97, 95, 26)
        self.create_team1_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
            }
                    QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }


        ''')
        self.create_team1_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team1_button.setIconSize(QSize(16,16))
        self.create_team1_button.clicked.connect(lambda: self.handle_create_team_button(1))

        self.create_team1_side_button = QPushButton('', parent)
        self.create_team1_side_button.setGeometry(42, 97, 7, 26)
        self.create_team1_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team2_button = QPushButton('', parent)
        self.create_team2_button.setObjectName('create_team2_button')
        self.create_team2_button.setGeometry(47, 134, 95, 26)
        self.create_team2_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team2_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team2_button.setIconSize(QSize(16,16))
        self.create_team2_button.clicked.connect(lambda: self.handle_create_team_button(2))

        self.create_team2_side_button = QPushButton('', parent)
        self.create_team2_side_button.setGeometry(42, 134, 7, 26)
        self.create_team2_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')


        self.create_team3_button = QPushButton('', parent)
        self.create_team3_button.setObjectName('create_team3_button')
        self.create_team3_button.setGeometry(47, 180, 95, 26)
        self.create_team3_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team3_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team3_button.setIconSize(QSize(16,16))
        self.create_team3_button.clicked.connect(lambda: self.handle_create_team_button(3))

        self.create_team3_side_button = QPushButton('', parent)
        self.create_team3_side_button.setGeometry(42, 180, 7, 26)
        self.create_team3_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team4_button = QPushButton('', parent)
        self.create_team4_button.setObjectName('create_team4_button')
        self.create_team4_button.setGeometry(47, 219, 95, 26)
        self.create_team4_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team4_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team4_button.setIconSize(QSize(16,16))
        self.create_team4_button.clicked.connect(lambda: self.handle_create_team_button(4))

        self.create_team4_side_button = QPushButton('', parent)
        self.create_team4_side_button.setGeometry(42, 219, 7, 26)
        self.create_team4_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team5_button = QPushButton('', parent)
        self.create_team5_button.setObjectName('create_team5_button')
        self.create_team5_button.setGeometry(47, 265, 95, 26)
        self.create_team5_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team5_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team5_button.setIconSize(QSize(16,16))
        self.create_team5_button.clicked.connect(lambda: self.handle_create_team_button(5))

        self.create_team5_side_button = QPushButton('', parent)
        self.create_team5_side_button.setGeometry(42, 265, 7, 26)
        self.create_team5_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team6_button = QPushButton('', parent)
        self.create_team6_button.setObjectName('create_team6_button')
        self.create_team6_button.setGeometry(47, 303, 95, 26)
        self.create_team6_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team6_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team6_button.setIconSize(QSize(16,16))
        self.create_team6_button.clicked.connect(lambda: self.handle_create_team_button(6))

        self.create_team6_side_button = QPushButton('', parent)
        self.create_team6_side_button.setGeometry(42, 303, 7, 26)
        self.create_team6_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team7_button = QPushButton('', parent)
        self.create_team7_button.setObjectName('create_team7_button')
        self.create_team7_button.setGeometry(47, 349, 95, 26)
        self.create_team7_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team7_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team7_button.setIconSize(QSize(16,16))
        self.create_team7_button.clicked.connect(lambda: self.handle_create_team_button(7))

        self.create_team7_side_button = QPushButton('', parent)
        self.create_team7_side_button.setGeometry(42, 349, 7, 26)
        self.create_team7_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team8_button = QPushButton('', parent)
        self.create_team8_button.setObjectName('create_team8_button')
        self.create_team8_button.setGeometry(47, 388, 95, 26)
        self.create_team8_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team8_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team8_button.setIconSize(QSize(16,16))
        self.create_team8_button.clicked.connect(lambda: self.handle_create_team_button(8))

        self.create_team8_side_button = QPushButton('', parent)
        self.create_team8_side_button.setGeometry(42, 388, 7, 26)
        self.create_team8_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        # *---------------------------------------------------------------* #


        self.create_team9_button = QPushButton('', parent)
        self.create_team9_button.setObjectName('create_team9_button')
        self.create_team9_button.setGeometry(47, 470, 95, 26)
        self.create_team9_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team9_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team9_button.setIconSize(QSize(16,16))
        self.create_team9_button.clicked.connect(lambda: self.handle_create_team_button(9))

        self.create_team9_side_button = QPushButton('', parent)
        self.create_team9_side_button.setGeometry(42, 470, 7, 26)
        self.create_team9_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team10_button = QPushButton('', parent)
        self.create_team10_button.setObjectName('create_team10_button')
        self.create_team10_button.setGeometry(47, 509, 95, 26)
        self.create_team10_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team10_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team10_button.setIconSize(QSize(16,16))
        self.create_team10_button.clicked.connect(lambda: self.handle_create_team_button(10))

        self.create_team6_side_button = QPushButton('', parent)
        self.create_team6_side_button.setGeometry(42, 509, 7, 26)
        self.create_team6_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team11_button = QPushButton('', parent)
        self.create_team11_button.setObjectName('create_team11_button')
        self.create_team11_button.setGeometry(47, 555, 95, 26)
        self.create_team11_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team11_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team11_button.setIconSize(QSize(16,16))
        self.create_team11_button.clicked.connect(lambda: self.handle_create_team_button(11))

        self.create_team11_side_button = QPushButton('', parent)
        self.create_team11_side_button.setGeometry(42, 555, 7, 26)
        self.create_team11_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team12_button = QPushButton('', parent)
        self.create_team12_button.setObjectName('create_team12_button')
        self.create_team12_button.setGeometry(47, 594, 95, 26)
        self.create_team12_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team12_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team12_button.setIconSize(QSize(16,16))
        self.create_team12_button.clicked.connect(lambda: self.handle_create_team_button(12))

        self.create_team12_side_button = QPushButton('', parent)
        self.create_team12_side_button.setGeometry(42, 594, 7, 26)
        self.create_team12_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team13_button = QPushButton('', parent)
        self.create_team13_button.setObjectName('create_team13_button')
        self.create_team13_button.setGeometry(47, 639, 95, 26)
        self.create_team13_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team13_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team13_button.setIconSize(QSize(16,16))
        self.create_team13_button.clicked.connect(lambda: self.handle_create_team_button(13))

        self.create_team13_side_button = QPushButton('', parent)
        self.create_team13_side_button.setGeometry(42, 639, 7, 26)
        self.create_team13_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')


        self.create_team14_button = QPushButton('', parent)
        self.create_team14_button.setObjectName('create_team14_button')
        self.create_team14_button.setGeometry(47, 678, 95, 26)
        self.create_team14_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team14_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team14_button.setIconSize(QSize(16,16))
        self.create_team14_button.clicked.connect(lambda: self.handle_create_team_button(14))

        self.create_team14_side_button = QPushButton('', parent)
        self.create_team14_side_button.setGeometry(42, 678, 7, 26)
        self.create_team14_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team15_button = QPushButton('', parent)
        self.create_team15_button.setObjectName('create_team15_button')
        self.create_team15_button.setGeometry(47, 724, 95, 26)
        self.create_team15_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team15_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team15_button.setIconSize(QSize(16,16))
        self.create_team15_button.clicked.connect(lambda: self.handle_create_team_button(15))

        self.create_team15_side_button = QPushButton('', parent)
        self.create_team15_side_button.setGeometry(42, 724, 7, 26)
        self.create_team15_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team16_button = QPushButton('', parent)
        self.create_team16_button.setObjectName('create_team16_button')
        self.create_team16_button.setGeometry(47, 762, 95, 26)
        self.create_team16_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team16_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team16_button.setIconSize(QSize(16,16))
        self.create_team16_button.clicked.connect(lambda: self.handle_create_team_button(16))

        self.create_team16_side_button = QPushButton('', parent)
        self.create_team16_side_button.setGeometry(42, 762, 7, 26)
        self.create_team16_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')



        # !--------------------------- right -------------------------------* #

        self.create_team17_button = QPushButton('', parent)
        self.create_team17_button.setObjectName('create_team17_button')
        self.create_team17_button.setGeometry(1393, 97, 95, 26)
        self.create_team17_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team17_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team17_button.setIconSize(QSize(16,16))
        self.create_team17_button.clicked.connect(lambda: self.handle_create_team_button(17))

        self.create_team17_side_button = QPushButton('', parent)
        self.create_team17_side_button.setGeometry(1486, 97, 7, 26)
        self.create_team17_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team18_button = QPushButton('', parent)
        self.create_team18_button.setObjectName('create_team18_button')
        self.create_team18_button.setGeometry(1393, 134, 95, 26)
        self.create_team18_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team18_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team18_button.setIconSize(QSize(16,16))
        self.create_team18_button.clicked.connect(lambda: self.handle_create_team_button(18))

        self.create_team18_side_button = QPushButton('', parent)
        self.create_team18_side_button.setGeometry(1486, 134, 7, 26)
        self.create_team18_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team19_button = QPushButton('', parent)
        self.create_team19_button.setObjectName('create_team19_button')
        self.create_team19_button.setGeometry(1393, 180, 95, 26)
        self.create_team19_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team19_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team19_button.setIconSize(QSize(16,16))
        self.create_team19_button.clicked.connect(lambda: self.handle_create_team_button(19))

        self.create_team19_side_button = QPushButton('', parent)
        self.create_team19_side_button.setGeometry(1486, 180, 7, 26)
        self.create_team19_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team20_button = QPushButton('', parent)
        self.create_team20_button.setObjectName('create_team20_button')
        self.create_team20_button.setGeometry(1393, 219, 95, 26)
        self.create_team20_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team20_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team20_button.setIconSize(QSize(16,16))
        self.create_team20_button.clicked.connect(lambda: self.handle_create_team_button(20))

        self.create_team20_side_button = QPushButton('', parent)
        self.create_team20_side_button.setGeometry(1486, 219, 7, 26)
        self.create_team20_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team21_button = QPushButton('', parent)
        self.create_team21_button.setObjectName('create_team21_button')
        self.create_team21_button.setGeometry(1393, 265, 95, 26)
        self.create_team21_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team21_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team21_button.setIconSize(QSize(16,16))
        self.create_team21_button.clicked.connect(lambda: self.handle_create_team_button(21))

        self.create_team21_side_button = QPushButton('', parent)
        self.create_team21_side_button.setGeometry(1486, 265, 7, 26)
        self.create_team21_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team22_button = QPushButton('', parent)
        self.create_team22_button.setObjectName('create_team22_button')
        self.create_team22_button.setGeometry(1393, 303, 95, 26)
        self.create_team22_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team22_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team22_button.setIconSize(QSize(16,16))
        self.create_team22_button.clicked.connect(lambda: self.handle_create_team_button(22))

        self.create_team22_side_button = QPushButton('', parent)
        self.create_team22_side_button.setGeometry(1486, 303, 7, 26)
        self.create_team22_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team23_button = QPushButton('', parent)
        self.create_team23_button.setObjectName('create_team23_button')
        self.create_team23_button.setGeometry(1393, 349, 95, 26)
        self.create_team23_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team23_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team23_button.setIconSize(QSize(16,16))
        self.create_team23_button.clicked.connect(lambda: self.handle_create_team_button(23))

        self.create_team23_side_button = QPushButton('', parent)
        self.create_team23_side_button.setGeometry(1486, 349, 7, 26)
        self.create_team23_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team24_button = QPushButton('', parent)
        self.create_team24_button.setObjectName('create_team24_button')
        self.create_team24_button.setGeometry(1393, 388, 95, 26)
        self.create_team24_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team24_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team24_button.setIconSize(QSize(16,16))
        self.create_team24_button.clicked.connect(lambda: self.handle_create_team_button(24))

        self.create_team24_side_button = QPushButton('', parent)
        self.create_team24_side_button.setGeometry(1486, 388, 7, 26)
        self.create_team24_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')


        # *---------------------------------------------------------------* #


        self.create_team25_button = QPushButton('', parent)
        self.create_team25_button.setObjectName('create_team25_button')
        self.create_team25_button.setGeometry(1393, 470, 95, 26)
        self.create_team25_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team25_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team25_button.setIconSize(QSize(16,16))
        self.create_team25_button.clicked.connect(lambda: self.handle_create_team_button(25))

        self.create_team25_side_button = QPushButton('', parent)
        self.create_team25_side_button.setGeometry(1486, 470, 7, 26)
        self.create_team25_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team26_button = QPushButton('', parent)
        self.create_team26_button.setObjectName('create_team26_button')
        self.create_team26_button.setGeometry(1393, 509, 95, 26)
        self.create_team26_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team26_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team26_button.setIconSize(QSize(16,16))
        self.create_team26_button.clicked.connect(lambda: self.handle_create_team_button(26))

        self.create_team26_side_button = QPushButton('', parent)
        self.create_team26_side_button.setGeometry(1486, 509, 7, 26)
        self.create_team26_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team27_button = QPushButton('', parent)
        self.create_team27_button.setObjectName('create_team27_button')
        self.create_team27_button.setGeometry(1393, 555, 95, 26)
        self.create_team27_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team27_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team27_button.setIconSize(QSize(16,16))
        self.create_team27_button.clicked.connect(lambda: self.handle_create_team_button(27))

        self.create_team27_side_button = QPushButton('', parent)
        self.create_team27_side_button.setGeometry(1486, 555, 7, 26)
        self.create_team27_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team28_button = QPushButton('', parent)
        self.create_team28_button.setObjectName('create_team28_button')
        self.create_team28_button.setGeometry(1393, 594, 95, 26)
        self.create_team28_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team28_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team28_button.setIconSize(QSize(16,16))
        self.create_team28_button.clicked.connect(lambda: self.handle_create_team_button(28))

        self.create_team28_side_button = QPushButton('', parent)
        self.create_team28_side_button.setGeometry(1486, 594, 7, 26)
        self.create_team28_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team29_button = QPushButton('', parent)
        self.create_team29_button.setObjectName('create_team29_button')
        self.create_team29_button.setGeometry(1393, 639, 95, 26)
        self.create_team29_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team29_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team29_button.setIconSize(QSize(16,16))
        self.create_team29_button.clicked.connect(lambda: self.handle_create_team_button(29))

        self.create_team29_side_button = QPushButton('', parent)
        self.create_team29_side_button.setGeometry(1486, 639, 7, 26)
        self.create_team29_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team30_button = QPushButton('', parent)
        self.create_team30_button.setObjectName('create_team30_button')
        self.create_team30_button.setGeometry(1393, 678, 95, 26)
        self.create_team30_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team30_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team30_button.setIconSize(QSize(16,16))
        self.create_team30_button.clicked.connect(lambda: self.handle_create_team_button(30))

        self.create_team30_side_button = QPushButton('', parent)
        self.create_team30_side_button.setGeometry(1486, 678, 7, 26)
        self.create_team30_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team31_button = QPushButton('', parent)
        self.create_team31_button.setObjectName('create_team31_button')
        self.create_team31_button.setGeometry(1393, 724, 95, 26)
        self.create_team31_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team31_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team31_button.setIconSize(QSize(16,16))
        self.create_team31_button.clicked.connect(lambda: self.handle_create_team_button(31))

        self.create_team31_side_button = QPushButton('', parent)
        self.create_team31_side_button.setGeometry(1486, 724, 7, 26)
        self.create_team31_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.create_team32_button = QPushButton('', parent)
        self.create_team32_button.setObjectName('create_team32_button')
        self.create_team32_button.setGeometry(1393, 762, 95, 26)
        self.create_team32_button.setStyleSheet('''
                    QPushButton{
            background: transparent;
            background-color: #d9d9d9;
            border: none;
        }
                            QPushButton:hover{
            background: transparent;
            background-color: #62000000;
            border: none;
            }
        ''')
        self.create_team32_button.setIcon(QIcon(r'C:\pic\create_team_plus_icon.png'))
        self.create_team32_button.setIconSize(QSize(16,16))
        self.create_team32_button.clicked.connect(lambda: self.handle_create_team_button(32))

        self.create_team32_side_button = QPushButton('', parent)
        self.create_team32_side_button.setGeometry(1486, 762, 7, 26)
        self.create_team32_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')


    # *------------------------------ round 16 team --------------------------------* #

        self.round_16_team_1_button = QPushButton('', parent)
        self.round_16_team_1_button.setObjectName('round_16_team_1_button')
        self.round_16_team_1_button.setGeometry(178, 116, 96, 26)
        self.round_16_team_1_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_1_side_button = QPushButton('', parent)
        self.round_16_team_1_side_button.setGeometry(173, 116, 6, 26)
        self.round_16_team_1_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_2_button = QPushButton('', parent)
        self.round_16_team_2_button.setObjectName('round_16_team_2_button')
        self.round_16_team_2_button.setGeometry(178, 200, 96, 26)
        self.round_16_team_2_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_2_side_button = QPushButton('', parent)
        self.round_16_team_2_side_button.setGeometry(173, 200, 6, 26)
        self.round_16_team_2_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_3_button = QPushButton('', parent)
        self.round_16_team_3_button.setObjectName('round_16_team_3_button')
        self.round_16_team_3_button.setGeometry(178, 285, 96, 26)
        self.round_16_team_3_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_3_side_button = QPushButton('', parent)
        self.round_16_team_3_side_button.setGeometry(173, 285, 6, 26)
        self.round_16_team_3_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_4_button = QPushButton('', parent)
        self.round_16_team_4_button.setObjectName('round_16_team_4_button')
        self.round_16_team_4_button.setGeometry(178, 369, 96, 26)
        self.round_16_team_4_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_4_side_button = QPushButton('', parent)
        self.round_16_team_4_side_button.setGeometry(173, 369, 6, 26)
        self.round_16_team_4_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

    # *------------------------------ round 16 team --------------------------------* #

        self.round_16_team_5_button = QPushButton('', parent)
        self.round_16_team_5_button.setObjectName('round_16_team_5_button')
        self.round_16_team_5_button.setGeometry(178, 491, 96, 26)
        self.round_16_team_5_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_5_side_button = QPushButton('', parent)
        self.round_16_team_5_side_button.setGeometry(173, 491, 6, 26)
        self.round_16_team_5_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_6_button = QPushButton('', parent)
        self.round_16_team_6_button.setObjectName('round_16_team_6_button')
        self.round_16_team_6_button.setGeometry(178, 573, 96, 26)
        self.round_16_team_6_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_6_side_button = QPushButton('', parent)
        self.round_16_team_6_side_button.setGeometry(173, 573, 6, 26)
        self.round_16_team_6_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_7_button = QPushButton('', parent)
        self.round_16_team_7_button.setObjectName('round_16_team_7_button')
        self.round_16_team_7_button.setGeometry(178, 660, 96, 26)
        self.round_16_team_7_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_7_side_button = QPushButton('', parent)
        self.round_16_team_7_side_button.setGeometry(173, 660, 6, 26)
        self.round_16_team_7_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_8_button = QPushButton('', parent)
        self.round_16_team_8_button.setObjectName('round_16_team_8_button')
        self.round_16_team_8_button.setGeometry(178, 745, 96, 26)
        self.round_16_team_8_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_8_side_button = QPushButton('', parent)
        self.round_16_team_8_side_button.setGeometry(173, 745, 6, 26)
        self.round_16_team_8_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

    # *------------------------------ round 16 team --------------------------------* #

        self.round_16_team_9_button = QPushButton('', parent)
        self.round_16_team_9_button.setObjectName('round_16_team_9_button')
        self.round_16_team_9_button.setGeometry(1261, 116, 96, 26)
        self.round_16_team_9_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_9_side_button = QPushButton('', parent)
        self.round_16_team_9_side_button.setGeometry(1357, 116, 6, 26)
        self.round_16_team_9_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_10_button = QPushButton('', parent)
        self.round_16_team_10_button.setObjectName('round_16_team_10_button')
        self.round_16_team_10_button.setGeometry(1261, 200, 96, 26)
        self.round_16_team_10_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_10_side_button = QPushButton('', parent)
        self.round_16_team_10_side_button.setGeometry(1357, 200, 6, 26)
        self.round_16_team_10_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_11_button = QPushButton('', parent)
        self.round_16_team_11_button.setObjectName('round_16_team_11_button')
        self.round_16_team_11_button.setGeometry(1261, 285, 96, 26)
        self.round_16_team_11_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_11_side_button = QPushButton('', parent)
        self.round_16_team_11_side_button.setGeometry(1357, 285, 6, 26)
        self.round_16_team_11_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_12_button = QPushButton('', parent)
        self.round_16_team_12_button.setObjectName('round_16_team_12_button')
        self.round_16_team_12_button.setGeometry(1261, 369, 96, 26)
        self.round_16_team_12_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_12_side_button = QPushButton('', parent)
        self.round_16_team_12_side_button.setGeometry(1357, 369, 6, 26)
        self.round_16_team_12_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

    # *------------------------------ round 16 team --------------------------------* #

        self.round_16_team_13_button = QPushButton('', parent)
        self.round_16_team_13_button.setObjectName('round_16_team_13_button')
        self.round_16_team_13_button.setGeometry(1261, 491, 96, 26)
        self.round_16_team_13_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_13_side_button = QPushButton('', parent)
        self.round_16_team_13_side_button.setGeometry(1357, 491, 6, 26)
        self.round_16_team_13_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_14_button = QPushButton('', parent)
        self.round_16_team_14_button.setObjectName('round_16_team_14_button')
        self.round_16_team_14_button.setGeometry(1261, 573, 96, 26)
        self.round_16_team_14_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_14_side_button = QPushButton('', parent)
        self.round_16_team_14_side_button.setGeometry(1357, 573, 6, 26)
        self.round_16_team_14_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_15_button = QPushButton('', parent)
        self.round_16_team_15_button.setObjectName('round_16_team_15_button')
        self.round_16_team_15_button.setGeometry(1261, 660, 96, 26)
        self.round_16_team_15_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_15_side_button = QPushButton('', parent)
        self.round_16_team_15_side_button.setGeometry(1357, 660, 6, 26)
        self.round_16_team_15_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_16_team_16_button = QPushButton('', parent)
        self.round_16_team_16_button.setObjectName('round_16_team_16_button')
        self.round_16_team_16_button.setGeometry(1261, 745, 96, 26)
        self.round_16_team_16_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_16_team_16_side_button = QPushButton('', parent)
        self.round_16_team_16_side_button.setGeometry(1357, 745, 6, 26)
        self.round_16_team_16_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')


    # !------------------------------ round 8 team --------------------------------* #

        self.round_8_team_1_button = QPushButton('', parent)
        self.round_8_team_1_button.setObjectName('round_8_team_1_button')
        self.round_8_team_1_button.setGeometry(310, 160, 97, 26)
        self.round_8_team_1_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_8_team_1_side_button = QPushButton('', parent)
        self.round_8_team_1_side_button.setGeometry(304, 160, 6, 26)
        self.round_8_team_1_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_8_team_2_button = QPushButton('', parent)
        self.round_8_team_2_button.setObjectName('round_8_team_2_button')
        self.round_8_team_2_button.setGeometry(310, 329, 97, 26)
        self.round_8_team_2_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_8_team_2_side_button = QPushButton('', parent)
        self.round_8_team_2_side_button.setGeometry(304, 329, 6, 26)
        self.round_8_team_2_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_8_team_3_button = QPushButton('', parent)
        self.round_8_team_3_button.setObjectName('round_8_team_3_button')
        self.round_8_team_3_button.setGeometry(310, 532, 97, 26)
        self.round_8_team_3_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_8_team_3_side_button = QPushButton('', parent)
        self.round_8_team_3_side_button.setGeometry(304, 532, 6, 26)
        self.round_8_team_3_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_8_team_4_button = QPushButton('', parent)
        self.round_8_team_4_button.setObjectName('round_8_team_4_button')
        self.round_8_team_4_button.setGeometry(310, 704, 97, 26)
        self.round_8_team_4_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_8_team_4_side_button = QPushButton('', parent)
        self.round_8_team_4_side_button.setGeometry(304, 704, 6, 26)
        self.round_8_team_4_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

    # !------------------------------ round 8 team --------------------------------* #

        self.round_8_team_5_button = QPushButton('', parent)
        self.round_8_team_5_button.setObjectName('round_8_team_5_button')
        self.round_8_team_5_button.setGeometry(1128, 157, 97, 26)
        self.round_8_team_5_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_8_team_5_side_button = QPushButton('', parent)
        self.round_8_team_5_side_button.setGeometry(1225, 157, 6, 26)
        self.round_8_team_5_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_8_team_6_button = QPushButton('', parent)
        self.round_8_team_6_button.setObjectName('round_8_team_6_button')
        self.round_8_team_6_button.setGeometry(1128, 326, 97, 26)
        self.round_8_team_6_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_8_team_6_side_button = QPushButton('', parent)
        self.round_8_team_6_side_button.setGeometry(1225, 326, 6, 26)
        self.round_8_team_6_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_8_team_7_button = QPushButton('', parent)
        self.round_8_team_7_button.setObjectName('round_8_team_7_button')
        self.round_8_team_7_button.setGeometry(1128, 529, 97, 26)
        self.round_8_team_7_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_8_team_7_side_button = QPushButton('', parent)
        self.round_8_team_7_side_button.setGeometry(1225, 529, 6, 26)
        self.round_8_team_7_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_8_team_8_button = QPushButton('', parent)
        self.round_8_team_8_button.setObjectName('round_8_team_8_button')
        self.round_8_team_8_button.setGeometry(1128, 701, 97, 26)
        self.round_8_team_8_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_8_team_8_side_button = QPushButton('', parent)
        self.round_8_team_8_side_button.setGeometry(1225, 701, 6, 26)
        self.round_8_team_8_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

    # ?------------------------------ round 4 team --------------------------------* #

        self.round_4_team_1_button = QPushButton('', parent)
        self.round_4_team_1_button.setObjectName('round_4_team_1_button')
        self.round_4_team_1_button.setGeometry(443, 242, 97, 26)
        self.round_4_team_1_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_4_team_1_side_button = QPushButton('', parent)
        self.round_4_team_1_side_button.setGeometry(437, 242, 6, 26)
        self.round_4_team_1_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_4_team_2_button = QPushButton('', parent)
        self.round_4_team_2_button.setObjectName('round_4_team_2_button')
        self.round_4_team_2_button.setGeometry(443, 618, 97, 26)
        self.round_4_team_2_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_4_team_2_side_button = QPushButton('', parent)
        self.round_4_team_2_side_button.setGeometry(437, 618, 6, 26)
        self.round_4_team_2_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

    # ?------------------------------ round 4 team --------------------------------* #

        self.round_4_team_3_button = QPushButton('', parent)
        self.round_4_team_3_button.setObjectName('round_4_team_3_button')
        self.round_4_team_3_button.setGeometry(994, 241, 98, 26)
        self.round_4_team_3_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_4_team_3_side_button = QPushButton('', parent)
        self.round_4_team_3_side_button.setGeometry(1092, 241, 6, 26)
        self.round_4_team_3_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_4_team_4_button = QPushButton('', parent)
        self.round_4_team_4_button.setObjectName('round_4_team_4_button')
        self.round_4_team_4_button.setGeometry(994, 617, 98, 26)
        self.round_4_team_4_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_4_team_4_side_button = QPushButton('', parent)
        self.round_4_team_4_side_button.setGeometry(1092, 617, 6, 26)
        self.round_4_team_4_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

    # !------------------------------ round 2 team --------------------------------* #

        self.round_2_team_1_button = QPushButton('', parent)
        self.round_2_team_1_button.setObjectName('round_2_team_1_button')
        self.round_2_team_1_button.setGeometry(585, 417, 97, 26)
        self.round_2_team_1_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_2_team_1_side_button = QPushButton('', parent)
        self.round_2_team_1_side_button.setGeometry(578, 417, 7, 26)
        self.round_2_team_1_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

        self.round_2_team_2_button = QPushButton('', parent)
        self.round_2_team_2_button.setObjectName('round_2_team_2_button')
        self.round_2_team_2_button.setGeometry(854, 417, 97, 26)
        self.round_2_team_2_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: #d9d9d9;
                                border: none;
                            }
                                            ''')

        self.round_2_team_2_side_button = QPushButton('', parent)
        self.round_2_team_2_side_button.setGeometry(951, 417, 7, 26)
        self.round_2_team_2_side_button.setStyleSheet('''
                            QPushButton{
                                background: transparent;
                                background-color: black;
                                border: none;
                            }
                                               ''')

    # todo------------------------------ line --------------------------------* #

        self.team1_line = QPushButton(parent)
        self.team1_line.setGeometry(142, 109, 16, 2)
        self.team1_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team2_line = QPushButton(parent)
        self.team2_line.setGeometry(142, 145, 16, 2)
        self.team2_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team3_line = QPushButton(parent)
        self.team3_line.setGeometry(142, 192, 16, 2)
        self.team3_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team4_line = QPushButton(parent)
        self.team4_line.setGeometry(142, 232, 16, 2)
        self.team4_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team5_line = QPushButton(parent)
        self.team5_line.setGeometry(142, 276, 16, 2)
        self.team5_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team6_line = QPushButton(parent)
        self.team6_line.setGeometry(142, 316, 16, 2)
        self.team6_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team7_line = QPushButton(parent)
        self.team7_line.setGeometry(142, 360, 16, 2)
        self.team7_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team8_line = QPushButton(parent)
        self.team8_line.setGeometry(142, 400, 16, 2)
        self.team8_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team9_line = QPushButton(parent)
        self.team9_line.setGeometry(142, 480, 16, 2)
        self.team9_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team10_line = QPushButton(parent)
        self.team10_line.setGeometry(142, 520, 16, 2)
        self.team10_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team11_line = QPushButton(parent)
        self.team11_line.setGeometry(142, 565, 16, 2)
        self.team11_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team12_line = QPushButton(parent)
        self.team12_line.setGeometry(142, 605, 16, 2)
        self.team12_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team13_line = QPushButton(parent)
        self.team13_line.setGeometry(142, 649, 16, 2)
        self.team13_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team14_line = QPushButton(parent)
        self.team14_line.setGeometry(142, 689, 16, 2)
        self.team14_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team15_line = QPushButton(parent)
        self.team15_line.setGeometry(142, 736, 16, 2)
        self.team15_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team16_line = QPushButton(parent)
        self.team16_line.setGeometry(142, 773, 16, 2)
        self.team16_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')


        self.team17_line = QPushButton(parent)
        self.team17_line.setGeometry(1377, 109, 16, 2)
        self.team17_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team18_line = QPushButton(parent)
        self.team18_line.setGeometry(1377, 145, 16, 2)
        self.team18_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team19_line = QPushButton(parent)
        self.team19_line.setGeometry(1377, 192, 16, 2)
        self.team19_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team20_line = QPushButton(parent)
        self.team20_line.setGeometry(1377, 232, 16, 2)
        self.team20_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team21_line = QPushButton(parent)
        self.team21_line.setGeometry(1377, 276, 16, 2)
        self.team21_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team22_line = QPushButton(parent)
        self.team22_line.setGeometry(1377, 316, 16, 2)
        self.team22_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team23_line = QPushButton(parent)
        self.team23_line.setGeometry(1377, 360, 16, 2)
        self.team23_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team24_line = QPushButton(parent)
        self.team24_line.setGeometry(1377, 400, 16, 2)
        self.team24_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team25_line = QPushButton(parent)
        self.team25_line.setGeometry(1377, 480, 16, 2)
        self.team25_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team26_line = QPushButton(parent)
        self.team26_line.setGeometry(1377, 520, 16, 2)
        self.team26_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team27_line = QPushButton(parent)
        self.team27_line.setGeometry(1377, 565, 16, 2)
        self.team27_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team28_line = QPushButton(parent)
        self.team28_line.setGeometry(1377, 605, 16, 2)
        self.team28_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team29_line = QPushButton(parent)
        self.team29_line.setGeometry(1377, 649, 16, 2)
        self.team29_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team30_line = QPushButton(parent)
        self.team30_line.setGeometry(1377, 689, 16, 2)
        self.team30_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team31_line = QPushButton(parent)
        self.team31_line.setGeometry(1377, 736, 16, 2)
        self.team31_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team32_line = QPushButton(parent)
        self.team32_line.setGeometry(1377, 773, 16, 2)
        self.team32_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

    # todo------------------------------ line --------------------------------* #

        self.team1_line_vertical = QPushButton(parent)
        self.team1_line_vertical.setGeometry(157, 109, 2, 19)
        self.team1_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team2_line_vertical = QPushButton(parent)
        self.team2_line_vertical.setGeometry(157, 129, 2, 18)
        self.team2_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team3_line_vertical = QPushButton(parent)
        self.team3_line_vertical.setGeometry(157, 192, 2, 20)
        self.team3_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team4_line_vertical = QPushButton(parent)
        self.team4_line_vertical.setGeometry(157, 214, 2, 20)
        self.team4_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team5_line_vertical = QPushButton(parent)
        self.team5_line_vertical.setGeometry(157, 276, 2, 20)
        self.team5_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team6_line_vertical = QPushButton(parent)
        self.team6_line_vertical.setGeometry(157, 298, 2, 20)
        self.team6_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team7_line_vertical = QPushButton(parent)
        self.team7_line_vertical.setGeometry(157, 360, 2, 20)
        self.team7_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team8_line_vertical = QPushButton(parent)
        self.team8_line_vertical.setGeometry(157, 382, 2, 20)
        self.team8_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team9_line_vertical = QPushButton(parent)
        self.team9_line_vertical.setGeometry(157, 480, 2, 22)
        self.team9_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team10_line_vertical = QPushButton(parent)
        self.team10_line_vertical.setGeometry(157, 503, 2, 19)
        self.team10_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team11_line_vertical = QPushButton(parent)
        self.team11_line_vertical.setGeometry(157, 565, 2, 20)
        self.team11_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team12_line_vertical = QPushButton(parent)
        self.team12_line_vertical.setGeometry(157, 586, 2, 20)
        self.team12_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team13_line_vertical = QPushButton(parent)
        self.team13_line_vertical.setGeometry(157, 649, 2, 23)
        self.team13_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team14_line_vertical = QPushButton(parent)
        self.team14_line_vertical.setGeometry(157, 672, 2, 19)
        self.team14_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team15_line_vertical = QPushButton(parent)
        self.team15_line_vertical.setGeometry(157, 736, 2, 20)
        self.team15_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team16_line_vertical = QPushButton(parent)
        self.team16_line_vertical.setGeometry(157, 757, 2, 18)
        self.team16_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team17_line_vertical = QPushButton(parent)
        self.team17_line_vertical.setGeometry(1376, 109, 2, 19)
        self.team17_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team18_line_vertical = QPushButton(parent)
        self.team18_line_vertical.setGeometry(1376, 129, 2, 18)
        self.team18_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team19_line_vertical = QPushButton(parent)
        self.team19_line_vertical.setGeometry(1376, 192, 2, 20)
        self.team19_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team20_line_vertical = QPushButton(parent)
        self.team20_line_vertical.setGeometry(1376, 214, 2, 20)
        self.team20_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team21_line_vertical = QPushButton(parent)
        self.team21_line_vertical.setGeometry(1376, 276, 2, 20)
        self.team21_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team22_line_vertical = QPushButton(parent)
        self.team22_line_vertical.setGeometry(1376, 298, 2, 20)
        self.team22_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team23_line_vertical = QPushButton(parent)
        self.team23_line_vertical.setGeometry(1376, 360, 2, 20)
        self.team23_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team24_line_vertical = QPushButton(parent)
        self.team24_line_vertical.setGeometry(1376, 382, 2, 20)
        self.team24_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team25_line_vertical = QPushButton(parent)
        self.team25_line_vertical.setGeometry(1376, 480, 2, 22)
        self.team25_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team26_line_vertical = QPushButton(parent)
        self.team26_line_vertical.setGeometry(1376, 503, 2, 19)
        self.team26_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team27_line_vertical = QPushButton(parent)
        self.team27_line_vertical.setGeometry(1376, 565, 2, 20)
        self.team27_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team28_line_vertical = QPushButton(parent)
        self.team28_line_vertical.setGeometry(1376, 586, 2, 20)
        self.team28_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team29_line_vertical = QPushButton(parent)
        self.team29_line_vertical.setGeometry(1376, 649, 2, 23)
        self.team29_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team30_line_vertical = QPushButton(parent)
        self.team30_line_vertical.setGeometry(1376, 672, 2, 19)
        self.team30_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team31_line_vertical = QPushButton(parent)
        self.team31_line_vertical.setGeometry(1376, 736, 2, 20)
        self.team31_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team32_line_vertical = QPushButton(parent)
        self.team32_line_vertical.setGeometry(1376, 757, 2, 18)
        self.team32_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')


        self.team_1_2_line_horizontal = QPushButton(parent)
        self.team_1_2_line_horizontal.setGeometry(157, 128, 16, 2)
        self.team_1_2_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_3_4_line_horizontal = QPushButton(parent)
        self.team_3_4_line_horizontal.setGeometry(157, 212, 16, 2)
        self.team_3_4_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_5_6_line_horizontal = QPushButton(parent)
        self.team_5_6_line_horizontal.setGeometry(157, 296, 16, 2)
        self.team_5_6_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_7_8_line_horizontal = QPushButton(parent)
        self.team_7_8_line_horizontal.setGeometry(157, 380, 16, 2)
        self.team_7_8_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_9_10_line_horizontal = QPushButton(parent)
        self.team_9_10_line_horizontal.setGeometry(157, 501, 16, 2)
        self.team_9_10_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_11_12_line_horizontal = QPushButton(parent)
        self.team_11_12_line_horizontal.setGeometry(157, 585, 16, 2)
        self.team_11_12_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_13_14_line_horizontal = QPushButton(parent)
        self.team_13_14_line_horizontal.setGeometry(157, 672, 16, 2)
        self.team_13_14_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_15_16_line_horizontal = QPushButton(parent)
        self.team_15_16_line_horizontal.setGeometry(157, 756, 16, 2)
        self.team_15_16_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_17_18_line_horizontal = QPushButton(parent)
        self.team_17_18_line_horizontal.setGeometry(1362, 128, 16, 2)
        self.team_17_18_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_19_20_line_horizontal = QPushButton(parent)
        self.team_19_20_line_horizontal.setGeometry(1362, 212, 16, 2)
        self.team_19_20_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_21_22_line_horizontal = QPushButton(parent)
        self.team_21_22_line_horizontal.setGeometry(1362, 296, 16, 2)
        self.team_21_22_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_23_24_line_horizontal = QPushButton(parent)
        self.team_23_24_line_horizontal.setGeometry(1362, 380, 16, 2)
        self.team_23_24_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_25_26_line_horizontal = QPushButton(parent)
        self.team_25_26_line_horizontal.setGeometry(1362, 501, 16, 2)
        self.team_25_26_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_27_28_line_horizontal = QPushButton(parent)
        self.team_27_28_line_horizontal.setGeometry(1362, 585, 16, 2)
        self.team_27_28_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_29_30_line_horizontal = QPushButton(parent)
        self.team_29_30_line_horizontal.setGeometry(1362, 672, 16, 2)
        self.team_29_30_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.team_31_32_line_horizontal = QPushButton(parent)
        self.team_31_32_line_horizontal.setGeometry(1362, 756, 16, 2)
        self.team_31_32_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

    # todo------------------------------ line --------------------------------* #

        self.round_16_team_1_line = QPushButton(parent)
        self.round_16_team_1_line.setGeometry(274, 128, 16, 2)
        self.round_16_team_1_line.setStyleSheet('''
                                        background: transparent;
                                        background-color: black;
                                        border: none;
                                        ''')


        self.round_16_team_2_line = QPushButton(parent)
        self.round_16_team_2_line.setGeometry(274, 212, 16, 2)
        self.round_16_team_2_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        selround_16_team_3_line = QPushButton(parent)
        selround_16_team_3_line.setGeometry(274, 296, 16, 2)
        selround_16_team_3_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        selround_16_team_4_line = QPushButton(parent)
        selround_16_team_4_line.setGeometry(274, 380, 16, 2)
        selround_16_team_4_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        selfround_16_team_5_line = QPushButton(parent)
        selfround_16_team_5_line.setGeometry(274, 501, 16, 2)
        selfround_16_team_5_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_6_line = QPushButton(parent)
        self.round_16_team_6_line.setGeometry(274, 585, 16, 2)
        self.round_16_team_6_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_7_line = QPushButton(parent)
        self.round_16_team_7_line.setGeometry(274, 672, 16, 2)
        self.round_16_team_7_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_8_line = QPushButton(parent)
        self.round_16_team_8_line.setGeometry(274, 756, 16, 2)
        self.round_16_team_8_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_9_line = QPushButton(parent)
        self.round_16_team_9_line.setGeometry(1245, 128, 16, 2)
        self.round_16_team_9_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_10_line = QPushButton(parent)
        self.round_16_team_10_line.setGeometry(1245, 212, 16, 2)
        self.round_16_team_10_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_11_line = QPushButton(parent)
        self.round_16_team_11_line.setGeometry(1245, 296, 16, 2)
        self.round_16_team_11_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_12_line = QPushButton(parent)
        self.round_16_team_12_line.setGeometry(1245, 380, 16, 2)
        self.round_16_team_12_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_13_line = QPushButton(parent)
        self.round_16_team_13_line.setGeometry(1245, 501, 16, 2)
        self.round_16_team_13_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_14_line = QPushButton(parent)
        self.round_16_team_14_line.setGeometry(1245, 585, 16, 2)
        self.round_16_team_14_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_15_line = QPushButton(parent)
        self.round_16_team_15_line.setGeometry(1245, 672, 16, 2)
        self.round_16_team_15_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_16_line = QPushButton(parent)
        self.round_16_team_16_line.setGeometry(1245, 756, 16, 2)
        self.round_16_team_16_line.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

    # todo------------------------------ line vertical --------------------------------* #

        self.round_16_team_1_line_vertical = QPushButton(parent)
        self.round_16_team_1_line_vertical.setGeometry(289, 128, 2, 44)
        self.round_16_team_1_line_vertical.setStyleSheet('''
                                        background: transparent;
                                        background-color: black;
                                        border: none;
                                        ''')


        self.round_16_team_2_line_vertical = QPushButton(parent)
        self.round_16_team_2_line_vertical.setGeometry(289, 174, 2, 40)
        self.round_16_team_2_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        selround_16_team_3_line_vertical = QPushButton(parent)
        selround_16_team_3_line_vertical.setGeometry(289, 296, 2, 44)
        selround_16_team_3_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        selround_16_team_4_line_vertical = QPushButton(parent)
        selround_16_team_4_line_vertical.setGeometry(289, 342, 2, 40)
        selround_16_team_4_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        selfround_16_team_5_line_vertical = QPushButton(parent)
        selfround_16_team_5_line_vertical.setGeometry(289, 501, 2, 43)
        selfround_16_team_5_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_6_line_vertical = QPushButton(parent)
        self.round_16_team_6_line_vertical.setGeometry(289, 546, 2, 41)
        self.round_16_team_6_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_7_line_vertical = QPushButton(parent)
        self.round_16_team_7_line_vertical.setGeometry(289, 672, 2, 44)
        self.round_16_team_7_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_8_line_vertical = QPushButton(parent)
        self.round_16_team_8_line_vertical.setGeometry(289, 718, 2, 40)
        self.round_16_team_8_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')


        self.round_16_team_9_line_vertical = QPushButton(parent)
        self.round_16_team_9_line_vertical.setGeometry(1245, 128, 2, 42)
        self.round_16_team_9_line_vertical.setStyleSheet('''
                                        background: transparent;
                                        background-color: black;
                                        border: none;
                                        ''')

        self.round_16_team_10_line_vertical = QPushButton(parent)
        self.round_16_team_10_line_vertical.setGeometry(1245, 170, 2, 44)
        self.round_16_team_10_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_11_line_vertical = QPushButton(parent)
        self.round_16_team_11_line_vertical.setGeometry(1245, 296, 2, 42)
        self.round_16_team_11_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_12_line_vertical = QPushButton(parent)
        self.round_16_team_12_line_vertical.setGeometry(1245, 338, 2, 44)
        self.round_16_team_12_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_13_line_vertical = QPushButton(parent)
        self.round_16_team_13_line_vertical.setGeometry(1245, 501, 2, 42)
        self.round_16_team_13_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_14_line_vertical = QPushButton(parent)
        self.round_16_team_14_line_vertical.setGeometry(1245, 542, 2, 43)
        self.round_16_team_14_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_15_line_vertical = QPushButton(parent)
        self.round_16_team_15_line_vertical.setGeometry(1245, 672, 2, 42)
        self.round_16_team_15_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_16_line_vertical = QPushButton(parent)
        self.round_16_team_16_line_vertical.setGeometry(1245, 714, 2, 44)
        self.round_16_team_16_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

    # todo------------------------------ line horizontal round16 --------------------------------* #

        self.round_16_team_1_2_line_horizontal = QPushButton(parent)
        self.round_16_team_1_2_line_horizontal.setGeometry(289, 172, 15, 2)
        self.round_16_team_1_2_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        selround_16_team_3_4_line_horizontal = QPushButton(parent)
        selround_16_team_3_4_line_horizontal.setGeometry(289, 340, 15, 2)
        selround_16_team_3_4_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_5_6_line_horizontal = QPushButton(parent)
        self.round_16_team_5_6_line_horizontal.setGeometry(289, 544, 15, 2)
        self.round_16_team_5_6_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_7_8_line_horizontal = QPushButton(parent)
        self.round_16_team_7_8_line_horizontal.setGeometry(289, 716, 15, 2)
        self.round_16_team_7_8_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_9_10_line_horizontal = QPushButton(parent)
        self.round_16_team_9_10_line_horizontal.setGeometry(1231, 169, 15, 2)
        self.round_16_team_9_10_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_11_12_line_horizontal = QPushButton(parent)
        self.round_16_team_11_12_line_horizontal.setGeometry(1231, 337, 15, 2)
        self.round_16_team_11_12_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_13_14_line_horizontal = QPushButton(parent)
        self.round_16_team_13_14_line_horizontal.setGeometry(1231, 541, 15, 2)
        self.round_16_team_13_14_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_16_team_15_16_line_horizontal = QPushButton(parent)
        self.round_16_team_15_16_line_horizontal.setGeometry(1231, 713, 15, 2)
        self.round_16_team_15_16_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

    # todo------------------------------ line horizontal round8 --------------------------------* #

        self.round_8_team_1_line_horizontal = QPushButton(parent)
        self.round_8_team_1_line_horizontal.setGeometry(407, 172, 15, 2)
        self.round_8_team_1_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_2_line_horizontal = QPushButton(parent)
        self.round_8_team_2_line_horizontal.setGeometry(407, 340, 15, 2)
        self.round_8_team_2_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_3_line_horizontal = QPushButton(parent)
        self.round_8_team_3_line_horizontal.setGeometry(407, 544, 15, 2)
        self.round_8_team_3_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_4_line_horizontal = QPushButton(parent)
        self.round_8_team_4_line_horizontal.setGeometry(407, 716, 15, 2)
        self.round_8_team_4_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_5_line_horizontal = QPushButton(parent)
        self.round_8_team_5_line_horizontal.setGeometry(1113, 169, 15, 2)
        self.round_8_team_5_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_6_line_horizontal = QPushButton(parent)
        self.round_8_team_6_line_horizontal.setGeometry(1113, 337, 15, 2)
        self.round_8_team_6_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_7_line_horizontal = QPushButton(parent)
        self.round_8_team_7_line_horizontal.setGeometry(1113, 541, 15, 2)
        self.round_8_team_7_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_8_line_horizontal = QPushButton(parent)
        self.round_8_team_8_line_horizontal.setGeometry(1113, 713, 15, 2)
        self.round_8_team_8_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

    # todo------------------------------ line vertical round8 --------------------------------* #

        self.round_8_team_1_line_vertical = QPushButton(parent)
        self.round_8_team_1_line_vertical.setGeometry(421, 172, 2, 82)
        self.round_8_team_1_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_2_line_vertical = QPushButton(parent)
        self.round_8_team_2_line_vertical.setGeometry(421, 255, 2, 87)
        self.round_8_team_2_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_3_line_vertical = QPushButton(parent)
        self.round_8_team_3_line_vertical.setGeometry(421, 544, 2, 86)
        self.round_8_team_3_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_4_line_vertical = QPushButton(parent)
        self.round_8_team_4_line_vertical.setGeometry(421, 631, 2, 87)
        self.round_8_team_4_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_5_line_vertical = QPushButton(parent)
        self.round_8_team_5_line_vertical.setGeometry(1113, 170, 2, 82)
        self.round_8_team_5_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_6_line_vertical = QPushButton(parent)
        self.round_8_team_6_line_vertical.setGeometry(1113, 254, 2, 84)
        self.round_8_team_6_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_7_line_vertical = QPushButton(parent)
        self.round_8_team_7_line_vertical.setGeometry(1113, 542, 2, 86)
        self.round_8_team_7_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_8_line_vertical = QPushButton(parent)
        self.round_8_team_8_line_vertical.setGeometry(1113, 630, 2, 84)
        self.round_8_team_8_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

    # todo------------------------------ line horizontal round8 --------------------------------* #

        self.round_8_team_1_2_line_horizontal = QPushButton(parent)
        self.round_8_team_1_2_line_horizontal.setGeometry(421, 253, 16, 2)
        self.round_8_team_1_2_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_3_4_line_horizontal = QPushButton(parent)
        self.round_8_team_3_4_line_horizontal.setGeometry(421, 629, 16, 2)
        self.round_8_team_3_4_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_5_6_line_horizontal = QPushButton(parent)
        self.round_8_team_5_6_line_horizontal.setGeometry(1098, 252, 17, 2)
        self.round_8_team_5_6_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_8_team_7_8_line_horizontal = QPushButton(parent)
        self.round_8_team_7_8_line_horizontal.setGeometry(1098, 628, 17, 2)
        self.round_8_team_7_8_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

    # todo------------------------------ line horizontal round4 --------------------------------* #

        self.round_4_team_1_line_horizontal = QPushButton(parent)
        self.round_4_team_1_line_horizontal.setGeometry(540, 253, 16, 2)
        self.round_4_team_1_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_4_team_2_line_horizontal = QPushButton(parent)
        self.round_4_team_2_line_horizontal.setGeometry(540, 629, 16, 2)
        self.round_4_team_2_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_4_team_3_line_horizontal = QPushButton(parent)
        self.round_4_team_3_line_horizontal.setGeometry(978, 252, 17, 2)
        self.round_4_team_3_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_4_team_4_line_horizontal = QPushButton(parent)
        self.round_4_team_4_line_horizontal.setGeometry(978, 628, 17, 2)
        self.round_4_team_4_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

    # todo------------------------------ line vertical round4 --------------------------------* #

        self.round_4_team_1_line_vertical = QPushButton(parent)
        self.round_4_team_1_line_vertical.setGeometry(556, 253, 2, 175)
        self.round_4_team_1_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color:  black;
                                      border: none;
                                      ''')

        self.round_4_team_2_line_vertical = QPushButton(parent)
        self.round_4_team_2_line_vertical.setGeometry(556, 430, 2, 201)
        self.round_4_team_2_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_4_team_3_line_vertical = QPushButton(parent)
        self.round_4_team_3_line_vertical.setGeometry(976, 252, 2, 176)
        self.round_4_team_3_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_4_team_4_line_vertical = QPushButton(parent)
        self.round_4_team_4_line_vertical.setGeometry(976, 429, 2, 201)
        self.round_4_team_4_line_vertical.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

    # todo------------------------------ line horizontal round4 --------------------------------* #

        self.round_4_team_1_2_line_horizontal = QPushButton(parent)
        self.round_4_team_1_2_line_horizontal.setGeometry(556, 428, 22, 2)
        self.round_4_team_1_2_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color:  black;
                                      border: none;
                                      ''')

        self.round_4_team_3_4_line_horizontal = QPushButton(parent)
        self.round_4_team_3_4_line_horizontal.setGeometry(956, 428, 22, 2)
        self.round_4_team_3_4_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')
    # todo------------------------------ line horizontal round4 --------------------------------* #

        self.round_2_team_1_line_horizontal = QPushButton(parent)
        self.round_2_team_1_line_horizontal.setGeometry(682, 428, 83, 2)
        self.round_2_team_1_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')

        self.round_2_team_2_line_horizontal = QPushButton(parent)
        self.round_2_team_2_line_horizontal.setGeometry(771, 428, 83, 2)
        self.round_2_team_2_line_horizontal.setStyleSheet('''
                                      background: transparent;
                                      background-color: black;
                                      border: none;
                                      ''')


    # *----------------------------------- button -------------------------------------* #

        self.set_up_match_button = QPushButton('Set up match', parent)
        self.set_up_match_button.setObjectName('set_up_match_button')
        self.set_up_match_button.setStyleSheet('''
                                QPushButton{
                                    border-radius: 20px;
                                    border: 2px solid #2a2a2a;
                                    color: aliceblue;
                                    background: transparent;
                                    background-color: #2a2a2a;
                                    font-family: TeX Gyre Adventor;
                                    font-size: 12px;
                                    font-weight: 900;
                                }
                                QPushButton:hover{
                                    border-radius: 20px;
                                    border: 2px solid #2a2a2a;
                                    color: #2a2a2a;
                                    background: transparent;
                                    background-color: #f3f3f3;
                                    font-family: TeX Gyre Adventor;
                                    font-size: 12px;
                                    font-weight: 900;
                                }
                                        ''')
        self.set_up_match_button.setGeometry(670, 690, 200, 40)
        self.set_up_match_button.clicked.connect(self.switch_to_set_up_match_from_tournament_32.emit)

    # *--------------------------------------------------------------------------------- #


    def tournament_name_input_box_check_none(self):
        text = self.tournament_name_input_box.text()
        if text != '':
            self.tournament_name_input_box_normal_border()
            self.tournament_name_error_label.setText('')
            self.tournament_name_label.setText(text)

            self.cursor.execute("SELECT COUNT(*) FROM tournament WHERE username = ?", (self.username,))
            count = self.cursor.fetchone()[0]

            if count == 0:
                self.cursor.execute("INSERT INTO tournament (username, tournament_name) VALUES (?, ?)", (self.username, text))
                print(f"\n✅ Inserted new tournament_name in tournament table: {text} \nfor username: {self.username}")
            else:
                self.cursor.execute("UPDATE tournament SET tournament_name = ? WHERE username = ?", (text, self.username))
                print(f"\n🆙 Updated existing tournament_name in tournament table: {text} \nfor username: {self.username}")

                self.cursor.execute("UPDATE teams SET tournament_name = ? WHERE username = ?", (text, self.username))
                print(f"\n🆙 Updated existing tournament_name in teams table: {text} \nfor username: {self.username}")

            self.connection.commit()

    def set_team_name(self,team_name):
        print(team_name)
        self.create_team1_button.setText(team_name)
        self.create_team1_button.setIcon(QIcon())

    def tournament_name_input_box_red_border(self):
        self.tournament_name_input_box.setStyleSheet('''
            QLineEdit#tournament_name_input_box{

                padding-left: 18px;
                background: transparent;
                color: #767676;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #ff7777;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }
            QLineEdit#tournament_name_input_box:hover,QLineEdit#tournament_name_input_box:focus:hover{

                padding-left: 18px;
                background: transparent;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #ff7777 !important;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }

            QLineEdit#tournament_name_input_box:focus{

                border-color: #ff7777;

            }

            QLineEdit#tournament_name_input_box::placeholder{

                padding-left: 18px;
                background: transparent;
                color: #dedede;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #dcdcdc;
                font-family: TeX Gyre Adventor;
                font-weight: 620;
            }''')

    def tournament_name_input_box_normal_border(self):
        self.tournament_name_input_box.setStyleSheet('''
            QLineEdit#tournament_name_input_box{

                padding-left: 18px;
                background: transparent;
                color: #767676;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #dcdcdc;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }
            QLineEdit#tournament_name_input_box:hover,QLineEdit#tournament_name_input_box:focus:hover{

                padding-left: 18px;
                background: transparent;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #ff56c7 !important;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }

            QLineEdit#tournament_name_input_box:focus{

                border-color: #2a2a2a;

            }

            QLineEdit#tournament_name_input_box::placeholder{

                padding-left: 18px;
                background: transparent;
                color: #dedede;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #dcdcdc;
                font-family: TeX Gyre Adventor;
                font-weight: 620;
            }''')

    def update_team_button(self, team_id, username, team_name):
        print(f"\n🛠 อัปเดตปุ่มทีม: team_id = {team_id}, team_name = {team_name}\n")
        button_name = f"create_team{team_id}_button"
        button = getattr(self, button_name, None)

        if button:
            button.setIcon(QIcon())
            button.setText(team_name)
            button.setStyleSheet('''
                                 QPushButton{
                                 border: none;
                                 background: transparent;
                                 background-color: #a9a9a9;
                                 color: black;
                                 font-weight: 600;
                                 }
                                 QPushButton:hover{
                                 border: none;
                                 background: transparent;
                                 background-color: #62000000;
                                 color: white;
                                 font-weight: 600;
                                 }
                                 ''')
            # button.clicked.connect(lambda: self.handle_create_team_button(team_id))

        self.cursor.execute("INSERT INTO teams (team_id, username, team_name, tournament_name) VALUES (?, ?, ?, ?)", (team_id, username, team_name, self.tournament_name_input_box.text()))
        self.connection.commit()

    def set_up_match(self):
        tournament_name = self.tournament_name_input_box.text()
        # self.cursor.execute("INSERT INTO tournaments (tournament_name) VALUES (?)", (tournament_name,))
        # self.connection.commit()
        # self.close()
        print('saved')

    def check_team_data(self, team_id):
        print(f"🔍 ตรวจสอบ team_id: {team_id}")
        if team_id is None:
            return False
        self.cursor.execute("SELECT COUNT(*) FROM teams WHERE team_id = ?", (team_id,))
        count = self.cursor.fetchone()[0]
        print(f"🔎 ฐานข้อมูลคืนค่า count = {count}")
        return count > 0

    def handle_create_team_button(self, team_id):
        print(f"🔍 กดปุ่มสร้างทีม ID: {team_id}")

        if self.tournament_name_input_box.text() == '':
            self.tournament_name_input_box_red_border()
            self.tournament_name_error_label.setText('Please enter tournament name')
            return
        else:
            self.tournament_name_input_box_normal_border()
            self.tournament_name_error_label.setText('')

            has_data = self.check_team_data(team_id)
            print(f"📊 check_team_data({team_id}) คืนค่า: {has_data}")

            if team_id is not None and has_data:
                print("✅ ไปหน้า 'ดูข้อมูล'")
                print(f"📡 ส่งค่าไปที่ stack: team_id = {team_id}")
                self.switch_to_create_team_from_tournament_32_.emit('ทีมที่เคยมีข้อมูล', team_id)
            else:
                print("🚀 ไปหน้า 'เพิ่มข้อมูล'")
                print(f"📡 ส่งค่าไปที่ stack: team_id = {team_id}")
                self.switch_to_create_team_from_tournament_32_.emit('สร้างทีมใหม่', team_id)

    def load_team_button(self,username):
        print('username : ',username)
        tournament_name_vb =  self.cursor.execute("SELECT tournament_name FROM tournament WHERE username = ?", (username,)).fetchone()
        self.tournament_name_label.setText(tournament_name_vb[0])
        if tournament_name_vb is None:
            return
        else:
            self.tournament_name_input_box.setText(tournament_name_vb[0])
            self.tournament_name_label.setText(tournament_name_vb[0])

            self.cursor.execute("SELECT team_id, team_name FROM teams")
            teams = self.cursor.fetchall()
            for team in teams:
                team_id, team_name = team

                print(f"\n🛠 สร้างปุ่มทีม: team_id = {team_id}, team_name = {team_name}\n")
                button_name = f"create_team{team_id}_button"
                button = getattr(self, button_name, None)

                if button:
                    button.setIcon(QIcon())
                    button.setText(team_name)
                    button.setStyleSheet('''
                                        QPushButton{
                                        border: none;
                                        background: transparent;
                                        background-color: #a9a9a9;
                                        color: black;
                                        font-weight: 600;
                                        }
                                        QPushButton:hover{
                                        border: none;
                                        background: transparent;
                                        background-color: #62000000;
                                        color: white;
                                        font-weight: 600;
                                        }
                                        ''')
                    # button.clicked.connect(lambda: self.handle_create_team_button(team_id))

    def fetch_usernames(self, username):
        self.username = username

    def update_round_16_buttons(self, winners):
        round_16_buttons = [
            self.round_16_team_1_button,
            self.round_16_team_2_button,
            self.round_16_team_3_button,
            self.round_16_team_4_button,
            self.round_16_team_5_button,
            self.round_16_team_6_button,
            self.round_16_team_7_button,
            self.round_16_team_8_button,
            self.round_16_team_9_button,
            self.round_16_team_10_button,
            self.round_16_team_11_button,
            self.round_16_team_12_button,
            self.round_16_team_13_button,
            self.round_16_team_14_button,
            self.round_16_team_15_button,
            self.round_16_team_16_button,
        ]

        for i, winner in enumerate(winners):
            if winner is not None:
                import re
                match = re.search(r'(\d+)', str(winner))  # หาเลขจากชื่อ เช่น team1 → 1
                if match:
                    winner_number = int(match.group(1))
                    index = (winner_number - 1) // 2
                    if 0 <= index < len(round_16_buttons):
                        round_16_buttons[index].setText(winner)
                    else:
                        print(f"⚠️ winner_number {winner_number} ทำให้ index เกินขอบเขต")
                else:
                    print(f"⚠️ หาเลขไม่เจอใน winner '{winner}'")
            else:
                print(f"ℹ️ ไม่มีผู้ชนะในตำแหน่ง {i}")

    def update_round_8_buttons(self, winners):
        round_8_buttons = [
            self.round_8_team_1_button,
            self.round_8_team_2_button,
            self.round_8_team_3_button,
            self.round_8_team_4_button,
            self.round_8_team_5_button,
            self.round_8_team_6_button,
            self.round_8_team_7_button,
            self.round_8_team_8_button,
        ]

        for i, winner in enumerate(winners):
            if winner is not None:
                import re
                match = re.search(r'(\d+)', str(winner))  # หาเลขจากชื่อ เช่น team1 → 1
                if match:
                    winner_number = int(match.group(1))
                    index = (winner_number - 1) // 2
                    if 0 <= index < len(round_8_buttons):
                        round_8_buttons[index].setText(winner)
                    else:
                        print(f"⚠️ winner_number {winner_number} ทำให้ index เกินขอบเขต")
                else:
                    print(f"⚠️ หาเลขไม่เจอใน winner '{winner}'")
            else:
                print(f"ℹ️ ไม่มีผู้ชนะในตำแหน่ง {i}")

    def update_round_4_buttons(self, winners):
        round_4_buttons = [
            self.round_4_team_1_button,
            self.round_4_team_2_button,
            self.round_4_team_3_button,
            self.round_4_team_4_button,
        ]

        for i, winner in enumerate(winners):
            if winner is not None:
                import re
                match = re.search(r'(\d+)', str(winner))  # หาเลขจากชื่อ เช่น team1 → 1
                if match:
                    winner_number = int(match.group(1))
                    index = (winner_number - 1) // 2
                    if 0 <= index < len(round_4_buttons):
                        round_4_buttons[index].setText(winner)
                    else:
                        print(f"⚠️ winner_number {winner_number} ทำให้ index เกินขอบเขต")
                else:
                    print(f"⚠️ หาเลขไม่เจอใน winner '{winner}'")
            else:
                print(f"ℹ️ ไม่มีผู้ชนะในตำแหน่ง {i}")


    def hide_set_up_match_button(self):
        self.set_up_match_button.hide()

#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    tournament32 = tournament32()
    tournament32.show()
    # tournament32.showMaximized()
    app.exec()
