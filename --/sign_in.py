
# ? ter yu nai jai nan gwa yu kang gun , eab fun tueng ter yu , kae yak hai ru wa kid tueng ter kae nai , kor duang jai mun kong mai yorn kuen ma , lub tar lae kid tueng rueng dee dee , korb kun tee krang nueng mun kei gerd kuen jing 💫
#                                                        #!            __ __     __ __
#                      .-----------------.               #!         /////\\\\\  /       \
#                    .'                   '.             #!        ||||||/////  \        |
#                  .'                       '.           #!         \\\\\\\\\\  /       /
#                 /                           \          #!           \\\\////  \     /
#                ;                             ;         #!             \\\\\\  /   /
#                |      .-"``"-.       .-"``"-. |        #!               \\//  \ /
#                |     /  _  _  \     /  _  _  \|        #!
#                |    | #!(o)(o)  |   |  (o)(o) |        #!
#                |     \   ^     /     \   ^    /        #!
#                |       '.___.'        '.___.'  |       #!
#                 \                             /        #!
#                  '.           --------      .'         #!
#                    '-.___________________.-'           #!
#!                       ---------------                 #!
#!                 +--- |               | ---+           #!
#!                       ----       ----                 #!
#!                          |      |                     #!
#!                           ------                      #!
#                             |  |                       #!
#                            _|  |_                      #!
# ---------------------------------------- sign in ----------------------------------------- #

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sqlite3

class Signin_page(QMainWindow):
    switch_to_sign_up = pyqtSignal()
    switch_to_forgot_password = pyqtSignal()
    switch_to_main_window = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basketball Score Sheet - Sign In')
        self.setGeometry(0, 110, 700, 650)
        self.import_style('style_sign_in.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.username = ''
        self.password = ''
        self.username_focus = 0
        self.password_focus = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mask_last_character)

        self.sign_in_click = 0

        QTimer.singleShot(0, self.clear_initial_focus)
        self.installEventFilter(self)

        self.connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

    def clear_error_label(self):
        self.username_error_label.setText('')
        self.password_error_label.setText('')

    def clear_input_box(self):
        self.username_input_box.clear()
        self.password_input_box.clear()

    def clear_initial_focus(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.username_input_box, self.password_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.username_input_box.clearFocus()
        self.password_input_box.clearFocus()
        self.setFocus(Qt.FocusReason.OtherFocusReason)


    # *---------- import style from qss ---------- #
    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")


    # *---------- layout ---------- #
    def ui(self):
        self.layout = QVBoxLayout()
        self.addWidgetsToLayout(self.layout)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)


    # *---------- sign_in page widget ---------- #
    def addWidgetsToLayout(self, ui):

        ui.addStretch()
        # # *----------- SIGN_IN ----------- #
        # sign_in label
        self.sign_in_label = QLabel('Sign In')
        self.sign_in_label.setObjectName('sign_in_label')
        self.sign_in_label.setFixedHeight(100)

        # sign_in layout
        sign_in_layout = QHBoxLayout()
        sign_in_layout.addStretch()
        sign_in_layout.addWidget(self.sign_in_label)
        sign_in_layout.addStretch()
        ui.addLayout(sign_in_layout)

        ui.addStretch()

        # *----------- Username ----------- #
        # username label
        self.username_label = QLabel('Username or email')
        self.username_label.setObjectName('username_label')
        self.username_label.setFixedSize(350,90)

        # username label layout
        username_layout = QHBoxLayout()
        username_layout.addStretch()
        username_layout.addWidget(self.username_label)
        username_layout.addStretch()
        ui.addLayout(username_layout)

        # username input box
        self.username_input_box = QLineEdit()
        self.username_input_box.setObjectName('username_input_box')
        self.username_input_box.setPlaceholderText('Type your username or email')
        self.username_input_box.returnPressed.connect(self.username_enter)
        self.username_input_box.textChanged.connect(self.check_button_style_change)
        self.username_input_box.setFixedSize(305, 40)
        self.username_input_box.setStyleSheet('''
QLineEdit#username_input_box, QLineEdit#password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover  {

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

QLineEdit#username_input_box:focus,  QLineEdit#password_input_box:focus{

    border-color: #2a2a2a;

}

QLineEdit#username_input_box::placeholder, QLineEdit#password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;
}
                                              ''')

        # username input box layout
        username_input_box_layout = QHBoxLayout()
        username_input_box_layout.setObjectName('username_input_box_layout')
        username_input_box_layout.addStretch()
        username_input_box_layout.addWidget(self.username_input_box)
        username_input_box_layout.addStretch()
        ui.addLayout(username_input_box_layout)

        # todo username error label
        self.username_error_label = QLabel('')
        self.username_error_label.setObjectName('username_error_label')
        self.username_error_label.setFixedHeight(25)

        # todo username error label layout
        username_error_label_layout = QHBoxLayout()
        username_error_label_layout.setObjectName('username_error_label_layout')
        username_error_label_layout.addStretch()
        username_error_label_layout.addWidget(self.username_error_label)
        username_error_label_layout.addStretch()
        ui.addLayout(username_error_label_layout)

        # *----------- Password ----------- #
        # password label
        self.password_label = QLabel('Password')
        self.password_label.setObjectName('password_label')
        self.password_label.setFixedSize(350,30)

        # password label layout
        password_label_layout = QHBoxLayout()
        password_label_layout.addStretch()
        password_label_layout.addWidget(self.password_label)
        password_label_layout.addStretch()
        ui.addLayout(password_label_layout)

        # password input box
        self.password_input_box = QLineEdit()
        self.password_input_box.setObjectName('password_input_box')
        self.password_input_box.setPlaceholderText('Type your password')
        self.password_input_box.textChanged.connect(self.handle_text_change)
        self.password_input_box.textChanged.connect(self.check_button_style_change)
        self.password_input_box.returnPressed.connect(self.password_enter)
        self.password_input_box.setFixedSize(305,50)
        self.password_input_box.setStyleSheet('''
QLineEdit#username_input_box, QLineEdit#password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover  {

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

QLineEdit#username_input_box:focus,  QLineEdit#password_input_box:focus{

    border-color: #2a2a2a;

}

QLineEdit#username_input_box::placeholder, QLineEdit#password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;
}
                                              ''')
        self.previous_text = ''

        # password input box layout
        password_input_box_layout = QHBoxLayout()
        password_input_box_layout.setObjectName('password_input_box_layout')
        password_input_box_layout.addStretch()
        password_input_box_layout.addWidget(self.password_input_box)
        password_input_box_layout.addStretch()
        ui.addLayout(password_input_box_layout)

        # todo Password error label
        self.password_error_label = QLabel('')
        self.password_error_label.setObjectName('password_error_label')
        self.password_error_label.setFixedHeight(25)
        # self.password_error_label.setStyleSheet('color: red')

        # todo password error label layout
        password_error_label_layout = QHBoxLayout()
        password_error_label_layout.setObjectName('password_error_label_layout')
        password_error_label_layout.addStretch()
        password_error_label_layout.addWidget(self.password_error_label)
        password_error_label_layout.addStretch()
        ui.addLayout(password_error_label_layout)


        # *---------- forgot password ----------#
        # forgot password label
        self.forgot_password_label = QLabel("""<a href='#' style='

                                   width:200px;
                                   text-decoration: none;
                                   outline: none !important;
                                   color:#767676;
                                   font-size: 12px;

                                   '>forgot password</a>""")
        # self.forgot_password_label = QLabel('<a href="#">forgot password</a>')
        self.forgot_password_label.setObjectName('forgot_password_label')
        # self.forgot_password_label.setFixedSize(200,80)
        # self.forgot_password_label.setMinimumHeight(30)
        self.forgot_password_label.setFixedHeight(20)
        self.forgot_password_label.setContentsMargins(210,0,0,0)
        self.forgot_password_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.forgot_password_label.linkActivated.connect(self.switch_to_forgot_password.emit)

        # forgot password label layout
        forgot_password_label_layout = QHBoxLayout()
        forgot_password_label_layout.addStretch()
        forgot_password_label_layout.addWidget(self.forgot_password_label)
        forgot_password_label_layout.addStretch()
        ui.addLayout(forgot_password_label_layout)

        ui.addStretch()
        ui.addSpacing(30)

        # *---------- Sign_in button ----------- #
        # sign_in button
        self.sign_in_button = QPushButton('Sign In',self)
        # self.sign_in_button = GradientButton('Sign in',self)
        self.sign_in_button.setObjectName('sign_in_button')
        self.sign_in_button.setFixedSize(230,37)
        self.sign_in_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sign_in_button.clicked.connect(self.check_sign_in)

        # sign_in button layout
        sign_in_button_layout = QHBoxLayout()
        sign_in_button_layout.setObjectName('sign_in_button_layout')
        # sign_in_button_layout.setContentsMargins(0,0,0,20)
        sign_in_button_layout.addStretch()
        sign_in_button_layout.addWidget(self.sign_in_button)
        sign_in_button_layout.addStretch()
        ui.addLayout(sign_in_button_layout)

        # *---------- sign up ----------#
        self.signup_label = QLabel("""<a href='#' style='

                                   text-decoration: none;
                                   outline: none !important;
                                   color: #767676;
                                   font-size: 12px;

                                   '>Sign Up</a>""")
        self.signup_label.setObjectName('signup_label')
        self.signup_label.setFixedHeight(70)
        self.signup_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.signup_label.linkActivated.connect(self.switch_to_sign_up.emit)

        # sign up label layout
        signup_label_layout = QHBoxLayout()
        signup_label_layout.addStretch()
        signup_label_layout.addWidget(self.signup_label)
        signup_label_layout.addStretch()
        ui.addLayout(signup_label_layout)

        ui.addStretch()

    # *---------- password to ● ---------- #
    # show current password but if not type longer than 500 millisec it will change to dot
    def handle_text_change(self, text):
        if self.timer.isActive():
            self.timer.stop()

        if len(text) > len(self.previous_text):
            self.password += text[-1]
            masked_password = '●' * (len(self.password) - 1) + self.password[-1]
        elif len(text) < len(self.previous_text):
            self.password = self.password[:len(text)]
            masked_password = '●' * len(self.password)

        self.previous_text = text
        self.password_input_box.blockSignals(True)
        self.password_input_box.setText(masked_password)
        self.password_input_box.blockSignals(False)
        self.password_input_box.setCursorPosition(len(masked_password))

        self.timer.start(700)

    def mask_last_character(self):
        self.timer.stop()
        masked_password = '●' * len(self.password)
        self.password_input_box.blockSignals(True)
        self.password_input_box.setText(masked_password)
        self.password_input_box.blockSignals(False)
        self.password_input_box.setCursorPosition(len(masked_password))


    # *---------- check username enter ---------- #
    def username_enter(self):
        self.username_focus += 1
        if self.username_focus >= 1:
            self.check_sign_in()

        self.username = self.username_input_box.text()
        if self.username != '':
            self.password_input_box.setFocus()

    # *---------- check password enter ---------- #
    def password_enter(self):
        self.password_focus += 1
        if self.password_focus >= 1:
            self.check_sign_in()

    # *---------- check signin clicked ---------- #
    def sign_in_clicked(self):
        self.username = self.username_input_box.text()

        if self.username == '':
            self.username_enter()
        elif self.password == '':
            self.password_enter()
        else:
            self.check_sign_in()


    # *---------- check sign in ---------- #
    def check_sign_in(self):
        self.username = self.username_input_box.text()
        valid = True

        self.cursor.execute("SELECT * FROM user_account WHERE username = ? OR email = ?", (self.username,self.username))
        self.existing_user = self.cursor.fetchone()

        if self.username == '':
            self.username_error_label.setText('Please enter your username')
            self.username_input_box_red_border()
            self.password_error_label.setText('')

        elif self.password == '':
            self.username_error_label.setText('')
            if self.password_focus >= 1:
                self.password_error_label.setText('Please enter your password')
                self.password_input_box_red_border()

        if self.username != '':
            self.username_error_label.setText('')
            self.username_input_box_normal_border()
        if self.password != '':
            self.password_error_label.setText('')
            self.password_input_box_normal_border()

        if self.username != '' and self.password != '':
            if self.existing_user:
                if (self.username == self.existing_user[1] or self.username == self.existing_user[5]) and self.password == self.existing_user[2]:
                    self.setFocus(Qt.FocusReason.OtherFocusReason)
                    self.switch_to_main_window.emit()
                else:
                    self.password_error_label.setText('Invalid username or password')
                    self.username_input_box_red_border()
                    self.password_input_box_red_border()
            else:
                self.password_error_label.setText('Invalid username or password')
                self.username_input_box_red_border()
                self.password_input_box_red_border()


    def change_button_style_successful(self):
        self.sign_in_button.setStyleSheet('''
            QPushButton{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #f203ff, stop:1 #0099ff);
            color: white;
            }
            QPushButton:hover{
            background: #ffffff;
            color: #d83aff;
            }
        ''')

    def change_back_button_style(self):
        self.sign_in_button.setStyleSheet('''
            QPushButton{
            background-color: #2a2a2a;
            color:#ffffff;
            }
            QPushButton:hover{
            background-color: #ffffff;
            color:#2a2a2a;
            }
        ''')

    def check_button_style_change(self):
        self.username = self.username_input_box.text()

        self.cursor.execute("SELECT * FROM user_account WHERE username = ? OR email = ?", (self.username,self.username))
        self.existing_user = self.cursor.fetchone()

        self.button_valid = False

        if self.username == '':
            self.username_error_label.setText('')
            self.username_input_box_normal_border()
            self.button_valid = False
        if self.password == '':
            self.password_error_label.setText('')
            self.password_input_box_normal_border()
            self.button_valid = False

        if len(self.username) > 0:
            self.username_error_label.setText('')
            self.username_input_box_normal_border()
        if len(self.password) > 0:
            self.password_error_label.setText('')
            self.password_input_box_normal_border()

        if self.username != '' and self.password != '':
            if self.existing_user:
                if (self.username == self.existing_user[1] or self.username == self.existing_user[5]) and self.password == self.existing_user[2]:
                    self.username_input_box_normal_border()
                    self.password_input_box_normal_border()
                    self.button_valid = True
            else : self.button_valid = False

        self.change_button_style_successful() if self.button_valid else self.change_back_button_style()

    def username_input_box_normal_border(self):
        self.username_input_box.setStyleSheet('''
QLineEdit#username_input_box, QLineEdit#password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover  {

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

QLineEdit#username_input_box:focus,  QLineEdit#password_input_box:focus{

    border-color: #2a2a2a;

}

QLineEdit#username_input_box::placeholder, QLineEdit#password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;
}
                                              ''')

    def password_input_box_normal_border(self):
        self.password_input_box.setStyleSheet('''
QLineEdit#username_input_box, QLineEdit#password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover  {

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

QLineEdit#username_input_box:focus,  QLineEdit#password_input_box:focus{

    border-color: #2a2a2a;

}

QLineEdit#username_input_box::placeholder, QLineEdit#password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;
}
                                              ''')

    def username_input_box_red_border(self):
        self.username_input_box.setStyleSheet('''
QLineEdit#username_input_box, QLineEdit#password_input_box {

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
QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover  {

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

QLineEdit#username_input_box:focus,  QLineEdit#password_input_box:focus{

    border-color: #ff7777;

}

QLineEdit#username_input_box::placeholder, QLineEdit#password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;
}
                                              ''')

    def password_input_box_red_border(self):
        self.password_input_box.setStyleSheet('''
QLineEdit#username_input_box, QLineEdit#password_input_box {

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
QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover  {

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

QLineEdit#username_input_box:focus,  QLineEdit#password_input_box:focus{

    border-color: #ff7777;

}

QLineEdit#username_input_box::placeholder, QLineEdit#password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;
}
                                              ''')

    def fetched_username(self):
        if self.username == self.existing_user[1]:
            return self.existing_user[1]
        elif self.username == self.existing_user[5]:
            return self.existing_user[1]

    def clear_username_password_focus(self):
        self.username_focus = 0
        self.password_focus = 0

#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    sign_in = Signin_page()
    # sign_in.show()
    sign_in.showMaximized()
    app.exec()
