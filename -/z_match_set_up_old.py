from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from zz_match_set_up_pop_up import AddPlayer
import sys, sqlite3

class HoverButton(QPushButton):
    def __init__(self, file_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if file_name == 'c:\pic\plus_icon.png':
            self.file_name = file_name
            self.file_name_hover = r'c:\pic\plus_icon_hover_white.png'
        else:
            self.file_name = file_name
            self.file_name_hover = r'c:\pic\change_image_label.png'

        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(127,127))

    def enterEvent(self, event):
        self.setStyleSheet("background-color: #d3d3d3;")
        self.setIcon(QIcon(self.file_name_hover))
        self.setIconSize(QSize(127,127))
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(127,127))
        self.setStyleSheet("")
        super().leaveEvent(event)

class Match_set_up(QMainWindow):
    switch_to_match_setup = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Match Setup")
        self.setGeometry(100, 60, 1000, 750)
        self.setMinimumSize(1000, 750)
        self.import_style('style_z_match_set_up.qss')
        self.ui()
        self.installEventFilter(self)
        self.clear_focus_from_all()
        self.connection = sqlite3.connect(r'C:/Users/ASUS/OneDrive/Desktop/Dabest/basketball_score_sheet.db')
        self.cursor = self.connection.cursor()


    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [ self.team1_input_box,self.team2_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.team1_input_box.clearFocus()
        self.team2_input_box.clearFocus()
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def ui(self):
        self.layout = QHBoxLayout()
        self.addWidgetsToLayout(self.layout)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

    def addWidgetsToLayout(self, ui):

        self.team1_layout = QVBoxLayout()
        self.team2_layout = QVBoxLayout()
        self.mid_layout = QVBoxLayout()

        self.mid_layout_widget = QWidget()
        self.mid_layout_widget.setObjectName('mid_layout_widget')
        self.mid_layout_widget.setLayout(self.mid_layout)
        self.mid_layout_widget.setFixedWidth(3)

        # * team1
        self.team1_label = QLabel('Team 1')
        self.team1_label.setObjectName('team1_label')
        self.team1_label.setFixedSize(245, 30)

        self.team1_label_layout = QHBoxLayout()
        self.team1_label_layout.addWidget(self.team1_label)

        self.team1_input_box = QLineEdit()
        self.team1_input_box.setPlaceholderText('Team1 name')
        self.team1_input_box.setObjectName('team1_input_box')
        self.team1_input_box.setFixedSize(200, 40)
        self.team1_input_box.setStyleSheet('''
            QLineEdit#team1_input_box{

                padding-left: 25px;
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
            QLineEdit#team1_input_box:hover,QLineEdit#team1_input_box:focus:hover{

                padding-left: 25px;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #ff56c7 !important;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }

            QLineEdit#team1_input_box:focus{

                border-color: #2a2a2a;

            }

            QLineEdit#team1_input_box::placeholder{

                padding-left: 25px;
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

        self.team1_input_box.textChanged.connect(self.team1_name_check_none)

        self.team1_input_box_layout = QHBoxLayout()
        self.team1_input_box_layout.addWidget(self.team1_input_box)

        self.team1_error_label = QLabel('')
        self.team1_error_label.setObjectName('team1_error_label')
        self.team1_error_label.setFixedSize(126, 30)
        self.team1_error_label.setStyleSheet('''
            QLabel#team1_error_label{

                color: #ff4343;

            }''')

        self.team1_error_label_layout = QHBoxLayout()
        self.team1_error_label_layout.addWidget(self.team1_error_label)

        self.team1_add_player_button = HoverButton('c:\pic\plus_icon.png')
        self.team1_add_player_button.setIcon(QIcon(r'c:\pic\plus_icon.png'))
        self.team1_add_player_button.setIconSize(QSize(127,127))
        self.team1_add_player_button.setObjectName('team1_add_player_button')
        self.team1_add_player_button.setFixedSize(120,140)
        self.team1_add_player_button.clicked.connect(self.team1_add_player)

        self.team1_add_player_button_layout = QVBoxLayout()
        self.team1_add_player_button_layout.addWidget(self.team1_add_player_button)

        self.team1_player_layout = QHBoxLayout()
        self.team1_player_layout.addLayout(self.team1_add_player_button_layout)
        self.team1_player_layout.addSpacing(10)

        self.team1_layout.addLayout(self.team1_label_layout)
        self.team1_layout.addLayout(self.team1_input_box_layout)
        self.team1_layout.addLayout(self.team1_error_label_layout)
        self.team1_layout.addStretch(1)
        self.team1_layout.addLayout(self.team1_player_layout)
        self.team1_layout.addStretch(2)


        # * team2
        self.team2_label = QLabel('Team 2')
        self.team2_label.setObjectName('team2_label')
        self.team2_label.setFixedSize(245, 30)

        self.team2_label_layout = QHBoxLayout()
        self.team2_label_layout.addWidget(self.team2_label)

        self.team2_input_box = QLineEdit()
        self.team2_input_box.setPlaceholderText('Team2 name')
        self.team2_input_box.setObjectName('team2_input_box')
        self.team2_input_box.setFixedSize(200, 40)
        self.team2_input_box.setStyleSheet('''
            QLineEdit#team2_input_box{

                padding-left: 25px;
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
            QLineEdit#team2_input_box:hover,QLineEdit#team2_input_box:focus:hover{

                padding-left: 25px;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;

                border-right: transparent;
                border-color: #ff56c7 !important;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }

            QLineEdit#team2_input_box:focus{

                border-color: #2a2a2a;

            }

            QLineEdit#team2_input_box::placeholder{

                padding-left: 25px;
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
        self.team2_input_box.textChanged.connect(self.team2_name_check_none)

        self.team2_input_box_layout = QHBoxLayout()
        self.team2_input_box_layout.addWidget(self.team2_input_box)

        self.team2_error_label = QLabel('')
        self.team2_error_label.setObjectName('team2_error_label')
        self.team2_error_label.setFixedSize(126, 30)
        self.team2_error_label.setStyleSheet('''
            QLabel#team2_error_label{

                color: #ff4343;

            }''')

        self.team2_error_label_layout = QHBoxLayout()
        self.team2_error_label_layout.addWidget(self.team2_error_label)

        self.team2_add_player_button = HoverButton('c:\pic\plus_icon.png')
        self.team2_add_player_button.setIcon(QIcon(r'c:\pic\plus_icon.png'))
        self.team2_add_player_button.setIconSize(QSize(127,127))
        self.team2_add_player_button.setObjectName('team2_add_player_button')
        self.team2_add_player_button.setFixedSize(120,140)
        self.team2_add_player_button.clicked.connect(self.team2_add_player)

        self.team2_add_player_button_layout = QVBoxLayout()
        self.team2_add_player_button_layout.addWidget(self.team2_add_player_button)

        self.team2_player_layout = QHBoxLayout()
        self.team2_player_layout.addLayout(self.team2_add_player_button_layout)
        # self.team2_player_layout.addSpacerItem(QSpacerItem(30, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        self.team2_player_layout.addSpacing(10)

        self.team2_layout.addLayout(self.team2_label_layout)
        self.team2_layout.addLayout(self.team2_input_box_layout)
        self.team2_layout.addLayout(self.team2_error_label_layout)
        self.team2_layout.addStretch(1)
        self.team2_layout.addLayout(self.team2_player_layout)
        self.team2_layout.addStretch(2)

        ui.addStretch()
        ui.addLayout(self.team1_layout)
        ui.addStretch()
        ui.addWidget(self.mid_layout_widget)
        ui.addStretch()
        ui.addLayout(self.team2_layout)
        ui.addStretch()

    def mid_layout_resizer(self,event):
        self.mid_layout_widget.setFixedHeight(self.height())
        super().resizeEvent(event)

    def team1_name_check_none(self):
        self.team1_check_none = self.team1_input_box.text()
        if self.team1_check_none != '':
            self.team_name1_input_box_normal_border()
            self.team1_error_label.setText('')

    def team2_name_check_none(self):
        self.team2_check_none = self.team2_input_box.text()
        if self.team2_check_none != '':
            self.team_name2_input_box_normal_border()
            self.team2_error_label.setText('')

    def team1_add_player(self):
        print('team1_add_player')

        self.team_name1 = self.team1_input_box.text()
        if self.team_name1 == '':
            self.team_name1_input_box_red_border()
            self.team_name2_input_box_normal_border()
            self.team1_error_label.setText('Please enter team name')
            self.team2_error_label.setText('')
            return
        else: pass

        self.team_name1_input_box_normal_border()
        self.team1_error_label.setText('')

        self.add_player_pop_up = AddPlayer()
        self.final_text_team1 = self.team1_input_box.text() + '    '
        self.add_player_pop_up.set_team_name_label(self.final_text_team1)
        self.add_player_pop_up.player_shirt_team1()

        parent_pos = self.team1_input_box.mapToGlobal(QPoint(0, 0))
        team1 = QRect(parent_pos, self.team1_input_box.size())
        x = team1.left() - (team1.width()//2) + 10
        y = team1.top() + (self.height()//10)
        self.add_player_pop_up.move(x, y)

        result = self.add_player_pop_up.exec()
        print(result)
        if result:
            print('ok')
            self.player_shirt_button = self.add_player_pop_up.get_player_shirt()
            # self.player_shirt_button.setStyleSheet(self.add_player_pop_up.get_player_shirt_style())
            self.player_shirt_button.setStyleSheet('''QPushButton#player_shirt{
                border-image: url('C:/pic/basketball_shirt_yellow_purple.png') 0 0 0 0 stretch stretch;
                border: none; /* ลบเส้นขอบ */
                padding: 0;
                font-size: 50px;
                color: #612ca4;
                font-family: TeX Gyre Adventor;
            }''')

            self.player_name_label = self.add_player_pop_up.get_player_name_under_shirt_label()
            self.player_name_label.setStyleSheet(self.add_player_pop_up.get_player_name_under_shirt_label_style())

            self.player_shirt_button_layout = QVBoxLayout()

            self.center_layout_team1 = QHBoxLayout()
            self.center_layout_team1.addStretch()
            self.center_layout_team1.addWidget(self.player_shirt_button)
            self.center_layout_team1.addStretch()

            self.center_layout_team1_2 = QHBoxLayout()
            self.center_layout_team1_2.addStretch()
            self.center_layout_team1_2.addWidget(self.player_name_label)
            self.center_layout_team1_2.addStretch()

            self.player_shirt_button_layout.addLayout(self.center_layout_team1)
            self.player_shirt_button_layout.addLayout(self.center_layout_team1_2)

            self.team1_player_layout.insertSpacing(0,10)
            self.team1_player_layout.insertLayout(0,self.player_shirt_button_layout)
            self.team1_player_layout.addSpacing(10)
        else:
            print('cancel')


    def team2_add_player(self):
        print('team2_add_player')

        self.team_name2 = self.team2_input_box.text()
        if self.team_name2 == '':
            self.team_name2_input_box_red_border()
            self.team_name1_input_box_normal_border()
            self.team2_error_label.setText('Please enter team name')
            self.team1_error_label.setText('')
            return
        else: pass

        self.team_name2_input_box_normal_border()
        self.team2_error_label.setText('')

        self.add_player_pop_up2 = AddPlayer()
        self.final_text_team2 = self.team2_input_box.text() + '    '
        self.add_player_pop_up2.set_team_name_label(self.final_text_team2)
        self.add_player_pop_up2.player_shirt_team2()

        parent_pos = self.team2_input_box.mapToGlobal(QPoint(0, 0))
        team2 = QRect(parent_pos, self.team2_input_box.size())
        x = team2.left() - (team2.width()//2) + 10
        y = team2.top() + (self.height()//10)
        self.add_player_pop_up2.move(x, y)

        result = self.add_player_pop_up2.exec()
        print(result)
        if result:
            print('ok')
            self.player_shirt_button2 = self.add_player_pop_up2.get_player_shirt()
            # self.player_shirt_button2.setStyleSheet(self.add_player_pop_up2.get_player_shirt_style())
            self.player_shirt_button2.setStyleSheet('''QPushButton#player_shirt{
                border-image: url('C:/pic/basketball_shirt_black_red.png') 0 0 0 0 stretch stretch;
                border: none; /* ลบเส้นขอบ */
                padding: 0;
                font-size: 50px;
                color: #c80000;
                font-family: TeX Gyre Adventor;
}''')

            self.player_name_label_2 = self.add_player_pop_up2.get_player_name_under_shirt_label()
            self.player_name_label_2.setStyleSheet(self.add_player_pop_up2.get_player_name_under_shirt_label_style())

            self.player_shirt_button_layout2 = QVBoxLayout()

            self.center_layout_team2 = QHBoxLayout()
            self.center_layout_team2.addStretch()
            self.center_layout_team2.addWidget(self.player_shirt_button2)
            self.center_layout_team2.addStretch()

            self.center_layout_team2_2 = QHBoxLayout()
            self.center_layout_team2_2.addStretch()
            self.center_layout_team2_2.addWidget(self.player_name_label_2)
            self.center_layout_team2_2.addStretch()

            self.player_shirt_button_layout2.addLayout(self.center_layout_team2)
            self.player_shirt_button_layout2.addLayout(self.center_layout_team2_2)

            self.team2_player_layout.insertSpacing(0,10)
            # self.team2_player_layout.addSpacing(20)
            self.team2_player_layout.insertLayout(0,self.player_shirt_button_layout2)
            self.team2_player_layout.addSpacing(10)

        else:
            print('cancel')

    def team_name1_input_box_red_border(self):
        self.team1_input_box.setStyleSheet('''
            QLineEdit#team1_input_box{

                padding-left: 25px;
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
            QLineEdit#team1_input_box:hover,QLineEdit#team1_input_box:focus:hover{

                padding-left: 25px;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #ff7777 !important;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }

            QLineEdit#team1_input_box:focus{

                border-color: #ff7777;

            }

            QLineEdit#team1_input_box::placeholder{

                padding-left: 25px;
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

    def team_name1_input_box_normal_border(self):
        self.team1_input_box.setStyleSheet('''
            QLineEdit#team1_input_box{

                padding-left: 25px;
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
            QLineEdit#team1_input_box:hover,QLineEdit#team1_input_box:focus:hover{

                padding-left: 25px;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #ff56c7 !important;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }

            QLineEdit#team1_input_box:focus{

                border-color: #2a2a2a;

            }

            QLineEdit#team1_input_box::placeholder{

                padding-left: 25px;
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

    def team_name2_input_box_red_border(self):
        self.team2_input_box.setStyleSheet('''
            QLineEdit#team2_input_box{

                padding-left: 25px;
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
            QLineEdit#team2_input_box:hover,QLineEdit#team2_input_box:focus:hover{

                padding-left: 25px;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #ff7777 !important;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }

            QLineEdit#team2_input_box:focus{

                border-color: #ff7777;

            }

            QLineEdit#team2_input_box::placeholder{

                padding-left: 25px;
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

    def team_name2_input_box_normal_border(self):
        self.team2_input_box.setStyleSheet('''
            QLineEdit#team2_input_box{

                padding-left: 25px;
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
            QLineEdit#team2_input_box:hover,QLineEdit#team2_input_box:focus:hover{

                padding-left: 25px;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #ff56c7 !important;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }

            QLineEdit#team2_input_box:focus{

                border-color: #2a2a2a;

            }

            QLineEdit#team2_input_box::placeholder{

                padding-left: 25px;
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Match_set_up()
    window.show()
    sys.exit(app.exec())
