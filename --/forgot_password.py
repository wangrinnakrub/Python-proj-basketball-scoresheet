
# * -------------------------------------- Forgot Password ----------------------------------------- #

# ------------------ import libary ------------------ #
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sqlite3

class Forgot_password_page(QMainWindow):
    switch_to_sign_in = pyqtSignal()
    switch_to_otp_check = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basketball Score Sheet - Forgot Password')
        self.setGeometry(360, 120, 700, 400) # x,y   w,h
        self.import_style('C:/Users/ASUS/OneDrive/Desktop/code/python/ED251007/project/style_forgot_password.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.username_or_email = ''
        self.username_or_email_focus = 0
        self.button_valid = False


        self.connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

        self.send_clicked = 0

        QTimer.singleShot(0, self.clear_initial_focus)
        self.installEventFilter(self)


    # *---------- clear focus ---------- #
    def clear_initial_focus(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.username_or_email_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.username_or_email_input_box.clearFocus()
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


    # *---------- forgot password page widget ---------- #
    def addWidgetsToLayout(self, ui):

        # *------- back to sign in -------* #
        self.back_button = QPushButton()
        self.back_button.setFixedSize(40, 40)
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_up')
        self.back_button.clicked.connect(self.switch_to_sign_in.emit)
        ui.addWidget(self.back_button ,alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        ui.addStretch(1)

        # *----------- forgot password ----------- #
        self.forgot_password_label = QLabel('Forgot Password')
        self.forgot_password_label.setObjectName('forgot_password_label')
        self.forgot_password_label.setFixedHeight(100)

        forgot_password_layout = QHBoxLayout()
        forgot_password_layout.addStretch()
        forgot_password_layout.addWidget(self.forgot_password_label,alignment=Qt.AlignmentFlag.AlignTop)
        forgot_password_layout.addStretch()
        ui.addLayout(forgot_password_layout)

        # ui.addSpacing(10)

        # *----------- Enter e-mail that link with email ----------- #

        self.please_enter_username_label = QLabel('Please enter your username or email to reset password')
        self.please_enter_username_label.setObjectName('please_enter_your_username_or_email_label')
        self.please_enter_username_label.setFixedHeight(25)

        enter_email_layout = QHBoxLayout()
        enter_email_layout.addStretch()
        enter_email_layout.addWidget(self.please_enter_username_label,alignment=Qt.AlignmentFlag.AlignTop)
        enter_email_layout.addStretch()
        ui.addLayout(enter_email_layout)

        ui.addSpacerItem(QSpacerItem(0, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))


        # *----------- Email ----------- #
        self.username_or_email_label = QLabel('Username or email')
        self.username_or_email_label.setObjectName('username_or_email_label')
        self.username_or_email_label.setFixedSize(350,60)

        username_or_email_layout = QHBoxLayout()
        username_or_email_layout.addStretch()
        username_or_email_layout.addWidget(self.username_or_email_label,alignment=Qt.AlignmentFlag.AlignTop)
        username_or_email_layout.addStretch()
        ui.addLayout(username_or_email_layout)

        self.username_or_email_input_box = QLineEdit()
        self.username_or_email_input_box.setObjectName('username_or_email_input_box')
        self.username_or_email_input_box.setPlaceholderText('Type your username or email')
        self.username_or_email_input_box.returnPressed.connect(self.username_or_email_enter)
        self.username_or_email_input_box.textChanged.connect(self.check_button_style_change)
        self.username_or_email_input_box.setFixedSize(305, 40)

        username_or_email_input_box_layout = QHBoxLayout()
        username_or_email_input_box_layout.setObjectName('username_or_email_input_box_layout')
        username_or_email_input_box_layout.addStretch()
        username_or_email_input_box_layout.addWidget(self.username_or_email_input_box,alignment=Qt.AlignmentFlag.AlignTop)
        username_or_email_input_box_layout.addStretch()
        ui.addLayout(username_or_email_input_box_layout)

        ui.addSpacing(3)

        # todo email error label
        self.username_or_email_error_label = QLabel('')
        self.username_or_email_error_label.setObjectName('username_or_email_error_label')
        self.username_or_email_error_label.setFixedHeight(25)
        self.username_or_email_input_box.setStyleSheet('''
QLineEdit#username_or_email_input_box {

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



QLineEdit#username_or_email_input_box:hover{

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

QLineEdit#username_or_email_input_box:focus {

    border-color: #2a2a2a;

}

QLineEdit#username_or_email_input_box::placeholder {

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

        # todo email error label layout
        username_or_email_error_label_layout = QHBoxLayout()
        username_or_email_error_label_layout.setObjectName('username_or_email_error_label_layout')
        username_or_email_error_label_layout.addStretch()
        username_or_email_error_label_layout.addWidget(self.username_or_email_error_label,alignment=Qt.AlignmentFlag.AlignTop)
        username_or_email_error_label_layout.addStretch()
        ui.addLayout(username_or_email_error_label_layout)

        ui.addSpacing(20)

        # *---------- Send button ----------- #
        self.send_button = QPushButton('Send')
        self.send_button.setObjectName('send_button')
        self.send_button.setFixedSize(230,37)
        self.send_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_button.clicked.connect(self.send_clicked)

        send_button_layout = QHBoxLayout()
        send_button_layout.setObjectName('send_button_layout')
        send_button_layout.setContentsMargins(0,10,0,65)
        send_button_layout.addStretch()
        send_button_layout.addWidget(self.send_button,alignment=Qt.AlignmentFlag.AlignTop)
        send_button_layout.addStretch()
        ui.addLayout(send_button_layout)

        ui.addStretch(2)

    # *---------- check username or email enter ---------- #
    def username_or_email_enter(self):
        self.username_or_email_focus += 1
        if self.username_or_email_focus >= 1:
            self.check_send()

    # *---------- check send clicked ---------- #
    def send_clicked(self):
        self.check_send()

    # *---------- check send ---------- #
    def check_send(self):
        self.username = self.username_or_email_input_box.text()

        if self.username == '':
            self.username_or_email_error_label.setText('Please enter your username or email')
            self.username_or_email_input_box_red_border()

        elif not self.button_valid:
            self.username_or_email_error_label.setText('We couldn\'t find an account with that username or email.')
            self.username_or_email_input_box_red_border()

        if self.button_valid:
            self.switch_to_otp_check.emit()
            self.clear_focus_from_all()


    def change_button_style_successful(self):
        self.send_button.setStyleSheet('''
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
        self.send_button.setStyleSheet('''
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
        self.username_or_email = self.username_or_email_input_box.text()

        self.cursor.execute("SELECT * FROM user_account WHERE username = ? OR email = ?", (self.username_or_email,self.username_or_email,))
        self.existing_user = self.cursor.fetchone()

        self.button_valid = False
        self.not_found = False

        self.username_or_email_error_label.setText('') if self.username_or_email == '' else print(f': {self.username_or_email}')

        if self.username_or_email != '':
                self.username_or_email_input_box_normal_border()
                self.username_or_email_error_label.setText('')
        else : pass

        if self.existing_user:
            if self.username_or_email == self.existing_user[1] or self.username_or_email == self.existing_user[5]:
                self.username_or_email_input_box_normal_border()
                self.email = self.existing_user[5]
                self.username_or_email_error_label.setText('')
                self.button_valid = True
        else: print('Not found')

        self.change_button_style_successful() if self.button_valid else self.change_back_button_style()

    def fetch_email(self): return self.email

    def clear_input_boxs(self): self.username_or_email_input_box.clear()

    def username_or_email_input_box_normal_border(self):
        self.username_or_email_input_box.setStyleSheet('''
QLineEdit#username_or_email_input_box {

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



QLineEdit#username_or_email_input_box:hover{

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

QLineEdit#username_or_email_input_box:focus {

    border-color: #2a2a2a;

}

QLineEdit#username_or_email_input_box::placeholder {

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

    def username_or_email_input_box_red_border(self):
        self.username_or_email_input_box.setStyleSheet('''
QLineEdit#username_or_email_input_box {

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



QLineEdit#username_or_email_input_box:hover{

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

QLineEdit#username_or_email_input_box:focus {

    border-color: #ff7777;

}

QLineEdit#username_or_email_input_box::placeholder {

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

#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    forgot_password = Forgot_password_page()
    forgot_password.show()
    app.exec()
